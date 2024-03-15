import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

# Download ETH data
eth_data = yf.download('ETH-USD', start='2017-11-09', end='2024-03-15')

# Drop rows with missing values
eth_data.dropna(inplace=True)

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

# Feature selection
eth_data = eth_data[['Close']]

# Scaling data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(eth_data)

# Define function to create sequences
def create_sequences(data, seq_length):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:(i + seq_length)])
        y.append(data[i + seq_length])
    return np.array(X), np.array(y)

# Choose sequence length (input window)
seq_length = 10

# Create sequences
X, y = create_sequences(scaled_data, seq_length)

# Split data into training and validation sets
train_size = int(len(X) * 0.8)
X_train, X_val = X[:train_size], X[train_size:]
y_train, y_val = y[:train_size], y[train_size:]

# Build LSTM model
model = Sequential([
    LSTM(50, input_shape=(X.shape[1], X.shape[2])),
    Dropout(0.2),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')

# Train model
history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_val, y_val), verbose=1)

# Plot training history
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.legend()
plt.show()

from sklearn.metrics import mean_squared_error

# Inverse scaling
actual_prices = scaler.inverse_transform(y_val[-6:].reshape(-1, 1))
predicted_prices = scaler.inverse_transform(np.array(future_forecast).reshape(-1, 1))

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(actual_prices, predicted_prices))
print("Root Mean Square Error (RMSE):", rmse)

y_train_pred = model.predict(X_train)
y_val_pred = model.predict(X_val)

# Inverse transform the scaled predicted prices
y_train_pred_inv = scaler.inverse_transform(y_train_pred)
y_val_pred_inv = scaler.inverse_transform(y_val_pred)

# Plot actual and predicted prices for training data
plt.figure(figsize=(12, 6))
plt.plot(eth_data.index[:train_size], eth_data['Close'][:train_size], label='Actual Prices (Training)', color='blue')
plt.plot(eth_data.index[:train_size][-len(y_train_pred_inv):], y_train_pred_inv, label='Predicted Prices (Training)', linestyle='dashed', color='orange')
plt.title('Actual vs Predicted Prices (Training Data)')

plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot actual and predicted prices for validation data
plt.figure(figsize=(12, 6))
plt.plot(eth_data.index[train_size:], eth_data['Close'][train_size:], label='Actual Prices (Validation)', color='blue')
plt.plot(eth_data.index[train_size:][-len(y_val_pred_inv):], y_val_pred_inv, label='Predicted Prices (Validation)', linestyle='dashed', color='orange')
plt.title('Actual vs Predicted Prices (Validation Data)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Predict the next 6 days' prices
future_forecast = forecast_future_values(model, X_val[-1], 7)

# Inverse transform the scaled predicted prices
future_forecast_inv = scaler.inverse_transform(np.array(future_forecast).reshape(-1, 1))

# Extend dates to include the next 6 days
next_days = pd.date_range(start=eth_data.index[-1] + pd.Timedelta(days=1), periods=7)

# Plot actual and predicted prices for validation data
plt.figure(figsize=(12, 6))
plt.plot(eth_data.index[train_size:], eth_data['Close'][train_size:], label='Actual Prices (Validation)', color='blue')
plt.plot(eth_data.index[train_size:][-len(y_val_pred_inv):], y_val_pred_inv, label='Predicted Prices (Validation)', linestyle='dashed', color='orange')
plt.plot(next_days, future_forecast_inv, label='Predicted Prices (Future)', linestyle='dotted', color='green')
plt.title('Actual vs Predicted Prices (Validation Data and Future Predictions)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Print the date and predicted value for each of the next 6 days
print("Date\t\tPredicted Price")
for date, price in zip(next_days, future_forecast_inv):
    print(f"{date.strftime('%Y-%m-%d')}\t${price[0]:.2f}")
