# Importing libraries
from instructions import ETHPriceRanges, ARBPriceRanges, LINKPriceRanges
import numpy as np
import tensorflow as tf
from keras.models import Model, Sequential
from keras.layers import Input, LSTM, Dense, Attention
from keras.optimizers import Adam
from keras import layers
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import datetime
import yfinance as yf
import pytz
from statsmodels.tsa.arima.model import ARIMA

# Some useful functions
def str_to_date(str_date):
    split1 = str_date.split(' ')
    split2 = split1[0].split('-')
    year, month, day = int(split2[0]), int(split2[1]), int(split2[2])
    return datetime.datetime(year=year, month=month, day=day)

def dataframe_to_windowed_df(dataframe, first_date_str, last_date_str, n=3):
    first_date = str_to_date(first_date_str)
    last_date = str_to_date(last_date_str)
    target_date = first_date
    dates = []
    X, Y = [], []

    last_time = False
    while True:
        df_subset = dataframe.loc[:target_date].tail(n+1)
        
        if len(df_subset) != n+1:
            return

        values = df_subset['Price'].to_numpy()
        x, y = values[:-1], values[-1]

        dates.append(target_date)
        X.append(x)
        Y.append(y)

        next_week = dataframe.loc[target_date:target_date+datetime.timedelta(days=7)]
        next_datetime_str = str(next_week.head(2).tail(1).index.values[0])
        next_date_str = next_datetime_str.split('T')[0]
        year_month_day = next_date_str.split('-')
        year, month, day = year_month_day
        next_date = datetime.datetime(day=int(day), month=int(month), year=int(year))
        
        if last_time:
            break
        
        target_date = next_date

        if target_date == last_date:
            last_time = True
        
    ret_df = pd.DataFrame({})
    ret_df['Target Date'] = dates
    
    X = np.array(X)
    for i in range(0, n):
        X[:, i]
        ret_df[f'Target-{n-i}'] = X[:, i]
    
    ret_df['Target'] = Y

    return ret_df

def windowed_df_to_date_X_y(windowed_dataframe):
    df_as_np = windowed_dataframe.to_numpy()
    
    dates = df_as_np[:, 0]
    middle_matrix = df_as_np[:, 1:-1]
    X = middle_matrix.reshape((len(dates), middle_matrix.shape[1], 1))
    Y = df_as_np[:, -1]

    return dates, X.astype(np.float32), Y.astype(np.float32) 

def create_custom_model():
    inputs = Input(shape=(X_train.shape[1], X_train.shape[2]))
    lstm = LSTM(64, return_sequences=True)(inputs)
    attention = Attention()([lstm, lstm])
    output = Dense(1)(attention)
    
    model = Model(inputs=inputs, outputs=output)
    return model

# Handling the prediction range of Ethereum
def find_custom_price_range_ETH(array):
    jump = 25
    arr = []
    for price in array:
        start, end = 2000, 2025
        for enum_value in ETHPriceRanges:
            if start <= price < end:
                arr.append(enum_value)
                break
            start += jump
            end += jump
        else:
            arr.append(None)
    return arr

# Handling the prediction range of Arbitrum
def find_custom_price_range_ARB(array):
    jump = 0.05
    arr = []
    for price in array:
        start, end = 1.35, 2.20
        for enum_value in ARBPriceRanges:
            if start <= price < end:
                arr.append(enum_value)
                break
            start += jump
            end += jump
        else:
            arr.append(None)
    return arr

# Handling the prediction range of Chainlink
def find_custom_price_range_LINK(array):
    jump = 0.25
    arr = []
    for price in array:
        start, end = 18, 18.25
        for enum_value in LINKPriceRanges:
            if start <= price < end:
                arr.append(enum_value)
                break
            start += jump
            end += jump
        else:
            arr.append(None)
    return arr


