import streamlit as st
from PIL import Image

st.markdown(
    """
# Curve Finance Overview

## Core Concept: Stablecoin Exchange

Curve is primarily a platform for swapping stablecoins (like USDC, DAI, etc.) with minimal slippage due to its specialized liquidity pools. This focus on stablecoins is a key differentiator from other decentralized exchanges (DEXs) that cater to a wider range of cryptocurrencies.

## Liquidity Pools & Liquidity Providers

- **Liquidity Pools:** Curve uses liquidity pools where users can deposit their stablecoins. These pools facilitate trading between different stablecoins.
- **Liquidity Providers:** Users who deposit their coins in these pools are known as liquidity providers (LPs). They earn fees from the trades executed in the pool, proportional to their share in the pool.

## CRV Token & Governance

- **CRV Token:** Curve has its own native token, CRV, used for governance and incentivizing liquidity.
- **Governance:** CRV holders can propose and vote on changes to the protocol, like fee structures or adding new pools.

## Low Slippage & High Efficiency

- **Algorithm:** Curve employs a market-making algorithm tailored for stablecoins. This algorithm reduces slippage, i.e., the difference between expected and actual trade prices, especially beneficial for large trades.
- **Efficiency:** By focusing on assets that are generally stable in price relative to each other, Curve can provide more efficient and cost-effective trades compared to traditional DEX models.
"""
)

st.markdown(
    """
### **Incentivization & Yield Farming**

- **Yield Farming:** Users can engage in yield farming by providing liquidity and earning CRV tokens as rewards. This process involves staking their LP tokens to earn additional rewards.
- **Incentives for LPs:** LPs are incentivized through trading fees and CRV rewards, leading to a robust liquidity environment.
"""
)

# Risks & Management Section
st.markdown(
    """
### **Risks & Management**

- **Smart Contract Risk:** As with all DeFi platforms, Curve is exposed to smart contract risks. They mitigate this through audits and robust security practices.
- **Liquidity Risk:** Like many other DeFi platforms Curve addresses this by offering attractive rewards and ensuring a user-friendly experience.
"""
)

# Revenue Stream and Business Model Section
st.markdown(
    """
## Revenue Stream and Business Model

The primary revenue stream for Curve comes from trading fees charged on each transaction. These fees are distributed among liquidity providers, aligning their interests with the platform's growth.
- **Traders** engage in transactions on the Curve Finance platform, paying trading fees for the swaps they perform. In the example, this fee is represented as $100.
- The trading fees are then split between the liquidity providers and Curve Finance itself.
- **Liquidity Providers**, who supply the stablecoins to the liquidity pools enabling trades, receive the majority of the trading fees as compensation for their capital investment. In the image, they receive \$67 out of the \$100 collected.
- **Curve Finance** retains a portion of the trading fees as **revenue**. In the image, Curve's share is shown as $33.
"""
)

# Image Example (make sure to download and place the image in the same directory as your script)
image_path = "./assets/business_model.png"
image = Image.open(image_path)
st.image(image, caption="Image Source: Token Terminal")

# veCRV Section
st.subheader("veCRV")
st.write(
    '**`veCRV`** refers to "vote-escrowed CRV". In the veCRV model, users lock their CRV tokens for a period of time. In return, they receive veCRV tokens...'
)
st.write(
    "`veCRV` holders get boosted governance power, boosted staking rewards and get a cut of the trading fees on the platform..."
)
st.write(
    "By locking CRV tokens to obtain veCRV, immediate sell pressure on the CRV token is reduced..."
)

# Table for CRV vs veCRV Holders
st.markdown(
    """
| Incentives | CRV Holders | veCRV Holders |
| --- | --- | --- |
| Staking Rewards | ✓ | ✓ (Boosted) |
| Governance Power | ✓ | ✓ (Boosted) |
| Admin Fee Collection (Share of Trading Fees) |  | ✓ |
| Participation in Protocol Decisions | ✓ | ✓ |
| Eligibility for Airdrops and Additional Rewards | ✓ | ✓ |
| Access to Yield Farming Opportunities | ✓ | ✓ |
"""
)

