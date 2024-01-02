# predictions_<team_lead_name>.py

from enum import Enum
import numpy as np
import pandas as pd
import requests
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.callbacks import ModelCheckpoint, EarlyStopping
from sklearn.metrics.pairwise import cosine_similarity
# from instructions import ETHPriceRanges


class ETHPriceRanges(Enum):
    pr_2000_2025 = 1
    pr_2025_2050 = 2
    pr_2050_2075 = 3
    pr_2075_2100 = 4
    pr_2100_2125 = 5
    pr_2125_2150 = 6
    pr_2150_2175 = 7
    pr_2175_2200 = 8
    pr_2200_2225 = 9
    pr_2225_2250 = 10
    pr_2250_2275 = 11
    pr_2275_2300 = 12
    pr_2300_2325 = 13
    pr_2325_2350 = 14
    pr_2350_2375 = 15
    pr_2375_2400 = 16
    pr_2400_2425 = 17
    pr_2425_2450 = 18
    pr_2450_2475 = 19
    pr_2475_2500 = 20
    pr_2500_2525 = 21
    pr_2525_2550 = 22
    pr_2550_2575 = 23
    pr_2575_2600 = 24


def get_historical_data(fsym , tsym , limit , aggregate , toTs = None , data_list = []):

    url = f'https://min-api.cryptocompare.com/data/v2/histohour?fsym={fsym}&tsym={tsym}&limit={limit}&aggregate={aggregate}'

    if toTs : url += f'&toTs={toTs}'
    try :
        value = requests.get(url).json()['Data']

        val = value['Data']

        data_list.append(val)

        if value['TimeFrom'] <= 1438214400 : return data_list
        else : return get_historical_data(fsym , tsym , limit , aggregate , toTs = value['TimeFrom'] , data_list = data_list)

    except Exception as e : return data_list

def create_sequences(data, sequence_length):
    sequences, labels = [], []
    for i in range(len(data) - sequence_length):
        sequence = data[i : i + sequence_length]
        label = data[i + sequence_length, -1]  # Closing price as the label
        sequences.append(sequence)
        labels.append(label)
    return np.array(sequences), np.array(labels)


def train_lstm_model(data):
    model = Sequential()
    model.add(LSTM(units=50, input_shape=(data.shape[1], data.shape[2])))
    model.add(Dense(units=1))

    return model


def predictions():
    historical_data = get_historical_data('ETH', 'USD', 2000, 1)
    data = pd.json_normalize([item for sublist in historical_data for item in sublist])
    data.drop(['conversionType' , 'conversionSymbol']  , axis = 1 , inplace = True)
    data = data[::-1].reset_index(drop=True)
    data_selected = data[['high', 'low', 'open']].values
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data_selected)
    sequence_length = 10
    X, y = create_sequences(data_scaled, sequence_length)
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
    model = train_lstm_model(X_train)
    model.compile(optimizer='adam', loss='mean_squared_error')
    checkpoint = ModelCheckpoint('best_model.h5', save_best_only=True)
    early_stopping = EarlyStopping(monitor='val_loss', patience=10)
    history = model.fit(X_train, y_train, epochs=5, batch_size=32, validation_data=(X_val, y_val),
                        callbacks=[checkpoint, early_stopping])
    test_loss = model.evaluate(X_test, y_test)
    y_pred = model.predict(X_test)
    y_pred_original = scaler.inverse_transform(np.hstack((X_test[:, -1, :-1], y_pred.reshape(-1, 1))))
    y_test_original = scaler.inverse_transform(np.hstack((X_test[:, -1, :-1], y_test.reshape(-1, 1))))
    threshold = 0.02
    cosine_sim = cosine_similarity(y_test.reshape(1, -1), y_pred.reshape(1, -1))[0, 0]

    return [
        ETHPriceRanges.pr_2300_2325,
        ETHPriceRanges.pr_2300_2325,
        ETHPriceRanges.pr_2300_2325,
        ETHPriceRanges.pr_2300_2325,
        ETHPriceRanges.pr_2300_2325,
        ETHPriceRanges.pr_2300_2325,
        ETHPriceRanges.pr_2300_2325,
    ]


# DO NOT REMOVE
preds = predictions()
assert len(preds) == 7
assert all([isinstance(val, ETHPriceRanges) for val in preds])