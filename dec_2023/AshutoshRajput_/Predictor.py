#numpy module is imported for creating arrays with the data
import numpy as np
#matplotlib module is imported to graph the prediciton
import matplotlib.pyplot as plt
#pandas module is imported to edit the dataset
import pandas as pd
#pandas-datareader module is imported to get the prices of the crypto currencies using yahoo finance 
import pandas_datareader as web
#datetime module is imported for the calculation of days
import datetime as dt

#MinMaxScaler is imported from sklearn to scale the data between 0 and 1 for nerual network calculation
from sklearn.preprocessing import MinMaxScaler
#tensorflow modules are imported for the neural network creation
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.models import Sequential
from tensorflow.python.keras.backend import shape

#The cryptocurrency to be predicted and base currency is defined here
crypto_currency = "BTC"
against_currency = "USD"

#Start and end date for test data
start = dt.datetime(2016, 1, 1)
end = dt.datetime.now()

#uses DataReader from pandas module to get the historical price data from yahoo finance
data = web.DataReader(f"{crypto_currency}-{against_currency}", "yahoo", start, end)

#Prepare data
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(data["Close"].values.reshape(-1,1))

#sets the number of days to be predicted and test data
#looks at past [prediction_days] to predict
prediction_days = 60
future_day = 30

#creates x_train and y_train
x_train, y_train = [], []


for x in range(prediction_days, len(scaled_data)-future_day):
    #past [prediction_days] and appends the real data to x_train
    x_train.append(scaled_data[x-prediction_days:x, 0])
    #the [future_day] is appended as the trained predected data to y_train
    y_train.append(scaled_data[x+future_day, 0])
    
#turns x and y train into numpy arrays and then reshapes them
x_train, y_train = np.array(x_train), np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

#Create neural network

model = Sequential()

#LSTM layers for feeding data to neural network. Dropout layers to prevent overfitting
model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50))
model.add(Dropout(0.2))
model.add(Dense(units=1))

#compiling and fitting the model 
model.compile(optimizer="adam", loss="mean_squared_error")
model.fit(x_train, y_train, epochs=25, batch_size=32)


#Testing the model

test_start = dt.datetime(2020, 1, 1)
test_end = dt.datetime.now()

test_data = web.DataReader(f"{crypto_currency}-{against_currency}", "yahoo", test_start, test_end)
actual_prices = test_data["Close"].values

#combine the test data and actual data
total_dataset = pd.concat((data["Close"], test_data["Close"]), axis=0)

#places the actual data - test and prediction data into the model input 
model_inputs = total_dataset[len(total_dataset) - len(test_data) - prediction_days:].values
model_inputs = model_inputs.reshape(-1, 1)
model_inputs = scaler.fit_transform(model_inputs)

x_test = []

for x in range(prediction_days, len(model_inputs)):
    x_test.append(model_inputs[x-prediction_days:x, 0])

x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

#Predicts the prices using the model
prediction_prices = model.predict(x_test)
prediction_prices = scaler.inverse_transform(prediction_prices)

#Plots them on a graph
plt.plot(actual_prices, color="black", label="Actual Prices")
plt.plot(prediction_prices, color="green", label="Predicited Prices")
plt.title(f"{crypto_currency} Price Prediction")
plt.xlabel("Time")
plt.ylabel("Price")
plt.show()

#Predict next day

real_data = [model_inputs[len(model_inputs) + 1 - prediction_days:len(model_inputs) + 1, 0]]
read_data = np.array(real_data)
real_data = np.reshape(read_data, (real_data.shape[0], real_data.shape[1], 1))

prediction = model.predict(real_data)
prediction = scaler.inverse_transform(prediction)
print()
