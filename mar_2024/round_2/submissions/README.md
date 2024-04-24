# Time Series Analysis and Forecasting Report for Ethereum (ETH), Arbitrum (ARB), and Chainlink (LINK) Token Prices

## Introduction

Cryptocurrencies have become increasingly popular investment assets, characterized by their high volatility and potential for 
significant gains or losses. In this report, we conduct a time series analysis to forecast the prices of Ethereum (ETH), 
Arbitrum (ARB), and Chainlink (LINK) tokens from April 17th to April 25th, 2024. Our analysis employs the AutoRegressive 
Integrated Moving Average (ARIMA) model, a powerful tool for predicting future values based on historical data patterns.

## Data Collection and Preprocessing

Historical price data for Ethereum (ETH), Arbitrum (ARB), and Chainlink (LINK) tokens are gathered from reliable 
cryptocurrency exchanges. The data undergoes preprocessing, including handling missing values, ensuring consistency in 
timestamps, and transforming the data to achieve stationarity if necessary.

## Exploratory Data Analysis (EDA)

Descriptive statistics are computed to summarize the characteristics of the data, such as measures of central tendency and 
dispersion. Visualization techniques such as time series plots, histograms, and box plots are utilized to identify trends, 
seasonality, and anomalies in the data.

## Model Selection

The ARIMA model is selected for its ability to capture the temporal dependencies present in time series data. The 
determination of the optimal lag order is crucial for the effectiveness of the ARIMA model. This is achieved through the 
analysis of the Partial Autocorrelation Function (PACF) and Autocorrelation Function (ACF) plots.

## Model Fitting

Once the optimal lag order is determined, the ARIMA model is fitted to the data. The model parameters are estimated, 
including the coefficients for the autoregressive (AR) and moving average (MA) terms, as well as the differencing order (d).

## Model Evaluation

Diagnostic checks are performed to assess the goodness of fit of the ARIMA model. This includes examining residual plots to 
ensure that the residuals are approximately normally distributed with constant variance. Additionally, forecast accuracy 
measures such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE) are computed to 
evaluate the performance of the model.

## Forecasting

Using the fitted ARIMA model, forecasts are generated for the prices of Ethereum (ETH), Arbitrum (ARB), and Chainlink 
(LINK) tokens for the specified period from April 17th to April 25th, 2024. Forecast intervals are provided to indicate 
the uncertainty associated with the predictions.

---

## Code Results

### Chainlink (LINK)

The ARIMA model results indicate an optimal order of (1,1,1) for the Chainlink token. The degree of fit on test data is 
89.69%. 

**Price Predictions (Model run on 15th April 4 pm)**

- 16 April expected = 13.346202
- 17 April expected = 13.346253
- 18 April expected = 13.346207
- 19 April expected = 13.346235
- 20 April expected = 13.346218
- 21 April expected = 13.346228
- 22 April expected = 13.346222

**Dependency of Price on other factors**

- Daily Change: 0.047028
- Volatility: 0.883769
- Intraday Movement: 0.676716

### Arbitrum (ARB)

The ARIMA model results indicate an optimal order of (1,1,1) for the Arbitrum token. The degree of fit on test data is 
92.33%.

**Price Predictions (Model run on 15th April 4 pm)**

- 16 April expected = 1.033838
- 17 April expected = 1.053270
- 18 April expected = 1.057184
- 19 April expected = 1.056649
- 20 April expected = 1.055558
- 21 April expected = 1.054275
- 22 April expected = 1.054498

**Dependency of Price on other factors**

- Daily Change: 0.085776
- Volatility: 0.712496
- Intraday Movement: 0.621387

### Ethereum (ETH)

The ARIMA model results indicate an optimal order of (1,1,1) for Ethereum. The degree of fit on test data is 96.87%.

**Price Predictions (Model run on 15th April 4 pm)**

- 16 April expected = 2976.258340
- 17 April expected = 2929.701366
- 18 April expected = 2927.923741
- 19 April expected = 2921.602093
- 20 April expected = 2912.680727
- 21 April expected = 2911.493823
- 22 April expected = 2910.533332

**Dependency of Price on other factors**

- Daily Change: 0.074245
- Volatility: 0.794026
- Intraday Movement: 0.696286

---

## Question 2

### Ethereum (ETH):

- 2023: BTC (0.91), BNB (0.05)
- 2024: BTC (0.96), UNI (0.56)

### Arbitrum (ARB):

- 2023: BNB (0.81), UNI (0.08)
- 2024: ADA (0.28), BNB (-0.50)

### Chainlink (LINK):

- 2023: BTC (0.86), BNB (-0.15)
- 2024: ADA (0.75), MKR (0.30)

---

## Potential Use in Model Building

These observed changes in correlations can be helpful when building a model for cryptocurrency price prediction, but with 
some important considerations:

- **Feature Selection**: Strong positive correlations suggest that including the price data of a particular cryptocurrency 
as a feature in your model might be beneficial.
  
- **Time-Series Analysis**: Correlations can change significantly over time. Regularly analyzing these correlations allows 
you to adapt your model features accordingly.

### Limitations

- Correlations don't capture all the relationships between cryptocurrencies. 
- Other factors like market sentiment, news events, and regulations can influence price movements.
- Correlations can change rapidly, making it challenging to rely solely on historical data for future predictions.

Overall, analyzing correlation changes can provide valuable insights for feature selection in your model. However, it's 
crucial to combine this information with other techniques and considerations for robust price prediction.
