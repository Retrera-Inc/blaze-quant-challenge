import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import TimeSeriesSplit
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the time series data
df = pd.read_csv('modified_file_with_technical_parameters.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Drop non-numeric columns and unnecessary features
features = df.drop(['Tomorrow Price'], axis=1)
target = df['Tomorrow Price']

# Use TimeSeriesSplit for time series cross-validation
tscv = TimeSeriesSplit(n_splits=2)

# Initialize the linear regression model
model = LinearRegression()

# Perform time series cross-validation
for train_index, test_index in tscv.split(features):
    X_train, X_test = features.iloc[train_index], features.iloc[test_index]
    y_train, y_test = target.iloc[train_index], target.iloc[test_index]

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions on the test set
    predictions = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, predictions)
    print(f'Mean Squared Error: {mse}')

# Make a prediction for tomorrow's price using the latest data point
latest_data_point = features.iloc[-1].values.reshape(1, -1)
predicted_price = model.predict(latest_data_point)
print(predicted_price)
print(f'Predicted Tomorrow\'s Price: {predicted_price[0]}')

# Visualize actual vs. predicted values with connected dots
plt.figure(figsize=(10, 6))
plt.plot(y_test.index, y_test, marker='o', linestyle='-', color='blue', label='Actual Tomorrow\'s Price')
plt.plot(y_test.index, predictions, marker='o', linestyle='-', color='red', label='Predicted Tomorrow\'s Price')
plt.title('Actual vs Predicted Tomorrow\'s Price')
plt.xlabel('Date')
plt.ylabel('Tomorrow\'s Price')
plt.legend()
plt.show()
