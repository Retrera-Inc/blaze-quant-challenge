import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt

# Load your dataset
# Assuming your dataset is stored in a variable named 'data'
# Modify this according to your actual dataset structure
# Example assuming the file is named 'modified_file_with_technical_parameters.csv'
data = pd.read_csv('modified_file_with_technical_parameters.csv')

# Data preprocessing
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data.drop(columns=['Date', 'Change']))

# Define a function to create time series sequences
def create_sequences(data, sequence_length=10):
    sequences = []
    target = []
    for i in range(len(data) - sequence_length):
        seq = data[i:i + sequence_length, :]
        label = data[i + sequence_length, 0]  # Assuming 'Price' is the first column
        sequences.append(seq)
        target.append(label)
    return np.array(sequences), np.array(target)

# Create sequences
sequence_length = 10
X, y = create_sequences(data_scaled, sequence_length)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Build the GRU model
model = Sequential()
model.add(GRU(50, activation='relu', input_shape=(sequence_length, X.shape[2])))
model.add(Dense(1))  # Output layer

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')

# Train the model
model.fit(X_train, y_train, epochs=5, batch_size=32, validation_data=(X_test, y_test), verbose=1)

# Evaluate the model
loss = model.evaluate(X_test, y_test)
print(f'Mean Squared Error on Test Set: {loss}')

# Make predictions
predictions = model.predict(X_test)

# Extract the last time step of the input sequences for inverse transform
last_sequence = X_test[:, -1, :]

# Concatenate the last time step of input sequences and predictions
combined_array = np.concatenate((last_sequence, predictions), axis=1)

# Inverse transform the scaled predictions to original values
predictions_original_scale = scaler.inverse_transform(combined_array)

# Assuming 'Price' is the first column in your original data
predictions_original_scale = predictions_original_scale[:, 0]

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(data['Date'][-len(y_test):], y_test, label='True Prices', marker='.')
plt.plot(data['Date'][-len(y_test):], predictions_original_scale, label='Predicted Prices', marker='.')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Ethereum Price Prediction with GRU')
plt.legend()
plt.show()