def make_custom_predictions_ETH_with_arima():
    array = []
    while len(array) < 7:
        today_date = datetime.date.today()
        us_eastern = pytz.timezone('US/Eastern')
        today_date = datetime.datetime(today_date.year, today_date.month, today_date.day, tzinfo=pytz.utc).astimezone(us_eastern).date()
        today_data = yf.download('ETH-USD', start='2024-03-15', end=today_date)
        today_data.drop(columns=['Open', 'High', 'Low', 'Adj Close', 'Volume'], inplace=True)
        today_data.rename(columns={"Close":"Price"}, inplace=True)
        if (len(array) > 0):
            addional_date = today_date + datetime.timedelta(days=len(array)-1)
            additional_data = pd.DataFrame({"Price": array[-1]}, index=[pd.to_datetime(addional_date)])
            today_data = pd.concat([today_data, additional_data])
        
        df = pd.read_csv('./ethereumData.csv')
        df = df.iloc[::-1]
        df["Date"] = df["Date"].astype(str)
        df["Date"] = df['Date'].apply(str_to_date)
        df1 = df.drop(columns=["Volume","Market_cap"])
        df3 = df1
        df3.index = df3.pop('Date')
        df4 = pd.concat([df3, today_data])      
        today = today_date - datetime.timedelta(days = 1)
        today = today.strftime("%Y-%m-%d")
        
        windowed_df = dataframe_to_windowed_df(df4,  '2018-08-11', today, n=3)
        dates, X, y = windowed_df_to_date_X_y(windowed_df)
        q_80 = int(len(dates) * .89)
        q_90 = int(len(dates) * 1)
        dates_train, X_train, y_train = dates[:q_80], X[:q_80], y[:q_80]
        dates_val, X_val, y_val = dates[q_80:q_90-1], X[q_80:q_90-1], y[q_80:q_90-1]
        dates_test, X_test, y_test = dates[-1:], X[-1:], y[-1:]
        
        model = Sequential([layers.Input((3, 1)),
                            layers.LSTM(64),
                            layers.Dense(32, activation='relu'),
                            layers.Dense(32, activation='relu'),
                            layers.Dense(1)])
        model.compile(loss='mse', 
                      optimizer=Adam(learning_rate=0.001),
                      metrics=['mean_absolute_error'])
        model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=25)
        test_predictions_lstm = model.predict(X_test).flatten()
        
        arima_model = ARIMA(df4['Price'], order=(5,1,0))  # Adjust ARIMA order as needed
        arima_model_fit = arima_model.fit()
        test_predictions_arima = arima_model_fit.forecast(steps=1)
        
        combined_prediction = (test_predictions_lstm[0] + test_predictions_arima[0]) / 2
        array.append(combined_prediction)
        
    return find_custom_price_range_ETH(array)

def make_custom_predictions_ARB_with_arima():
    array = []
    while len(array) < 7:
        today_date = datetime.date.today()
        us_eastern = pytz.timezone('US/Eastern')
        today_date = datetime.datetime(today_date.year, today_date.month, today_date.day, tzinfo=pytz.utc).astimezone(us_eastern).date()
        today_data = yf.download('ARB11841-USD', start='2024-03-29', end=today_date)
        today_data.drop(columns=['Open', 'High', 'Low', 'Adj Close', 'Volume'], inplace=True)
        today_data.rename(columns={"Close":"Price"}, inplace=True)
        if (len(array) > 0):
            addional_date = today_date + datetime.timedelta(days=len(array)-1)
            additional_data = pd.DataFrame({"Price": array[-1]}, index=[pd.to_datetime(addional_date)])
            today_data = pd.concat([today_data, additional_data])
        
        df = pd.read_csv('arbitrumData.csv')
        df2 = pd.read_csv('dataset.csv')
        coin_data = df2[df2['crypto_name']=='Dogecoin' ]
        coin_data.index = pd.Series(np.arange(coin_data["date"].size) + 1)
        coin_data = coin_data.iloc[:1717]
        coin_data = coin_data[["date","close"]]
        coin_data["close"] = coin_data["close"].multiply(1000)
        new_column_names = {'date': 'Date', 'close': 'Price'}
        coin_data.rename(columns=new_column_names, inplace=True)
        df = df.iloc[::-1]
        df["Date"] = df["Date"].astype(str)
        df["Date"] = df['Date'].apply(str_to_date)
        df1 = df.drop(columns=["Volume","Market_cap"])
        end_date_df1 = pd.to_datetime('2018-08-27')  
        desired_end_date = pd.to_datetime('2023-03-22')
        delta = desired_end_date - end_date_df1
        coin_data['Date'] = pd.to_datetime(coin_data['Date']) + delta
        df3 = pd.concat([coin_data, df1])
        df3.index = df3.pop('Date')
        df3 = pd.concat([df3, today_data])      
        today = today_date - datetime.timedelta(days = 1)
        today = today.strftime("%Y-%m-%d")
        windowed_df = dataframe_to_windowed_df(df3,  '2018-09-28', today, n=3)
        dates, X, y = windowed_df_to_date_X_y(windowed_df)
        q_80 = int(len(dates) * .89)
        q_90 = int(len(dates) * 1)
        dates_train, X_train, y_train = dates[:q_80], X[:q_80], y[:q_80]
        dates_val, X_val, y_val = dates[q_80:q_90-1], X[q_80:q_90-1], y[q_80:q_90-1]
        dates_test, X_test, y_test = dates[-1:], X[-1:], y[-1:]
        
        model = Sequential([layers.Input((3, 1)),
                            layers.LSTM(64),
                            layers.Dense(32, activation='relu'),
                            layers.Dense(32, activation='relu'),
                            layers.Dense(1)])
        model.compile(loss='mse', 
                      optimizer=Adam(learning_rate=0.001),
                      metrics=['mean_absolute_error'])
        model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10)
        test_predictions_lstm = model.predict(X_test).flatten()
        
        arima_model = ARIMA(df3['Price'], order=(5,1,0))  # Adjust ARIMA order as needed
        arima_model_fit = arima_model.fit()
        test_predictions_arima = arima_model_fit.forecast(steps=1)
        
        combined_prediction = (test_predictions_lstm[0] + test_predictions_arima[0]) / 2
        array.append(combined_prediction)
        
    return find_custom_price_range_ARB(array)

