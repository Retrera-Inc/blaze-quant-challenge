"""
Copy this file and add your business logic for the predictions. Add your file in
the format: predictions_<team_lead_name>.py
"""

from instructions import ETHPriceRanges, ARBPriceRanges, LINKPriceRanges

# Impoerting libraries
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

# Some useful functions
def str_to_datetime(str):
    split1=str.split(' ')
    split2=split1[0].split('-')
    year,month,day=int(split2[0]),int(split2[1]),int(split2[2])
    return datetime.datetime(year=year,month=month,day=day)

def df_to_windowed_df(dataframe, first_date_str, last_date_str, n=3):
#   print(first_date)
  first_date = str_to_datetime(first_date_str)
  last_date  = str_to_datetime(last_date_str)
#   print(first_date)

  target_date = first_date
#   target_date = np.datetime64(target_date)
  dates = []
  X, Y = [], []

  last_time = False
  while True:
    df_subset = dataframe.loc[:target_date].tail(n+1)
    
    if len(df_subset) != n+1:
      print(f'Error: Window of size {n} is too large for date {target_date}')
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

  return dates, X.astype(np.float32),Y.astype(np.float32) 

def create_model():
    inputs = Input(shape=(X_train.shape[1], X_train.shape[2]))
    lstm = LSTM(64, return_sequences=True)(inputs)
    attention = Attention()([lstm, lstm])
    output = Dense(1)(attention)
    
    model = Model(inputs=inputs, outputs=output)
    return model

# Handling the prediction range of Ethereum
def find_price_range_ETH(price):
    start, end = 2000, 2025
    jump = 25
    for enum_value in ETHPriceRanges:
        if start <= price < end:
            return enum_value
        start += jump
        end += jump
    return None

# Handling the prediction range of Arbitrum
def find_price_range_ARB(price):
    start, end = 1.8, 1.85
    jump = 0.05
    for enum_value in ARBPriceRanges:
        if start <= price < end:
            return enum_value
        start += jump
        end += jump
    return None

# Handling the prediction range of Chainlink
def find_price_range_LINK(price):
    start, end = 18, 18.25
    jump = 0.25
    for enum_value in LINKPriceRanges:
        if start <= price < end:
            return enum_value
        start += jump
        end += jump
    return None



   


def predictions_ETH():
    # Fetching today's data from yfinance
    today_date = datetime.date.today()
    today_data = yf.download('ETH-USD', start='2024-03-15', end=today_date)
    today_data.drop(columns=['Open', 'High', 'Low', 'Adj Close', 'Volume'], inplace=True)
    today_data.rename(columns={"Close":"Price"}, inplace=True)
    # print(today_data)
    

    # Load the Ethereum data and prearing it
    df=pd.read_csv('./ethereumData.csv')
    # df['Price']=pd.to_numeric(df['Price'])
    df=df.iloc[::-1]
    # print(today_data.index.dtype)
    df["Date"]=df["Date"].astype(str)
    df["Date"] = df['Date'].apply(str_to_datetime)
    # df.index=df.pop('Date')
    # print(df.head())
    df1=df.drop(columns=["Volume","Market_cap"])
    # print(df1)
    df3 = df1
    df3.index=df3.pop('Date')
    # print(df3)

    df4 = pd.concat([df3, today_data])      # Concatenating today's data with the historical data
    # print("The data is\n", df4)

    # Start day second time around: '2021-03-25'
    today = datetime.date.today() - datetime.timedelta(days = 1)
    today = today.strftime("%Y-%m-%d")
    # print(today)
    # print(type(today))
    windowed_df = df_to_windowed_df(df4,  '2016-08-11', 
                                    today, 
                                    n=3)
    # windowed_df

    dates, X, y = windowed_df_to_date_X_y(windowed_df)
    # print(dates.shape,X.shape," ",y.shape)

    q_80 = int(len(dates) * .89)
    q_90 = int(len(dates) * 1)

    dates_train, X_train, y_train = dates[:q_80], X[:q_80], y[:q_80]

    dates_val, X_val, y_val = dates[q_80:q_90-1], X[q_80:q_90-1], y[q_80:q_90-1]
    dates_test, X_test, y_test = dates[-1:], X[-1:], y[-1:]

    # plt.plot(dates_train, y_train)
    # plt.plot(dates_val, y_val)
    # plt.plot(dates_test, y_test)

    # plt.legend(['Train', 'Validation', 'Test'])

    # Building the model
    model = Sequential([layers.Input((3, 1)),
                        layers.LSTM(64),
                        layers.Dense(32, activation='relu'),
                        layers.Dense(32, activation='relu'),
                        layers.Dense(1)])

    model.compile(loss='mse', 
                optimizer=Adam(learning_rate=0.001),
                metrics=['mean_absolute_error'])

    model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10)

    test_predictions = model.predict(X_test).flatten()
    print(test_predictions)

    return find_price_range_ETH(test_predictions[0])