# Exploratory Data Analysis Section
st.subheader("Exploratory Data Analysis")
st.write("We will look at the following metrics for the EDA of curve platform - ")
st.write("*Data source: Token Terminal*")

# List of metrics for EDA
eda_metrics = [
    "Code commits - The number of commits to Curve's public GitHub repository",
    "Core developers - The number of developers in Curve's public GitHub repositories",
    "Price - Average price of the CRV governance token",
    "CRV Token Holders - Number of addresses with CRV token balance greater than 0",
    "CRV Trading Volume - The trading volume of CRV token",
    "Revenue - Share of the trading fees that goes to the protocol",
    "Token Incentives - USD value of the protocol's governance token that have been distributed to users",
    "Expenses - Total on-chain expense of the protocol (currently only token incentives)",
    "Earnings - Revenue minus token incentives",
    "Fees - Total trading fees paid by traders",
    "Market cap circulating - Current supply * average price of governance token",
    "Market cap fully diluted - Maximum supply * average price of governance token",
    "P/F ratio circulating - Circulating market cap / Annualised fee",
    "P/F ratio fully diluted - Fully diluted market cap / Annualised fee",
    "P/S ratio circulating - Circulating market cap / Annualised revenue",
    "P/S ratio fully diluted - Fully diluted market cap / Annualised revenue",
    "Supply side fees - Share of the trading fees that goes to the liquidity providers",
    "Trading Volume - Trading Volume on Curve",
    "Treasury - USD value of the protocol's fund held on-chain including undistributed tokens",
    "TVL (Total Value Locked) - Average value of the funds locked into Curve's protocol",
]


for metric in eda_metrics:
    st.write(f"- {metric}")

# Seasonality Section
st.subheader("Seasonality")

st.write(
    "Upon decomposing to obtain the seasonality of some of the key metrics, we notice that these seem to be repeating at a cadence of 1 year upon filtering the noise."
)

# Displaying images for each metric
# Replace 'path_to_your_image.png' with the actual paths or URLs to your images

st.markdown("**Revenue**")
image_path = "./assets/revenue.png"
image = Image.open(image_path)
st.image(image)

st.markdown("**TVL**")
image_path = "./assets/tvl.png"
image = Image.open(image_path)
st.image(image)

st.markdown("**Trading volume on CRV**")
image_path = "./assets/trading_volume_crv.png"
image = Image.open(image_path)
st.image(image)

st.markdown("**Trading volume of CRV Governance token**")
image_path = "./assets/trading_volume_crv_token.png"
image = Image.open(image_path)
st.image(image)

st.markdown("**Number of holders of CRV Governance token**")
image_path = "./assets/number_of_holders_crv.png"
image = Image.open(image_path)
st.image(image)

# Correlation Section
st.subheader("Correlation")

st.write(
    "Now let's take a look at how the correlation matrix for these metrics looks like and see if it fits in with our understanding of Curve Finance -"
)

# Display the correlation matrix image
st.markdown("**Correaltion Matrix**")
image_path = "./assets/correlation.png"
image = Image.open(image_path)
st.image(image)

# Metrics showing strong correlation
st.markdown(
    """
**Some metrics showing strong correlation**:

1. **Revenue & Supply Side Fees** - There is a strong correlation which holds up with our understanding of the business since these are both parts of the total fees that is collected. Hence the correlation between fees and each of revenue and supply side fees individually is also 1.
2. **Treasury & Expenses** - This could potentially indicate that as the size of the treasury increases the tokens are distributed to the users.
3. **Price & Treasury** - This is logical given the treasury would potentially contain a high amount of CRV token.
4. **Price & CRV Trading Volume, Price & Circulating Market Cap, Price & Token Incentives** - Strong correlation given that these metrics are a function of CRV price.
"""
)

