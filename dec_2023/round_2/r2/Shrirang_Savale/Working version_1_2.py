import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import TimeSeriesSplit

# Load the time series data
df = pd.read_csv('modified_file_with_technical_parameters.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Drop non-numeric columns and unnecessary features
features = df.drop(['Tomorrow Price'], axis=1)
target = df['Tomorrow Price']

# Use TimeSeriesSplit for time series cross-validation
tscv = TimeSeriesSplit(n_splits=2)

# Initialize the linear regression model
model = LinearRegression()

# Perform time series cross-validation
for train_index, test_index in tscv.split(features):
    X_train, X_test = features.iloc[train_index], features.iloc[test_index]
    y_train, y_test = target.iloc[train_index], target.iloc[test_index]

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions on the test set
    predictions = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, predictions)
    print(f'Mean Squared Error: {mse}')

# Make predictions for January 1, 2024, to January 7, 2024
prediction_dates = pd.date_range(start='2023-9-17', end='2023-12-30', freq='D')
predicted_prices = []

for date in prediction_dates:
    data_point = features.loc[date].values.reshape(1, -1)
    predicted_price = model.predict(data_point)
    predicted_prices.append(predicted_price[0])

# Create a DataFrame for the predicted prices
predicted_df = pd.DataFrame(data={'Predicted Price': predicted_prices}, index=prediction_dates)

# Visualize actual vs. predicted values with connected dots
plt.figure(figsize=(30, 18))
plt.plot(target.index, target, marker='o', linestyle='-', color='blue', label='Actual Tomorrow\'s Price (Test Data)')
plt.plot(predicted_df.index.shift(-2), predicted_df['Predicted Price'], marker='o', linestyle='-', color='red', label='Predicted Tomorrow\'s Price (Validation Data)')
plt.plot(X_train.index, y_train, marker='o', linestyle='-', color='green', label='Actual Tomorrow\'s Price (Training Data)')
plt.title('Actual vs Predicted Tomorrow\'s Price')
plt.xlabel('Date')
plt.ylabel('Tomorrow\'s Price')
plt.legend()
plt.show()
