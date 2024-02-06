import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Bidirectional, Dense, Dropout, Activation
import requests
from instructions import ETHPriceRanges

# This model predicts the prices using Bidirectional LSTM and the trading data includes closing price of ETH and BTC for the past month
def predictions():
# Fetch data
    request = requests.get('https://min-api.cryptocompare.com/data/v2/histohour?fsym=ETH&tsym=USD&limit=65&aggregate=1')
    eth_json = request.json()['Data']['Data']
    # print(eth_json)

    df = pd.json_normalize(eth_json)
    # print(df.shape)

    request = requests.get('https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USD&limit=65&aggregate=1')
    btc_json = request.json()['Data']['Data']
    # print(btc_json)

    df_bitcoin = pd.json_normalize(btc_json)
    # print(df_bitcoin.shape)

    # processing
    ethereum_prices = df[['time', 'close','high','low', 'open']]
    bitcoin_prices = df_bitcoin[['time', 'close']]
    # print(ethereum_prices.shape, bitcoin_prices.shape)

    # fetch old data
    df_old = pd.read_csv("train_data.csv")

    # Merge ethereum and bitcoin on 'Date' column
    merged_data = pd.merge(ethereum_prices, bitcoin_prices, on='time', suffixes=('_ETH', '_BTC'))
    # concatenate two datasets
    merged_data = pd.concat([df_old,merged_data]).drop_duplicates().reset_index(drop=True)
    # print(merged_data.shape)

    # Normalize data between 0 and 1
    scaler = MinMaxScaler(feature_range=(0, 1))
    # scaled_data = scaler.fit_transform(merged_data[['close_ETH','high', 'low', 'open','close_BTC']])
    scaled_data = scaler.fit_transform(merged_data[['close_ETH','close_BTC']])
    # print(scaled_data.shape)

    # Prepare data for training
    n_feat_eth = 1
    X_eth, X_btc, y = [], [], []
    look_back = 24  # Number of previous days to use for prediction

    for i in range(len(scaled_data) - look_back - 168):
        X_eth.append(scaled_data[i:i+look_back, 0:n_feat_eth])  # Feature 1: Ethereum
        X_btc.append(scaled_data[i:i+look_back, 1])  # Feature 2: Bitcoin
        y.append(scaled_data[i+look_back:i+look_back+168,0])
    X_eth, X_btc, y = np.array(X_eth), np.array(X_btc), np.array(y)
    # print(X_eth.shape, X_btc.shape, y.shape)

    # Reshape input data to be 3D (samples, timesteps, features)
    X_eth = np.reshape(X_eth, (X_eth.shape[0], X_eth.shape[1], n_feat_eth))  # 1 feature for Ethereum
    X_btc = np.reshape(X_btc, (X_btc.shape[0], X_btc.shape[1], 1))  # 1 feature for Bitcoin
    # print(X_eth.shape, X_btc.shape)

    # combining ETH and BTC input
    combined_input = np.concatenate([X_eth, X_btc], axis=-1)

    # Build the Bi-LSTM model
    model = Sequential()
    model.add(Bidirectional(LSTM(units=24, return_sequences=True, input_shape=(combined_input[1], combined_input[2]))))
    model.add(Dropout(0.2))

    model.add(Bidirectional(LSTM(units=48, return_sequences=True)))
    model.add(Dropout(0.2))

    model.add(Bidirectional(LSTM(24)))
    model.add(Dense(units=168))  # predicts for next 168 hours
    model.add(Activation('linear'))
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train the model
    model.fit(combined_input, y, epochs=50, batch_size=32, verbose=1)

    # Make predictions for the next 7 days
    last_window = scaled_data[-look_back:]
    last_window = np.array(last_window)
    #(X_eth, (X_eth.shape[0], X_eth.shape[1], 1)
    # print(last_window.shape)
    last_window = np.reshape(last_window, (1, look_back, n_feat_eth+1))

    predicted_prices_scaled = model.predict(last_window)
    print(predicted_prices_scaled.ndim) # this output is (1,7)
    # Inverse transform the predicted prices to get actual prices
    predicted_prices = scaler.inverse_transform((np.repeat(predicted_prices_scaled.reshape(-1,1), n_feat_eth+1, axis=1)))
    predicted_prices_7days = predicted_prices[::24,0]
    # print("Predicted Prices for the Next 7 Days:")
    # print(predicted_prices_7days)

    result = []
    for val in predicted_prices_7days: 
        if val >= 2000 and val < 2025 : result.append(ETHPriceRanges.pr_2000_2025)
        elif val >= 2025 and val < 2050 : result.append(ETHPriceRanges.pr_2025_2050)
        elif val >= 2050 and val < 2075 : result.append(ETHPriceRanges.pr_2050_2075)
        elif val >= 2075 and val < 2100 : result.append(ETHPriceRanges.pr_2075_2100)
        elif val >= 2100 and val < 2125 : result.append(ETHPriceRanges.pr_2100_2125)
        elif val >= 2125 and val < 2150 : result.append(ETHPriceRanges.pr_2125_2150)
        elif val >= 2150 and val < 2175 : result.append(ETHPriceRanges.pr_2150_2175)
        elif val >= 2175 and val < 2200 : result.append(ETHPriceRanges.pr_2175_2200)
        elif val >= 2200 and val < 2225 : result.append(ETHPriceRanges.pr_2200_2225)
        elif val >= 2225 and val < 2250 : result.append(ETHPriceRanges.pr_2225_2250)
        elif val >= 2250 and val < 2275 : result.append(ETHPriceRanges.pr_2250_2275)
        elif val >= 2275 and val < 2300 : result.append(ETHPriceRanges.pr_2275_2300)
        elif val >= 2300 and val < 2325 : result.append(ETHPriceRanges.pr_2300_2325)
        elif val >= 2325 and val < 2350 : result.append(ETHPriceRanges.pr_2325_2350)
        elif val >= 2350 and val < 2375 : result.append(ETHPriceRanges.pr_2350_2375)
        elif val >= 2375 and val < 2400 : result.append(ETHPriceRanges.pr_2375_2400)
        elif val >= 2400 and val < 2425 : result.append(ETHPriceRanges.pr_2400_2425)
        elif val >= 2425 and val < 2450 : result.append(ETHPriceRanges.pr_2425_2450)
        elif val >= 2450 and val < 2475 : result.append(ETHPriceRanges.pr_2450_2475)
        elif val >= 2475 and val < 2500 : result.append(ETHPriceRanges.pr_2475_2500)
        elif val >= 2500 and val < 2525 : result.append(ETHPriceRanges.pr_2500_2525)
        elif val >= 2525 and val < 2550 : result.append(ETHPriceRanges.pr_2525_2550)
        elif val >= 2550 and val < 2575 : result.append(ETHPriceRanges.pr_2550_2575)
        elif val >= 2575 and val < 2600 : result.append(ETHPriceRanges.pr_2575_2600)
        else : result.append(ETHPriceRanges.pr_2600_2625)

    return(result)

"""
DO NOT REMOVE
"""
preds = predictions()
assert len(preds) == 7
assert all([isinstance(val, ETHPriceRanges) for val in preds])
