This folder contains the following documents:

- `predictions_Shruhrid_Banthia.py`: Python file containing code related to the predictions
- `instructions.py`: copy of the instructions.py provided during hackathon
- `requirements.txt`: libraries required
- `eth_modified.csv`: historical data related to Ethereum
- `estimator.ipynb`: generating a neural network meta learner through stacking based ensemble learning using FbProphet and ARIMA
- `model_final.h5`: neural network model obtained through `estimator.ipynb`

## How to Run

- First install the required libraries using
  - `pip install -r requirements.txt`
- Run the prediction python file using
  - `py predictions_Shruhrid_Banthia.py`
- Prediction results will be displayed in the terminal

## Obtained Results

We have obtained these results while running the prediction code in our machine:

- `[2318.503662109375, 2374.12255859375, 2396.463134765625, 2381.54248046875, 2367.949462890625, 2359.844970703125, 2373.169677734375]`
- These correspond to 7 days starting from 2nd Jan till 8th Jan, 2024.

These are the printed enum values of the above predicted prices:

```
2nd Jan 2024: <ETHPriceRanges.pr_2300_2325: 13>
3rd Jan 2024: <ETHPriceRanges.pr_2350_2375: 15>
4th Jan 2024: <ETHPriceRanges.pr_2375_2400: 16>
5th Jan 2024: <ETHPriceRanges.pr_2375_2400: 16>
6th Jan 2024: <ETHPriceRanges.pr_2350_2375: 15>
7th Jan 2024: <ETHPriceRanges.pr_2350_2375: 15>
8th Jan 2024: <ETHPriceRanges.pr_2350_2375: 15>
```

These could be used for verification of the prices obtained by running the Python file.
