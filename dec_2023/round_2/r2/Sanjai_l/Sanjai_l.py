from instructions import ETHPriceRanges
import numpy as np
import pandas as pd
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler


model = load_model("final_model.h5")


def convert_to_eth_price_ranges(predictions):
    converted_predictions = []

    for prediction in predictions:
        for eth_range in ETHPriceRanges:
            lower_bound, upper_bound = map(int, eth_range.name.split('_')[1:])
            if lower_bound <= prediction < upper_bound:
                converted_predictions.append(eth_range)
                break

    return converted_predictions


def create_dataset(dataset, look_back=5):
    dataX= []
    for i in range(len(dataset) - look_back):
        a = dataset[i:(i + look_back), :]
        dataX.append(a)

    return np.array(dataX)

def make_prediction():
    data=pd.read_csv('final-cleaned-data.csv')
    y=data['Price']
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data)
    scaler_y = MinMaxScaler()
    y_scaled = scaler_y.fit_transform(y.values.reshape(-1, 1))
    data_lookback = create_dataset(scaled_data, look_back=5)
    lookback_period = 7
    upcoming_7_days_prediction = data_lookback[- lookback_period:]
    jan_2_to_jan_8_forecasting = []

    for i in range(7):
        predicted_forecast_price_test_x = model.predict(upcoming_7_days_prediction[i:i + 1])

        predicted_forecast_price_test_x = scaler_y.inverse_transform(predicted_forecast_price_test_x)

        jan_2_to_jan_8_forecasting.append(predicted_forecast_price_test_x[0])



    final_prediction = [val[0] for val in jan_2_to_jan_8_forecasting]

    return final_prediction




def predictions():
    predictions=make_prediction()
    result=convert_to_eth_price_ranges(predictions)
    return result










preds = predictions()
assert len(preds) == 7
assert all([isinstance(val, ETHPriceRanges) for val in preds])
