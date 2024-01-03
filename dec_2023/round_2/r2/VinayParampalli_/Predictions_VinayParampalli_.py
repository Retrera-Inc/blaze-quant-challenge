from instruction import ETHPriceRanges
from prophet import Prophet
import pandas as pd
import numpy as np


def predictions():
    price_ranges = [
        (2000, 2025),
        (2025, 2050),
        (2050, 2075),
        (2075, 2100),
        (2100, 2125),
        (2125, 2150),
        (2150, 2175),
        (2175, 2200),
        (2200, 2225),
        (2225, 2250),
        (2250, 2275),
        (2275, 2300),
        (2300, 2325),
        (2325, 2350),
        (2350, 2375),
        (2375, 2400),
        (2400, 2425),
        (2425, 2450),
        (2450, 2475),
        (2475, 2500),
        (2500, 2525),
        (2525, 2550),
        (2550, 2575),
        (2575, 2600),
    ]
    df = pd.read_csv('Ethereum.csv')
    prophet_df = df.rename(columns={'timestamp': 'ds', 'close': 'y'})
    model = Prophet()
    model.fit(prophet_df)
    future = model.make_future_dataframe(periods=8)
    forecast = model.predict(future)
    fc = forecast.tail(7)
    final_fc = fc.iloc[:, : 2]
    pred_list = final_fc['trend']
    L = np.ravel(pred_list.T).tolist()
    result = []

    for val in L:
        for i, (lower, upper) in enumerate(price_ranges, start=1):
            if lower <= val <= upper:
                result.append(ETHPriceRanges(i))
                break
        else:
            result.append(ETHPriceRanges.pr_2300_2325)

    return result


# Test the predictions
preds = predictions()


assert len(preds) == 7
assert all(isinstance(val, ETHPriceRanges) for val in preds)
print(preds)
