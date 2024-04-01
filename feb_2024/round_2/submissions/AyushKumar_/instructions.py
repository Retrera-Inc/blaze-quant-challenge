"""
For round 2, you have to predict ETH price in USD between Mar 16th and Feb 22nd 2024 (inclusive).
Each team will have to make 7 predictions; one for each day. The prediction has to be
within a range. Each range is inclusive of the lower bound and exclusive of the higher bound.
E.g. pr_2000_2025 is [2000, 2025).

Note: the price ranges might be updated closer to Mar 16.
Please copy the example to add your predictions.
We will call the predictions function on Feb Mar 16 12:00 AM PST. After that, the predictions
will not be altered.

We will take the closing price on the day as the correct price. The source for the closing
price will be https://coinmarketcap.com/currencies/ethereum/. Coin market cap provides
prices at 5 min intervals. We will take the price at 11:55 pm PST as the closing price.
"""
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


class ARBPriceRanges(Enum):
    pr_180_185 = 1
    pr_185_190 = 2
    pr_190_195 = 3
    pr_195_200 = 4
    pr_200_205 = 5
    pr_205_210 = 6
    pr_210_215 = 7
    pr_215_220 = 8


class LINKPriceRanges(Enum):
    pr_1800_1825 = 1
    pr_1825_1850 = 2
    pr_1850_1875 = 3
    pr_1875_1900 = 4
    pr_1900_1925 = 5
    pr_1925_1950 = 6
    pr_1950_1975 = 7
    pr_1975_2000 = 8
    pr_2000_2025 = 9
    pr_2025_2050 = 10
    pr_2050_2075 = 11
    pr_2075_2100 = 12
    pr_2100_2125 = 13
    pr_2125_2150 = 14
    pr_2150_2175 = 15
    pr_2175_2200 = 16