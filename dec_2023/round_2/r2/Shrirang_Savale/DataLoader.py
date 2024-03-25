import pandas as pd

# Read the CSV file into a DataFrame
file_path = 'Ethereum Historical Data - 1st jan to 31 dec 2023.csv'
df = pd.read_csv(file_path)

# Convert the 'Date' column to datetime format for easier manipulation
df['Date'] = pd.to_datetime(df['Date'])

# Remove commas from numerical columns
numeric_columns = ['Close', 'Open', 'High', 'Low', 'Vol.', 'Change ']
df[numeric_columns] = df[numeric_columns].replace({',': ''}, regex=True)

# Handle 'K', 'M', 'B' in the 'Vol.' column
df['Vol.'] = df['Vol.'].replace('[KMB]', '', regex=True).replace('', '1', regex=True).astype(str)  # Ensure 'Vol.' is treated as a string
df.loc[df['Vol.'].str.contains('K'), 'Vol.'] = df.loc[df['Vol.'].str.contains('K'), 'Vol.'].replace('K', '', regex=True).astype(float) * 1e3
df.loc[df['Vol.'].str.contains('M'), 'Vol.'] = df.loc[df['Vol.'].str.contains('M'), 'Vol.'].replace('M', '', regex=True).astype(float) * 1e6
df.loc[df['Vol.'].str.contains('B'), 'Vol.'] = df.loc[df['Vol.'].str.contains('B'), 'Vol.'].replace('B', '', regex=True).astype(float) * 1e9

# Sort the DataFrame by date in ascending order
df.sort_values(by='Date', inplace=True)

# Add a column for yesterday's price
df['Yesterday Price'] = df['Price'].shift(1)

# Add a column for tomorrow's price
df['Tomorrow Price'] = df['Price'].shift(-1)

# Add a column for 30-day average
df['30 Day Average'] = df['Price'].rolling(window=30).mean()

# Add a column for 7-day average
df['7 Day Average'] = df['Price'].rolling(window=7).mean()

# Add technical parameters
df['10-day SMA'] = df['Price'].rolling(window=10).mean()
df['20-day SMA'] = df['Price'].rolling(window=20).mean()
df['50-day SMA'] = df['Price'].rolling(window=50).mean()

df['12-day EMA'] = df['Price'].ewm(span=12, adjust=False).mean()
df['26-day EMA'] = df['Price'].ewm(span=26, adjust=False).mean()
df['50-day EMA'] = df['Price'].ewm(span=50, adjust=False).mean()

# Drop NaN values
df.dropna(inplace=True)

# Print the modified DataFrame
print(df)

# Save the modified DataFrame back to a new CSV file
df.to_csv('modified_file_with_technical_parameters.csv', index=False)