def predictions_ARB():
    # Fetching today's data from yfinance
    today_date = datetime.date.today()
    today_data = yf.download('ETH-USD', start='2024-03-15', end=today_date)
    today_data.drop(columns=['Open', 'High', 'Low', 'Adj Close', 'Volume'], inplace=True)
    today_data.rename(columns={"Close":"Price"}, inplace=True)
    # print(today_data)



    # Load the Ethereum data and prearing it
    df=pd.read_csv('arbitrumData.csv')
    df2=pd.read_csv('dataset.csv')
    coin_data=df2[df2['crypto_name']=='Dogecoin' ]
    coin_data.index = pd.Series(np.arange(coin_data["date"].size) + 1)
    coin_data=coin_data.iloc[:1717]
    coin_data=coin_data[["date","close"]]
    coin_data["close"]=coin_data["close"].multiply(1000)
    new_column_names = {'date': 'Date', 'close': 'Price'}
    coin_data.rename(columns=new_column_names, inplace=True)
    df=df.iloc[::-1]
    df["Date"]=df["Date"].astype(str)
    df["Date"] = df['Date'].apply(str_to_datetime)
    df1=df.drop(columns=["Volume","Market_cap"])
    end_date_df1 = pd.to_datetime('2018-08-27')  
    desired_end_date = pd.to_datetime('2023-03-22')
    delta = desired_end_date - end_date_df1
    coin_data['Date'] = pd.to_datetime(coin_data['Date']) + delta
    df3= pd.concat([coin_data, df1])
    df3.index=df3.pop('Date')
    df3 = pd.concat([df3, today_data])      # Concatenating today's data with the historical data

    # Start day second time around: '2021-03-25'
    today = datetime.date.today() - datetime.timedelta(days = 1)
    today = today.strftime("%Y-%m-%d")
    # print(today)
    # print(type(today))
    windowed_df = df_to_windowed_df(df3,  '2018-09-28', 
                                    today, 
                                    n=3)
    # print("Here", windowed_df)

    dates, X, y = windowed_df_to_date_X_y(windowed_df)
    # print(dates.shape,X.shape," ",y.shape)

    q_80 = int(len(dates) * .89)
    q_90 = int(len(dates) * 1)

    dates_train, X_train, y_train = dates[:q_80], X[:q_80], y[:q_80]

    dates_val, X_val, y_val = dates[q_80:q_90-1], X[q_80:q_90-1], y[q_80:q_90-1]
    dates_test, X_test, y_test = dates[-1:], X[-1:], y[-1:]

    # plt.plot(dates_train, y_train)
    # plt.plot(dates_val, y_val)
    # plt.plot(dates_test, y_test)

    # plt.legend(['Train', 'Validation', 'Test'])

    # Building the model
    model = Sequential([layers.Input((3, 1)),
                        layers.LSTM(64),
                        layers.Dense(32, activation='relu'),
                        layers.Dense(32, activation='relu'),
                        layers.Dense(1)])

    model.compile(loss='mse', 
                optimizer=Adam(learning_rate=0.001),
                metrics=['mean_absolute_error'])

    model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10)

    test_predictions = model.predict(X_test).flatten()
    print(test_predictions)

    return find_price_range_ARB(test_predictions[0])


def predictions_LINK():
    # Fetching today's data from yfinance
    today_date = datetime.date.today()
    today_data = yf.download('LINK-USD', start='2024-03-15', end=today_date)
    today_data.drop(columns=['Open', 'High', 'Low', 'Adj Close', 'Volume'], inplace=True)
    today_data.rename(columns={"Close":"Price"}, inplace=True)
    # print(today_data)
    

    # Load the Ethereum data and prearing it
    df=pd.read_csv('./chainlinkData.csv')
    # df['Price']=pd.to_numeric(df['Price'])
    df=df.iloc[::-1]
    # print(today_data.index.dtype)
    df["Date"]=df["Date"].astype(str)
    df["Date"] = df['Date'].apply(str_to_datetime)
    # df.index=df.pop('Date')
    # print(df.head())
    df1=df.drop(columns=["Volume","Market_cap"])
    # print(df1)
    df3 = df1
    df3.index=df3.pop('Date')
    # print(df3)

    df4 = pd.concat([df3, today_data])      # Concatenating today's data with the historical data
    # print("The data is\n", df4)

    # Start day second time around: '2021-03-25'
    today = datetime.date.today() - datetime.timedelta(days = 1)
    today = today.strftime("%Y-%m-%d")
    # print(today)
    # print(type(today))
    windowed_df = df_to_windowed_df(df4,  '2017-09-25', 
                                    today, 
                                    n=3)
    # print(windowed_df)

    dates, X, y = windowed_df_to_date_X_y(windowed_df)
    # print(dates.shape,X.shape," ",y.shape)

    q_80 = int(len(dates) * .89)
    q_90 = int(len(dates) * 1)

    dates_train, X_train, y_train = dates[:q_80], X[:q_80], y[:q_80]

    dates_val, X_val, y_val = dates[q_80:q_90-1], X[q_80:q_90-1], y[q_80:q_90-1]
    dates_test, X_test, y_test = dates[-1:], X[-1:], y[-1:]

    # plt.plot(dates_train, y_train)
    # plt.plot(dates_val, y_val)
    # plt.plot(dates_test, y_test)

    # plt.legend(['Train', 'Validation', 'Test'])

    # Building the model
    model = Sequential([layers.Input((3, 1)),
                        layers.LSTM(64),
                        layers.Dense(32, activation='relu'),
                        layers.Dense(32, activation='relu'),
                        layers.Dense(1)])

    model.compile(loss='mse', 
                optimizer=Adam(learning_rate=0.001),
                metrics=['mean_absolute_error'])

    model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10)

    test_predictions = model.predict(X_test).flatten()
    print(test_predictions)

    return find_price_range_LINK(test_predictions[0])

print("The price of the Ethereum is = ", predictions_ETH())
print("The predictions of ARB are = ", predictions_ARB())
print("The price of the Chainlink is = ", predictions_LINK())


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