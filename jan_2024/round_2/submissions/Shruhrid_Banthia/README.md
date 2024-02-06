This folder contains the following documents:

- `predictions_Shruhrid.py`: Python file containing code related to the predictions
- `instructions.py`: copy of the instructions.py provided during hackathon
- `requirements.txt`: libraries required
- `model_e1d1.h5`: Multivariate multistep LSTM model to predict closing price of the next 7 days
- `scaler_Close.pkl`: Scaler to be used with the LSTM

## How to Run

- First install the required libraries using
  - `pip install -r requirements.txt`
- Run the prediction python file using
  - `py predictions_Shruhrid_Banthia.py`
- Prediction results will be displayed in the terminal

## Obtained Results

We have obtained these results while running the prediction code in our machine:

- `[2330.366943359375, 2338.9970703125, 2372.23876953125, 2404.749267578125, 2361.4150390625, 2367.240966796875, 2372.28759765625]`
- These correspond to 7 days starting from 4th February.

These are the printed enum values of the above predicted prices:

```
4th Feb 2024: <ETHPriceRanges.pr_2375_2400: 14>
5th Feb 2024: <ETHPriceRanges.pr_2375_2400: 14>
6th Feb 2024: <ETHPriceRanges.pr_2350_2375: 15>
7th Feb 2024: <ETHPriceRanges.pr_2350_2375: 17>
8th Feb 2024: <ETHPriceRanges.pr_2350_2375: 15>
9th Feb 2024: <ETHPriceRanges.pr_2350_2375: 15>
10th Feb 2024: <ETHPriceRanges.pr_2350_2375: 15>

```

These could be used for verification of the prices obtained by running the Python file.