# Metrics showing strong negative correlation
st.markdown(
    """
**Some metrics showing strong negative correlation**:

1. **Token Incentives and Earnings** - As more tokens are distributed Earnings decreases since `Earnings = Revenue - Token Incentives`.
2. **Treasury and Earnings** - This is expected since tokens are distributed from the treasury.
"""
)

# Interesting insights
st.markdown(
    """
**Interesting insights**:

1. The number of token holders of CRV seems to be increasing as the number of core developers increase. This could indicate the conviction of token holders in a robust product-focused team.
2. However, the trading volume seems to have a negative correlation. This could be due to market speculation or even the broader decentralized finance trends around a given time.
3. Price and token holders seem to have a negative correlation. This could be due to the regular market sentiments wherein people are more likely to buy a token when its price increases due to a fear of missing out on opportunity.
"""
)

st.subheader("Historical Evolution")

# Display the weekly trading volume graph
st.markdown("**Significant shifts**")
image_path = "./assets/weekly_trading_volume.png"
image = Image.open(image_path)
st.image(image)

st.write(
    "Based on the weekly trading volume the three most significant dates are - `2023-03-12, 2022-11-13, 2022-05-15`"
)

# Event Descriptions
st.markdown(
    """
1. **2023-03-12** - On March 12, 2023, Curve Finance, a platform for trading digital currencies, saw its highest ever trading in a single day, going over $7 billion. This surge happened because the Silicon Valley Bank, a major bank, faced serious problems, causing widespread worry in financial markets. This situation affected USD Coin (USDC), a major digital currency meant to have a stable value equal to the U.S. dollar. But its value dropped below the dollar. Curve, which is a popular place for trading major stablecoins including USDC, Tether (USDT), Frax (FRAX), Dai (DAI), and TrueUSD (TUSD), experienced a lot of selling of USDC. This drop in USDC's value also affected other similar digital currencies, like DAI, which lost 5 percent of its value. As a result, the organization behind DAI, MakerDAO, quickly proposed measures to reduce risks and suggested limiting the creation of new DAI using USDC. [Tweet link from Curve's Official Handle](https://twitter.com/CurveFinance/status/1634543016818929664) | [News Article](https://cointelegraph.com/news/curve-finance-trading-volume-reaches-7b-historic-high-after-usdc-depeg)

2. **2022-11-13** - On November 13, 2022, CRV, saw a sudden and sharp decrease in value, dropping 17% to its lowest point in two years at 40 cents. However, it quickly rebounded to 53 cents. During this time, there was a noticeable increase in the amount of CRV held in digital wallets managed by centralized platforms, going up by 70% to a record 148.9 million. This meant there were more CRV tokens available for trading on these platforms. This event was significant for the online financial market, especially because Curve Finance is a major provider of funds in this sector. A part of this increase in CRV on exchanges was linked to a large trader borrowing 20 million CRV and moving half to another platform, likely to sell it. This action was called a "big short" in Curve's own newsletter. Additionally, there was a decrease in the number of users willing to contribute their tokens to Curve's fund pools, which might affect Curve's performance in the near future. [News Article](https://www.coindesk.com/markets/2022/11/22/curves-crv-token-slides-17-as-exchange-balance-hits-record-high/)

3. **2022-05-15** - Curve Finance started working with a technology called Aurora from Near Protocol. Aurora is built to work with Ethereum, a popular blockchain platform. This collaboration made it easier for people to use their Ethereum-based digital wallets, like MetaMask, to access Curve's features and participate in its financial pools. Near Protocol's financial hub, Proximity Labs, supported this partnership by promising up to $7.5 million in funding to Curve. This move was aimed at improving Curve's ability to exchange different types of stable digital currencies and to integrate more deeply with Aurora's financial system. This development helped Aurora strengthen its position in an environment where multiple blockchain networks operate together. [News Article](https://www.coindesk.com/markets/2022/05/05/curve-finance-integrates-with-nears-aurora-network/)
"""
)

