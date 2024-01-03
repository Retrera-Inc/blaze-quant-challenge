# LSTM Model for Ethereum Price Forecasting

## Model Performance

- **R-squared (R2) Score:** 0.9624576006246804
- **Model Type:** Long Short-Term Memory (LSTM)

## Overview

This LSTM model was trained to forecast the Ethereum price. The model demonstrates a high level of accuracy, as evidenced by an impressive R-squared (R2) score of 0.9625.

## Model Details

- **Model Architecture:** LSTM (Long Short-Term Memory)
- **Performance Metric:** R-squared (R2) Score
- **Training Data:** Historical Ethereum price data
- **Mean Average Precision (MAP):** 22

## Model Performance Visualization for 90 days of testing data

![](img.png)

## Usage

1. **Loading the Model:**
   ```python
   from tensorflow.keras.models import load_model

   model = load_model("final_model.h5")
