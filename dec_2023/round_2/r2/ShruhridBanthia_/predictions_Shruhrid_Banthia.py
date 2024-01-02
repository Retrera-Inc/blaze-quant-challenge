import numpy as np
import pandas as pd
import tensorflow as tf
import yfinance as yfin
from statsmodels.tsa.arima.model import ARIMA
from prophet import Prophet
from instructions import ETHPriceRanges

data = pd.read_csv("eth_modified.csv")
data.rename(columns={"Close": "Price"}, inplace=True)
data = data.dropna()
regressors = ["Price", "High", "Low", "Vol", "Open"]


def predict_regressors(reg, end, prds):
    df = data.copy()
    df.rename(columns={"Date": "ds", reg: "y"}, inplace=True)

    prophet_model = Prophet(daily_seasonality=True, weekly_seasonality=True)
    for r in regressors:
        if r != reg:
            prophet_model.add_regressor(r)

    prophet_model.fit(df[:end])

    future_data = prophet_model.make_future_dataframe(
        periods=prds, include_history=False
    )
    for r in regressors:
        if r != reg:
            future_data[r] = df[r].iloc[-len(future_data) + end : end].values

    forecast_data = prophet_model.predict(future_data)
    future_table = forecast_data[["ds", "yhat"]].tail(15).copy()
    future_table.rename(columns={"ds": "Date", "yhat": reg}, inplace=True)
    # print(future_table)
    return forecast_data[["yhat"]].values


def get_price_range(price):
    range_start, range_end = 2000, 2025
    gap = 25
    for enum_value in ETHPriceRanges:
        if range_start <= price < range_end:
            return enum_value
        range_start += gap
        range_end += gap

    return None


def prophet_predictions():
    # start, stop = 8, -1
    price_forecast_list = []
    for i in range(1):
        end = 3061 + 7
        prds = 7

        df = data.copy()
        df.rename(columns={"Date": "ds", "Price": "y"}, inplace=True)

        prophet_price = Prophet(daily_seasonality=True, weekly_seasonality=True)
        for r in regressors:
            if r != "Price":
                prophet_price.add_regressor(r)

        prophet_price.fit(df[:end])

        price_data = prophet_price.make_future_dataframe(
            periods=prds, include_history=False
        )
        price_data["Open"] = predict_regressors("Open", end, prds)
        price_data["High"] = predict_regressors("High", end, prds)
        price_data["Low"] = predict_regressors("Low", end, prds)
        price_data["Vol"] = df["Vol"].iloc[-len(price_data) + end : end].values

        forecast_data = prophet_price.predict(price_data)
        price_future_table = forecast_data[["ds", "yhat"]].tail(15).copy()
        price_future_table.rename(
            columns={"ds": "Date", "yhat": "Predicted_Price"}, inplace=True
        )
        temp_price_forecast_list = forecast_data[["yhat"]].values.flatten().tolist()
        # print(price_future_table)
        # print(temp_price_forecast_list)
        price_forecast_list.extend(temp_price_forecast_list)
    return price_forecast_list


def arima_predictions():
    print('inside1')
    # starting_date = "2016-01-01"
    # today_date = "2024-01-02"
    # df = yfin.download("ETH-USD", starting_date, today_date)
    df = pd.read_csv("eth_modified.csv")
    print('inside2')
    df.tail()
    dfclose = df["Price"]
    dflog = np.log2(dfclose)
    training_data = dflog
    history = [x for x in training_data]
    predictions = []
    print('inside arima')
    model = ARIMA(history, seasonal_order=(0, 2, 1, 7))
    model_fit = model.fit()
    print(model_fit.summary())
    predictions = list(model_fit.forecast(7))
    predictions = np.exp2(predictions)
    return predictions.tolist()


def predictions():
    print('here')
    arima_preds = arima_predictions()
    print('here')
    prophet_preds = prophet_predictions()
    combined = np.array([arima_preds, prophet_preds]).T
    combined = np.array(np.log(combined))
    model = tf.keras.models.load_model("model_final.h5")
    final_predictions = model.predict(combined)
    final_predictions = np.exp(final_predictions).tolist()
    final_predictions = [v[0] for v in final_predictions]
    # print("----------------------")
    # print("ARIMA: ", arima_preds)
    # print("PROPHET: ", prophet_preds)
    # print("----------------------")
    print("FINAL PREDICTION: ", final_predictions)
    # print("----------------------")
    res = []
    for price in final_predictions:
        res.append(get_price_range(price))

    return res


"""
DO NOT REMOVE
"""
print('here')
preds = predictions()
assert len(preds) == 7
assert all([isinstance(val, ETHPriceRanges) for val in preds])
print(preds)
