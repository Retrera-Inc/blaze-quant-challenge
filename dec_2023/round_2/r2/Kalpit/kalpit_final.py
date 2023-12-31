# -*- coding: utf-8 -*-
"""Kalpit_Final

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mNA8wNozIZawpd4wxlnG0Whl0wgo973l

**The Final Prediction Function's output has been edited according to my final predictions**
"""

import pandas as pd
eth=pd.read_csv('eth.csv')

eth.plot(kind="line", x="Date", y="Close", figsize=(12,6))

prophet_data = eth[["Date", "Close"]]

prophet_data = prophet_data.rename(columns = {
    "Date": "ds",
    "Close": "y"
})

prophet_data.head()
from prophet import Prophet

prophet = Prophet(daily_seasonality=True)

prophet.fit(prophet_data)

print("Data fitted")

future = prophet.make_future_dataframe(periods=7, include_history=False)

future.tail()
forecast = prophet.predict(future)

forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

forecast.info()

import matplotlib as mpl
import matplotlib.pyplot as plt

fig = plt.figure(dpi=100)

fig.set_facecolor("white")

prophet_plot_forecast_fig = prophet.plot(forecast, ax=fig.gca());

prophet_plot_forecast_fig.savefig('forecast_details.png')

prophet.plot_components(forecast);

PLOT_COLUMS = [
    "Price",
    "Price (forecast)",
]

mpl.style.use("seaborn")

result_df = prophet_data.copy()

# Add first result from forecast as y to connect dots
result_df = result_df.append(result_df.tail(1).rename(columns = {"y": "yhat"}))

result_df = result_df.append(forecast)

result_df = result_df.rename(columns = {
    "ds": "Date",
    "y": "Price",
    "yhat": "Price (forecast)"
})

fig = plt.figure(dpi=100)

fig.set_facecolor("white")

plot = result_df.plot(x="Date", y=PLOT_COLUMS, figsize=(15, 8), ax=fig.gca())

plot_fig = plot.get_figure()

forecast

# Online references for better accuracy

l1=[2350.77,2400.14,2450.54,2502,2554.54,2608.19,2662.96]
l2=[2340.97,2319.40,2304.11,2303.55,]
l3=[2289,2287,2246,2163]
l4=[2452,2460,2468,2478,2482,2493,2502]
l5=[2373,2403,2438,2497,2584,2402,2322]
l6=[2295,2351,2382,2417,2476,2563,2379]
l7=[2277.724,2295.360,2346.903,2368.092,2325.378,2325.999,2301.828]
l8=[2223,2258,2349,2392,2348,2324,2253]
gh=pd.DataFrame()
# gh['a1']=l1
gh['a2']=l4
gh['a3']=l5
gh['a4']=l6
gh['a5']=l7
gh['a6']=l8

gh.corr()

gh.a3.plot()
gh.a4.plot()
gh.a5.plot()
gh.a6.plot()

forecast['trend']

gh

final_pred=[2360,2396,2402,2440,2404,2414,2380]

gh['fin']=final_pred
gh.fin.plot()

gh.plot()

from enum import Enum


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

def predictions():
    """
    All of the business logic should go here. The output should be a list
    of size 7 with values from ETHPriceRanges
    """
    return [
        ETHPriceRanges.pr_2350_2375,
        ETHPriceRanges.pr_2375_2400,
        ETHPriceRanges.pr_2400_2425,
        ETHPriceRanges.pr_2425_2450,
        ETHPriceRanges.pr_2400_2425,
        ETHPriceRanges.pr_2400_2425,
        ETHPriceRanges.pr_2375_2400,
    ]


"""
DO NOT REMOVE
"""
preds = predictions()
assert len(preds) == 7
assert all([isinstance(val, ETHPriceRanges) for val in preds])

