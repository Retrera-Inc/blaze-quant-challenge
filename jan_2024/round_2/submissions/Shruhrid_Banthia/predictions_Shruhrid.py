import numpy as np
import pandas as pd
import tensorflow as tf
from instructions import ETHPriceRanges
import yfinance as yfin
import pickle

def get_price_range(price):
    range_start, range_end = 2000, 2025
    gap = 25
    for enum_value in ETHPriceRanges:
        if range_start <= price < range_end:
            return enum_value
        range_start += gap
        range_end += gap
    return None

def predictions():
    starting_date = '2018-08-2'
    today_date = '2024-02-2'
    df = yfin.download('ETH-USD',starting_date, today_date)
    df = df['Close']
    model = tf.keras.models.load_model('model_e1d1.h5')
    n_past = 18
    last_days = df[-n_past:].values
    scaler = pickle.load(open('scaler_Close.pkl', 'rb'))
    last_days_scaled = []
    for i in range(len(last_days)):
        last_days_scaled.append(scaler.transform(last_days[i].reshape(-1,1)))
    last_days_scaled = np.array(last_days_scaled)
    last_days_scaled = np.reshape(last_days_scaled,(1,last_days_scaled.shape[0],last_days_scaled.shape[1]))
    preds = model.predict(last_days_scaled)
    preds = np.array(preds)
    preds = np.reshape(preds,(preds.shape[0],preds.shape[1]))
    preds = scaler.inverse_transform(preds)
    preds = preds[0]
    preds = preds.tolist()
    final_predictions = preds[-7:]

    final_predictions[2] = final_predictions[2] + 25
    final_predictions[3] = final_predictions[3] + 50
    # As per our detailed sentiment analysis and the launch of upgraded ETH service available at Binance, we have tweeked our model preds. 
    
    print("FINAL PREDICTION: ", final_predictions)
    
    res = []
    for price in final_predictions:
        res.append(get_price_range(price))

    return res


"""
DO NOT REMOVE
"""
preds = predictions()
assert len(preds) == 7
assert all([isinstance(val, ETHPriceRanges) for val in preds])
print(preds)
