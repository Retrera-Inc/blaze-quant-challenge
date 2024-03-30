"""
Copy this file and add your business logic for the predictions. Add your file in
the format: predictions_<team_lead_name>.py
"""
import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense, Bidirectional
import datetime as dt
from instructions import ETHPriceRanges, ARBPriceRanges, LINKPriceRanges

def calculate_rsi(df, window=14):
    delta = df['Close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=window, min_periods=1).mean()
    avg_loss = loss.rolling(window=window, min_periods=1).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_sma(df, window=20):
    sma = df['Close'].rolling(window=window).mean()
    return sma

def get_data(crypto="ETH", prediction_days = 50):
    end_date="2024-03-30"
    data = yf.download(f"{crypto}-USD", start="2018-01-01", end=end_date)
    data['rsi'] = calculate_rsi(data)
    data['sma50'] = calculate_sma(data, window=50)
    data['sma10'] = calculate_sma(data, window=10)
    data['sma5'] = calculate_sma(data, window=5)
    data = data.dropna()
    data = data[['Open', 'High', 'Low', 'Volume','sma50','sma10','sma5','Close']]
    y = data['Close']
    scaler_y = MinMaxScaler(feature_range=(0, 1))
    scaled_data_y = scaler_y.fit_transform(y.values.reshape(-1, 1))
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data)
    x_train, y_train = [], []
    for x in range(prediction_days, len(scaled_data)-7):
        x_train.append(scaled_data[x-prediction_days:x, :])  
        y_train.append(scaled_data_y[x:x+7, -1])
    x_train, y_train = np.array(x_train), np.array(y_train)
    return x_train, y_train, scaler,scaler_y,data



def build_model(input_shape):
    model = Sequential()
    model.add(LSTM(units=50,return_sequences=True,input_shape=input_shape))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50,return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50,return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50))
    model.add(Dropout(0.2))
    model.add(Dense(units=7))
    model.compile(optimizer='adam',loss='mean_squared_error')

    return model

def get_price_range_ETH(price):
    for enum_value in ETHPriceRanges:
        range_start, range_end = map(int, enum_value.name.split('_')[1:3])
        if range_start <= price < range_end:
            return enum_value
    return None

def get_price_range_LINK(price):
    for enum_value in LINKPriceRanges:
        range_start, range_end = map(int, enum_value.name.split('_')[1:3])
        if range_start <= price < range_end:
            return enum_value
    return None

def get_price_range_ARB(price):
    for enum_value in ARBPriceRanges:
        range_start, range_end = map(int, enum_value.name.split('_')[1:3])
        if range_start <= price < range_end:
            return enum_value
    return None

def get_model(token="ETH"):
    start_date = "2018-01-01"
    end_date = "2024-03-30"
    prediction_days = 50
    future_days = 7
    x_train, y_train, scaler,scaler_y,data = get_data(token)
    model = build_model(input_shape=(x_train.shape[1], 8))
    model.fit(x_train, y_train, epochs=25, batch_size=32)
    return model,data.tail(50),scaler,scaler_y

def predict(token="ETH"):
    model,data,scaler,scaler_y = get_model(token)
    data = scaler.fit_transform(data)
    batch_data = np.expand_dims(data, axis=0)
    current_prediction = model.predict(batch_data)
    predicted_prices = scaler_y.inverse_transform(current_prediction[0].reshape(1, -1))
    print(predicted_prices[0])
    return predicted_prices
def predictions_ETH():
    """
    All of the business logic should go here. The output should be a list
    of size 7 with values from ETHPriceRanges
    
    """
    print("start")
    predicted_prices = predict("ETH")
    predicted_ranges = [get_price_range_ETH(min(max(3601,price),3980)) for price in predicted_prices[0]]
    return predicted_ranges


def predictions_ARB():
    """
    All of the business logic should go here. The output should be a list
    of size 7 with values from ARBPriceRanges
    """
    predicted_prices = predict("ARB11841")
    predicted_ranges = [get_price_range_ARB(min(max(181,price*0.85*100),216)) for price in predicted_prices[0]]
    return predicted_ranges    


def predictions_LINK():
    """
    All of the business logic should go here. The output should be a list
    of size 7 with values from LINKPriceRanges
    """
    predicted_prices = predict("LINK")
    predicted_ranges = [get_price_range_LINK(min(max(1801,price*0.45*100),2161)) for price in predicted_prices[0]]
    return predicted_ranges    


"""
DO NOT REMOVE
"""
preds_ETH = predictions_ETH()
assert len(preds_ETH) == 7
assert all([isinstance(val, ETHPriceRanges) for val in preds_ETH])

preds_ARB = predictions_ARB()
assert len(preds_ARB) == 7
assert all([isinstance(val, ARBPriceRanges) for val in preds_ARB])

preds_LINK = predictions_LINK()
assert len(preds_LINK) == 7
assert all([isinstance(val, LINKPriceRanges) for val in preds_LINK])
