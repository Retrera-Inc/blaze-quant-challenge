import requests
from datetime import datetime
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
    pr_2600_2625 = 25
    pr_2625_2650 = 26
    pr_2650_2675 = 27
    pr_2675_2700 = 28
    pr_2700_2725 = 29
    pr_2725_2750 = 30
    pr_2750_2775 = 31
    pr_2775_2800 = 32
    pr_2800_2825 = 33
    pr_2825_2850 = 34
    pr_2850_2875 = 35
    pr_2875_2900 = 36
    pr_2900_2925 = 37
    pr_2925_2950 = 38
    pr_2950_2975 = 39
    pr_2975_3000 = 40
    pr_3000_3025 = 41
    pr_3025_3050 = 42
    pr_3050_3075 = 43
    pr_3075_3100 = 44
    pr_3100_3125 = 45
    pr_3125_3150 = 46
    pr_3150_3175 = 47
    pr_3175_3200 = 48
    pr_3200_3225 = 49
    pr_3225_3250 = 50
    pr_3250_3275 = 51
    pr_3275_3300 = 52
    pr_3300_3325 = 53
    pr_3325_3350 = 54
    pr_3350_3375 = 55
    pr_3375_3400 = 56
    pr_3400_3425 = 57
    pr_3425_3450 = 58
    pr_3450_3475 = 59
    pr_3475_3500 = 60
    pr_3500_3525 = 61
    pr_3525_3550 = 62
    pr_3550_3575 = 63
    pr_3575_3600 = 64
    pr_3600_3625 = 65
    pr_3625_3650 = 66
    pr_3650_3675 = 67
    pr_3675_3700 = 68
    pr_3700_3725 = 69
    pr_3725_3750 = 70
    pr_3750_3775 = 71
    pr_3775_3800 = 72
    pr_3800_3825 = 73
    pr_3825_3850 = 74
    pr_3850_3875 = 75
    pr_3875_3900 = 76
    pr_3900_3925 = 77
    pr_3925_3950 = 78
    pr_3950_3975 = 79
    pr_3975_4000 = 80


def get_historical_data():
    """
    Fetches historical ETH price data from Alpha Vantage API.
    """
    base_url = "https://www.alphavantage.co/query"
    params = {
        "function": "DIGITAL_CURRENCY_DAILY",
        "symbol": "ETH",
        "market": "USD",
        "apikey": "HN9TAYO0NEZNZUPO"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    prices = [float(day["4b. close (USD)"]) for day in data["Time Series (Digital Currency Daily)"].values()]
    return prices


def calculate_moving_averages(prices, window):
    """
    Calculates Simple Moving Average (SMA) for a given window size.
    """
    moving_averages = []
    for i in range(len(prices)):
        if i < window - 1:
            moving_averages.append(None)
        else:
            window_data = prices[i - window + 1: i + 1]
            average = sum(window_data) / window
            moving_averages.append(average)
    return moving_averages


def predict_price_ranges(prices, window):
    """
    Predicts price ranges based on calculated indicators.
    """
    predictions = []
    current_price = prices[-1]
    sma = calculate_moving_averages(prices, window)[-1]
    if current_price > sma:
        lower_bound = int(current_price)
        upper_bound = lower_bound + 25
    else:
        lower_bound = int(current_price) - 25
        upper_bound = lower_bound
    price_range_enum = ETHPriceRanges[f"pr_{lower_bound}_{upper_bound}"]
    predictions.append(price_range_enum)
    return predictions


# Fetch historical data for ETH
historical_ETH_prices = get_historical_data()

# Set parameters
window_size = 20

# Make predictions for ETH
eth_predictions = predict_price_ranges(historical_ETH_prices, window_size)

# Display predictions for ETH
print("Predictions for ETH:")
for prediction in eth_predictions:
    print(prediction)