def make_custom_predictions_LINK_with_arima():
    array = []
    while len(array) < 7:
        today_date = datetime.date.today()
        us_eastern = pytz.timezone('US/Eastern')
        today_date = datetime.datetime(today_date.year, today_date.month, today_date.day, tzinfo=pytz.utc).astimezone(us_eastern).date()
        today_data = yf.download('LINK-USD', start='2024-03-15', end=today_date)
        today_data.drop(columns=['Open', 'High', 'Low', 'Adj Close', 'Volume'], inplace=True)
        today_data.rename(columns={"Close":"Price"}, inplace=True)
        if (len(array) > 0):
            addional_date = today_date + datetime.timedelta(days=len(array)-1)
            additional_data = pd.DataFrame({"Price": array[-1]}, index=[pd.to_datetime(addional_date)])
            today_data = pd.concat([today_data, additional_data])
        
        df = pd.read_csv('./chainlinkData.csv')
        df = df.iloc[::-1]
        df["Date"] = df["Date"].astype(str)
        df["Date"] = df['Date'].apply(str_to_date)
        df1 = df.drop(columns=["Volume","Market_cap"])
        df3 = df1
        df3.index = df3.pop('Date')
        df4 = pd.concat([df3, today_data])      
        today = today_date - datetime.timedelta(days = 1)
        today = today.strftime("%Y-%m-%d")
        windowed_df = dataframe_to_windowed_df(df4,  '2017-09-25', today, n=3)
        dates, X, y = windowed_df_to_date_X_y(windowed_df)
        q_80 = int(len(dates) * .89)
        q_90 = int(len(dates) * 1)
        dates_train, X_train, y_train = dates[:q_80], X[:q_80], y[:q_80]
        dates_val, X_val, y_val = dates[q_80:q_90-1], X[q_80:q_90-1], y[q_80:q_90-1]
        dates_test, X_test, y_test = dates[-1:], X[-1:], y[-1:]
        
        model = Sequential([layers.Input((3, 1)),
                            layers.LSTM(64),
                            layers.Dense(32, activation='relu'),
                            layers.Dense(32, activation='relu'),
                            layers.Dense(1)])
        model.compile(loss='mse', 
                      optimizer=Adam(learning_rate=0.001),
                      metrics=['mean_absolute_error'])
        model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10)
        test_predictions_lstm = model.predict(X_test).flatten()
        
        arima_model = ARIMA(df4['Price'], order=(5,1,0))  # Adjust ARIMA order as needed
        arima_model_fit = arima_model.fit()
        test_predictions_arima = arima_model_fit.forecast(steps=1)
        
        combined_prediction = (test_predictions_lstm[0] + test_predictions_arima[0]) / 2
        array.append(combined_prediction)
        
    return find_custom_price_range_LINK(array)



# Print custom results
def print_custom_results():
    print("Predicted Ethereum Price Ranges: ", make_custom_predictions_ETH_with_arima())
    print("Predicted Arbitrum Price Ranges: ", make_custom_predictions_ARB_with_arima())
    print("Predicted Chainlink Price Ranges: ", make_custom_predictions_LINK_with_arima())
    # Add calls to similar functions for Arbitrum and Chainlink predictions here

print_custom_results()
