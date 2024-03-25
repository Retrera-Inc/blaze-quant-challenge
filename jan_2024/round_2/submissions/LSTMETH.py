import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense, Dropout, LSTM, BatchNormalization
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.initializers import GlorotNormal

class ETHPriceRanges:
    def __init__(self, date, predicted_close):
        self.date = date
        self.predicted_close = predicted_close

def predictions():
    crypto_currency = "ETH"
    against_currency = "USD"
    train_data = pd.read_csv('ETH.csv')

    # Display the first few rows of each dataset for verification
    print("Train Dataset:")
    print(train_data.head())

    # Convert 'Date' column to datetime
    train_data['Date'] = pd.to_datetime(train_data['Date'])
    train_data.set_index('Date', inplace=True)

    # Drop unnecessary columns
    train_data.drop(columns=['Open', 'High', 'Low', 'Volume'], inplace=True)

    # Fill NaN values with 0
    train_data.fillna(0, inplace=True)

    # Choose relevant features for scaling
    features = ['Close']

    # Scale the selected features
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(train_data[features])

    # Define the prediction_days and create input sequences and labels
    prediction_days = 60
    x_train, y_train = [], []

    for x in range(prediction_days, len(scaled_data)):
        x_train.append(scaled_data[x - prediction_days:x, 0])
        y_train.append(scaled_data[x, 0])

    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    # Split the data into training and testing sets
    test_size = 0.2
    x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=test_size, random_state=42)

    # Build the LSTM model
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1), kernel_initializer=GlorotNormal()))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))

    # Add BatchNormalization layer
    model.add(BatchNormalization())

    optimizer = Adam(learning_rate=0.001)
    model.compile(optimizer=optimizer, loss='mean_squared_error')

    # Training
    model.fit(x_train, y_train, epochs=16, batch_size=32, validation_data=(x_test, y_test))

    # Specify the number of future days for which you want to predict
    future_prediction_days = 7

    # Generate sequences for future dates
    future_dates = pd.date_range(start='2024-02-01', periods=future_prediction_days, freq='D')

    # Create an initial input sequence for prediction
    last_sequence = scaled_data[-prediction_days:].reshape(1, -1, 1)
    input_sequence = last_sequence.copy()

    # Predict future prices
    future_prices = []

    for day in range(future_prediction_days):
        predicted_price = model.predict(input_sequence)
        future_prices.append(predicted_price[0, 0])

        # Update the input sequence for the next prediction
        input_sequence = np.roll(input_sequence, -1, axis=1)
        input_sequence[0, -1, 0] = predicted_price[0, 0]

    # Inverse transform to get the original scale
    future_prices = scaler.inverse_transform(np.array(future_prices).reshape(-1, 1))

    # Create a list of ETHPriceRanges objects
    preds = [ETHPriceRanges(date=date, predicted_close=price) for date, price in zip(future_dates, future_prices[:, 0])]

    # Display the predicted prices for future dates
    for pred in preds:
        print(f"Date: {pred.date}, Predicted Close: {pred.predicted_close}")

    return preds

# Call the function to execute the predictions
preds = predictions()

# Assertions
assert len(preds) == 7
assert all([isinstance(val, ETHPriceRanges) for val in preds])