# veCRV Impact Section
st.subheader("veCRV Impact")

# Total Curve Holders with 30-Day Moving Average
st.markdown(
    """
1. **Total Curve Holders with 30-Day Moving Average (average taken for the last 30 days)**:
    - Before the launch of veCRV, there was a steady increase in the number of Curve token holders.
    - The launch of veCRV seems to have accelerated this growth, with a sharp rise in the number of holders immediately following the launch.
    - The 30-day moving average shows a smoothing of the daily fluctuations and indicates a sustained increase in token holders.
"""
)
st.markdown("**30 day moving average of curve holders**")
image_path = "./assets/curve_holders_30dma.png"
image = Image.open(image_path)
st.image(image)

# Total Value Locked (TVL) in Curve with 30-Day Moving Average
st.markdown(
    """
2. **Total Value Locked (TVL) in Curve with 30-Day Moving Average**:
    - TVL, a measure of the total assets held in Curve liquidity pools, shows a rapid increase following the veCRV launch, indicating that it incentivized more users to lock their assets.
    - The long term trend seems to be in line with the defi market cycle around that time.
"""
)
st.markdown("**30 day moving average of TVL**")
image_path = "./assets/tvl_30dma.png"
image = Image.open(image_path)
st.image(image)

# Price of Curve with 30-Day Moving Average
st.markdown(
    """
3. **Price of Curve with 30-Day Moving Average**:
    - There isn't a significant spike in the price of Curve tokens immediately following the veCRV launch. The graph shows that the price remains relatively stable or even slightly decreases post-launch before eventually increasing.
    - The increase in the token price seems to occur about a month after the veCRV launch. This delay suggests that other factors, potentially including the broader crypto bull market during late 2020 and early 2021, could have influenced the price increase rather than the immediate impact of veCRV's introduction.
"""
)
st.markdown("**30 day moving average of TVL**")
image_path = "./assets/price_30dma.png"
image = Image.open(image_path)
st.image(image)

# CRV Lock Rates
st.markdown(
    """
4. **CRV Lock Rates**:

    *Data Source: Dune https://dune.com/queries/1119876/2985589*

    - This graph indicates the percentage of daily CRV emissions locked as veCRV.
    - There's a steady increase in the amount of CRV being locked up, showing a growing interest in boosted yields incentive to the veCRV holders and also potentially in participating in the governance of the protocol through veCRV.
    - The overall increasing trend in the lock rate implies that the veCRV mechanism successfully incentivized long-term holding and participation in governance, which is essential for the protocol's stability and success.
"""
)
st.markdown("**30 day moving average of TVL**")
image_path = "./assets/lock_rates_100dma.png"
image = Image.open(image_path)
st.image(image)

# Qualitative Assessment for Governance
st.markdown(
    """
### **Qualitative Assessment for Governance**

- **Governance Participation**: The introduction of veCRV, linking governance rights with token locking, likely enhanced governance engagement. While its hard to conclude this with direct data given that Curve was a relatively new protocol around that time and it generally takes a time for even the initial adoption to happen. veCRV's mechanism is designed to incentivize long-term commitment and active participation in governance decisions.
"""
)


# Unusual Activity Section
st.markdown("#### Unusual Activity")

st.markdown(
    "*Data Source: Dune Dashboard* ([Dune Dashboard](https://dune.com/encrypted_soul/mev-activity-on-curve))"
)

st.write(
    "In terms of the percentage of transactions on curve that are MEV transactions and the percentage of swaps that are MEV swaps, curve seems to be amongst the lowerst in comparison to other dexes. That said, even a 0.176% of the total swaps being related to MEV is a significant number. This is the historical trend since inception."
)
st.markdown("**MEV swaps and volume comparison across dexes**")
image_path = "./assets/mev_swaps_and_volume_across_dexes.png"
image = Image.open(image_path)
st.image(image)

