import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM
import datetime as dt

from instructions import ETHPriceRanges

def fetch_data(crypto_currency="ETH", against_currency="USD", start_date="2018-01-01", end_date=dt.datetime.now().strftime("%Y-%m-%d")):
    data = yf.download(f"{crypto_currency}-{against_currency}", start=start_date, end=end_date)
    return data['Close']

def preprocess_data(data, prediction_days=60):
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data.values.reshape(-1, 1))
    x_train, y_train = [], []
    for x in range(prediction_days, len(scaled_data)):
        x_train.append(scaled_data[x-prediction_days:x, 0])
        y_train.append(scaled_data[x, 0])
    if not x_train:
        print("x_train is empty. Check your data and prediction_days.")
        return np.array([]), np.array([]), scaler
    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    return x_train, y_train, scaler

def build_model(input_shape):
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=input_shape))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def get_price_range(price):
    for enum_value in ETHPriceRanges:
        range_start, range_end = map(int, enum_value.name.split('_')[1:3])
        if range_start <= price < range_end:
            return enum_value
    return None

def predict_next_7_days(model, last_days, scaler, future_days=7):
    predicted_prices = []
    current_input = last_days
    for _ in range(future_days):
        current_prediction = model.predict(current_input)
        predicted_price = scaler.inverse_transform(current_prediction)[0][0]
        predicted_prices.append(predicted_price)
        current_input = np.append(current_input[:,1:,:], [[[current_prediction[0][0]]]], axis=1)
    return predicted_prices

def predictions():
    start_date = "2018-01-01"
    end_date = dt.datetime.now().strftime("%Y-%m-%d")
    prediction_days = 60
    future_days = 7

    data = fetch_data(start_date=start_date, end_date=end_date)
    if data.empty:
        print("No data fetched. Please check your dates and internet connection.")
        return []

    x_train, y_train, scaler = preprocess_data(data, prediction_days)
    if x_train.size == 0:
        print("Training data is empty. Adjust your prediction_days or data range.")
        return []

    model = build_model(input_shape=(x_train.shape[1], 1))
    model.fit(x_train, y_train, epochs=25, batch_size=32)

    last_days = data[-prediction_days:].values
    last_days_scaled = scaler.transform(last_days.reshape(-1, 1))
    last_days_scaled = np.reshape(last_days_scaled, (1, last_days_scaled.shape[0], 1))

    predicted_prices = predict_next_7_days(model, last_days_scaled, scaler, future_days)
    predicted_ranges = [get_price_range(price) for price in predicted_prices]

    return predicted_ranges

"""
DO NOT REMOVE
"""
preds = predictions()
assert len(preds) == 7
assert all([isinstance(val, ETHPriceRanges) for val in preds])
print(preds)
for i, pred in enumerate(preds, start=1):
    print(f"Day {i}: {pred.name if pred else 'Out of defined ranges'}")

