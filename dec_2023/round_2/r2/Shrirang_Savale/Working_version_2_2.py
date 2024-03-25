# Importing the Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from keras.layers import LSTM, Dense, Dropout
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.dates as mdates
from sklearn.preprocessing import MinMaxScaler
from sklearn import linear_model
from keras.models import Sequential
from keras.layers import Dense
import keras.backend as K
from keras.callbacks import EarlyStopping
from keras.optimizers import Adam
from keras.models import load_model
from keras.layers import LSTM
from keras.utils import plot_model

# Importing additional libraries for GPU support
from tensorflow.python.client import device_lib
from keras import backend as K

# Check available devices
print(device_lib.list_local_devices())
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

# Use GPU if available
if len(tf.config.experimental.list_physical_devices('GPU')) > 0:
    print("Using GPU")
    # Set TensorFlow to use GPU memory growth
    for device in device_lib.list_local_devices():
        if device.device_type == 'GPU':
            tf.config.experimental.set_memory_growth(device, True)
    # Set Keras backend to use GPU
    K.set_floatx('float32')
    K.set_epsilon(1e-7)

# Get the Dataset
df = pd.read_csv('modified_file_with_technical_parameters.csv', na_values=['null'], index_col='Date', parse_dates=True, infer_datetime_format=True)
df.head()

# Print the shape of DataFrame and Check for Null Values
print("Dataframe Shape: ", df.shape)
print("Null Value Present: ", df.isnull().values.any())

# Extract features and output variable
features = ['Open', 'High', 'Low', 'Vol.', 'Change', 'Yesterday Price', '30 Day Average', '7 Day Average',
            '10-day SMA', '20-day SMA', '50-day SMA', '12-day EMA', '26-day EMA', '50-day EMA']
output_var = pd.DataFrame(df['Price'])

# Normalize features
scaler = MinMaxScaler()
feature_transform = scaler.fit_transform(df[features])
feature_transform = pd.DataFrame(columns=features, data=feature_transform, index=df.index)

# Splitting to Training set and Test set
timesplit = TimeSeriesSplit(n_splits=5)
for train_index, test_index in timesplit.split(feature_transform):
    X_train, X_test = feature_transform[:len(train_index)], feature_transform[len(train_index):(len(train_index) + len(test_index))]
    y_train, y_test = output_var[:len(train_index)].values.ravel(), output_var[len(train_index):(len(train_index) + len(test_index))].values.ravel()

# Process the data for LSTM
trainX = np.array(X_train)
testX = np.array(X_test)
X_train = trainX.reshape(X_train.shape[0], 1, X_train.shape[1])
X_test = testX.reshape(X_test.shape[0], 1, X_test.shape[1])

# Building the LSTM Model with multiple layers
lstm = Sequential()

# First LSTM layer
lstm.add(LSTM(32, input_shape=(1, trainX.shape[1]), activation='relu', return_sequences=True))

# Additional LSTM layers
lstm.add(LSTM(64, activation='relu', return_sequences=True))
lstm.add(LSTM(128, activation='relu', return_sequences=False))  # Last layer does not return sequences

# Dense layer
lstm.add(Dense(1))

# Compile the model
lstm.compile(loss='mean_squared_error', optimizer='adam')
plot_model(lstm, show_shapes=True, show_layer_names=True)

# Train the model on GPU
with tf.device('/GPU:0'):
    history = lstm.fit(X_train, y_train, epochs=150, batch_size=4, verbose=1, shuffle=False)

# Make predictions
y_pred = lstm.predict(X_test)

# Save the trained model
lstm.save('lstm_model.h5')

# Plotting predicted vs true prices
plt.plot(y_test, label='True Price')
plt.plot(y_pred, label='LSTM Price')
plt.title("Prediction by LSTM")
plt.xlabel('Time Scale')
plt.ylabel('Scaled USD')
plt.legend()
plt.show()