st.write(
    "However, the following two graphs show that more recently the total number of MEV transactions and the volume of MEV transactions as decreased considerably for curve -"
)
st.markdown("**MEV swaps and volume comparison across dexes**")
image_path = "./assets/mev_swaps_and_transactions_curve.png"
image = Image.open(image_path)
st.image(image)

st.markdown(
    """
Regarding the impact on the protocol:

- **Wash Trading**: Can lead to misleading volume metrics, giving the impression of liquidity that isn't actually there.
- **Front-Running**: Erodes trust in the fairness of the protocol and can discourage genuine users from participating.
- **Pump-and-Dump**: Damages the protocol's reputation and can lead to severe price volatility.
"""
)

# Trading Volume VS Liquidity Section
st.subheader("Trading Volume VS Liquidity")
st.markdown("**Trading Volume vs TVL regression**")
image_path = "./assets/trading_volume_vs_tvl_regression.png"
image = Image.open(image_path)
st.image(image)

st.markdown(
    """
The plot above illustrates the regression analysis of trading volume versus Total Value Locked (TVL) in Curve Finance:

1. **Scatter Plot**: Each point represents a day's data, with TVL on the x-axis and trading volume on the y-axis. This visual representation shows how these two variables are distributed and their relationship.
2. **Regression Line**: The red line is the regression line, summarizing the average relationship between TVL and trading volume. It's calculated from the regression model and shows the expected value of trading volume for a given level of TVL.

### **Understanding the Analysis:**

- **R-squared (0.094)**: This value tells us that the model explains about 9.4 percent of the variability in trading volume. It's a measure of how well the model fits the data. While it indicates some level of fit, it also suggests that other factors, not included in this model, significantly influence trading volume. Think of the regression line like a trend line in a graph. It shows the general direction of the relationship between liquidity (TVL) and how much trading happens.
- **Coefficient (0.022 for TVL)**: This number indicates the change in trading volume for each unit increase in TVL. A positive coefficient suggests that as TVL increases, so does the trading volume, albeit at a relatively modest rate. The R-squared value is like a scorecard for how much of the change in trading volume can be explained just by looking at TVL. In this case, it's not a high score, meaning there are other factors out there that also affect how much trading is happening.
- **P-value**: The statistical significance of the TVL coefficient, being less than 0.05, confirms that TVL is a relevant factor in determining trading volume. It means the observed relationship is unlikely to be due to random chance. The positive relationship between TVL and trading volume suggests that when there's more money locked in Curve Finance (indicating more liquidity), there tends to be more trading activity. However, the effect is not very strong, indicating that liquidity is just one of the many factors influencing trading volumes.

In summary, while TVL is a significant factor affecting trading volume, it's not the only one. The analysis points to the complexity of the financial markets where multiple factors, some possibly not captured in this dataset, influence trading behavior.
"""
)

# Trading Volume Fluctuations Section
st.subheader("Trading Volume Fluctuations")

st.markdown("*Data Source: Flipside Crypto*")

# Displaying images for trading volume fluctuations
image_path = "./assets/trading_volume_by_day_of_the_week.png"
image = Image.open(image_path)
st.image(image)
st.write(
    "For the case of trading volume, the volume seems to pick up towards the end of the week starting from Wednesday and slows down during the weekend and picks back up from Monday."
)

image_path = "./assets/trading_volume_by_hour_of_the_day.png"
image = Image.open(image_path)
st.image(image)
st.write(
    "This graph shows that the trading volume reaches a small peak early UTC time around 9 AM and then another major peak later in the evening UTC time."
)

image_path = "./assets/trading_volume_by_day_of_the_month.png"
image = Image.open(image_path)
st.image(image)
st.write(
    "For the trend throughout the month, the trading volume seems to peak till the later part of the second week of the month and then we notice a downward trend."
)

