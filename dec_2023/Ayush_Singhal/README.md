# Illuvium Data Analysis

## Overview

This project involves the analysis and visualization of data related to the Illuvium cryptocurrency Tokens, including market data and tweets. It utilizes Python, Streamlit, and various libraries for data processing, analysis, and visualization.

## Project Structure

- `app.py`: Streamlit app for data analysis and visualization.
- `helper.py`: Helper functions for data preprocessing and fetching market data.
- `requirements.txt`: List of Python dependencies required for the project.

## Setup

1. Install the required dependencies by running:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

## Files and Functions

- `app.py`:
    - `main()`: Main function for the Streamlit app.
    - `generate_wordcloud(text)`: Generates a word cloud for a given text.
    - `get_sentiment(text)`: Analyzes sentiment using TextBlob.
    - `process_date(df)`: Processes date data for tweet analysis.
    - `extract(token, df)`: Extracts relevant columns from a DataFrame based on a token.

- `helper.py`:
    - Various helper functions for data preprocessing, background setup, and data fetching.

## Usage

1. Run the Streamlit app to interactively explore Illuvium market data and tweet analysis.

2. Customize and extend the functionality of `app.py` and `helper.py` based on your requirements.

## Data Sources

- Market data is fetched from the CoinGecko API.
- Tweet data is loaded from a CSV file.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to customize this README to provide more specific details about your project, how to interpret the results, and any additional features or functionalities.

