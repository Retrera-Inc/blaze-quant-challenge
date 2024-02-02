from instructions import ETHPriceRanges
import numpy as np
import pandas as pd
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

# Load the LSTM model
model = load_model("model.h5")

def convert_to_eth_price_ranges(predictions):
    converted_predictions = []

    for prediction in predictions:
        for eth_range in ETHPriceRanges:
            lower_bound, upper_bound = map(int, eth_range.name.split('_')[1:])
            if lower_bound <= prediction < upper_bound:
                converted_predictions.append(eth_range)
                break

    return converted_predictions

def make_prediction(model, scaled_data, scaler_y):
    look_back = 5
    upcoming_days_prediction = scaled_data[-look_back:]
    feb_4_to_feb_10_forecasting = []

    for i in range(7):
        predicted_price = model.predict(upcoming_days_prediction.reshape(1, look_back, scaled_data.shape[1]))
        predicted_price = scaler_y.inverse_transform(predicted_price)
        feb_4_to_feb_10_forecasting.append(predicted_price[0, 0])

        # Update the upcoming_days_prediction for the next iteration
        upcoming_days_prediction = np.concatenate((upcoming_days_prediction[1:], predicted_price.reshape(1, -1)), axis=0)

    return feb_4_to_feb_10_forecasting

def predictions():
    data = pd.read_csv('eth.csv')
    y = data['Price']
    features = ['Adj Close', 'upper_shadow', 'lower_shadow', 'open2close', 'high2low', 'high2mean', 'low2mean',
                'high2median', 'low2median', 'Price', 'Market_cap', 'Supply', 'BlockSize', 'BlockDifficulty',
                'Hash_count', 'Growth Value']

    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data[features])
    scaler_y = MinMaxScaler()
    y_scaled = scaler_y.fit_transform(y.values.reshape(-1, 1))

    feb_4_to_feb_10_forecasting = make_prediction(model, scaled_data, scaler_y)
    final_prediction = convert_to_eth_price_ranges(feb_4_to_feb_10_forecasting)

    return final_prediction

preds = predictions()
print(preds)
assert len(preds) == 7
assert all(isinstance(val, ETHPriceRanges) for val in preds)