# Bank of International Settlements Use Cases Section
st.subheader("Bank of International Settlements Use Cases")

st.markdown(
    "[Project Mariana](https://www.bis.org/about/bisih/topics/cbdc/mariana.htm), a proof of concept (PoC) for a global interbank market for spot foreign exchange (FX) featuring automated market-makers (AMMs) and wholesale central bank digital currencies (wCBDCs), demonstrates the technical feasibility of this new architecture. It leverages decentralized finance concepts to potentially simplify FX (foreign exchange) trading and settlement, with the aim of enhancing market efficiency and reducing settlement risk."
)

# Subsections for each use case
st.markdown(
    """
### **1. Suitability of Curve's AMM Design for Cross-border CBDC Projects:**

#### Problem:
Cross-border CBDC transactions face complexities due to different currencies, regulatory environments, and the need for efficient, secure, and transparent trading and settlement processes.

#### Curve's AMM Solution:
- **Smart Contract Flexibility**: Curve's AMM, built on smart contracts, offers flexibility in managing digital currencies, crucial for wCBDCs that operate across different national monetary systems.
- **Efficient Liquidity Management**: Curve's AMM design, particularly its stablecoin-focused liquidity pools, can provide more stable and efficient liquidity management, crucial for minimizing slippage in cross-border transactions involving multiple currencies.
- **Transparency and Security**: Curve's blockchain-based infrastructure ensures transparency and security, critical for maintaining trust in cross-border financial transactions involving central banks.

### **2. Enhancing Efficiency and Effectiveness of Cross-border CBDC Transactions:**

#### Problem:
Current cross-border transactions can be slow, lack transparency, and are prone to settlement risks, demanding a more efficient and risk-mitigated solution.

#### Curve's Solution:
- **Reduced Slippage and Better Price Discovery**: Curve's core technical innovation lies in the formula used to compute the exchange rate of assets holding the same value (for instance, USD Circle and USD Tether). It is, therefore, able to offer lower trading fees and slippage than its competitors, especially important in large volume trades typical of cross-border transactions.
- **Instant Settlement and Reduced Risk**: Utilizing smart contracts, Curve's AMM can provide instant settlement, reducing counterparty and settlement risks that are significant in current cross-border transactions.
- **Enhanced Liquidity**: Curve's efficient liquidity provision, especially for stablecoin-like assets, can be helpful in ensuring sufficient liquidity for cross-border trades, enhancing overall transaction efficiency.

### **3. Significance of Collaboration Between Central Banks and a DeFi Platform like Curve:**

#### Problem:
Central banks require innovative solutions to address the evolving needs of digital currencies while ensuring stability, security, and regulatory compliance.

#### Curve's Solution:
- **Innovative Liquidity and Pricing Models**: Curve's AMM design offers liquidity management and pricing models suitable for the high-value, low-volatility nature of CBDCs.
- **Expertise in Stablecoin Transactions**: Curve's expertise in stablecoin transactions can be invaluable in handling CBDCs, which share several characteristics with stablecoins.

### **4. Benefits and Challenges of Integrating Curve's AMM into the CBDC Ecosystem:**

#### Problem:
Integrating a DeFi solution like Curve's AMM into a central bank-regulated digital currency ecosystem poses challenges in terms of security, regulatory compliance, and liquidity management.

#### Curve's Solution:
- **Benefits**:
    - **Efficient Liquidity Pools**: Curve's AMM design, known for efficient liquidity pools, can provide a stable and efficient trading environment, essential for CBDCs.
    - **Innovative Risk Management**:  Curve's AMM model can offer risk management features through its liquidity provision and pricing mechanisms.
- **Challenges**:
    While Curve has demonstrated product-market-fit with native crypto VCs and its retail customers, adoption by regulated players will require protocols such as Curve to adapt their offerings and work with regulated entities.
"""
)
