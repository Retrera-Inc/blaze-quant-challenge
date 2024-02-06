# ETH Price Prediction using LSTM

## Overview
This project utilizes Long Short-Term Memory (LSTM) neural network for predicting future Ethereum (ETH) prices against USD. The model is trained on historical price data using the TensorFlow and scikit-learn libraries.

## Contents
- [Requirements](#requirements)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Model Architecture](#model-architecture)
- [Results](#results)

## Requirements
- Python 3.x
- NumPy
- Pandas
- scikit-learn
- TensorFlow 2.x
- google colab ID
## Usage
1. Clone the repository: git clone https://github.com/your-username/eth-price-prediction.git
2. Install the required dependencies: pip install -r requirements.txt
3. Run the predictions() function in the provided Jupyter notebook or script.

## File Structure
- ETH.csv: Historical Ethereum price data.
- eth_price_prediction.ipynb: Jupyter notebook containing the code for data preprocessing, model training, and future price prediction.
- README.md: Documentation for the project.

## Model Architecture
The LSTM model consists of three layers with dropout and batch normalization for better performance.

1. Input layer: LSTM with 50 units, return sequences.
2. Dropout layer (20% dropout rate).
3. LSTM layer with 50 units and return sequences.
4. Dropout layer (20% dropout rate).
5. LSTM layer with 50 units.
6. Dropout layer (20% dropout rate).
7. Dense layer with 1 unit for regression.

## Results
The model is trained for 16 epochs with a batch size of 32. The predictions for the next 7 days are displayed, including the predicted closing prices and corresponding dates.

Feel free to contribute and open issues for suggestions or improvements!