
import pandas as pd
from datetime import datetime, timedelta
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import helper
from wordcloud import WordCloud
from helper import remove_emojis, remove_stopwords, stem_text, filter_words, help
from textblob import TextBlob
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots


# st.set_page_config(layout="wide")

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=600, background_color="black").generate(text)
    plt.figure(figsize=(10, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title("Word Cloud after Preprocessing")
    st.pyplot()

def get_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def process_date(df):
    # Convert 'created_at' column to datetime
    df['created_at'] = pd.to_datetime(df['created_at'])

    # Sort DataFrame by 'created_at'
    df.sort_values(by='created_at', inplace=True)

    # Count the number of tweets and retweets for each date
    df['Date'] = df['created_at'].dt.date
    tweet_counts = df.groupby('Date').size().reset_index(name='Total Tweets')
    retweet_counts = df.groupby('Date')['retweet_count'].sum().reset_index(name='Total Retweets')

    # Merge the two counts on 'Date'
    counts_df = pd.merge(tweet_counts, retweet_counts, on='Date')

    return counts_df

def extract(token, df):
    cols = [val for val in df.columns if token in val or 'Date' in val]
    return df[cols]
    
about_1 = f'''
`Illuvium` is among the `Largest CryptocCurrencies`, valued at over $ USD$ $96.37$. What sets it apart is it's `consistent price` of around $USD$ $263.2$, unlike competitors struggling to reach even $USD$ $1$. 

`But does Illuvium live up to the hype...?`

#### About Illuvium

`Illuvium`, a `Decentralized Gaming Ecosystem` on the `Ethereum Blockchain`, offers an `Open-World Fantasy` battle experience. Driven by `NFTs`, players `collect and trade unique creatures` `(Illuvials)` for battles, exploration, and potential rewards. The game `integrates DeFi elements`, combining a `Collectible NFT RPG` and `Auto-Battler` on the `Immutable X L2 Network`.

#### Roots and Building the Ecosystem

Founded by the `Warwick Brothers` in `September 2020`, Illuvium attracted a `team of experienced developers` and `raised funds` through multiple rounds. Illuvium successfully fuses `AAA-quality open-world RPG` with `blockchain technology`.

#### Illuvials

Illuvials, `Deadly Beasts` in the `Alien World`, possess `Hybrid Synergies` and `Unique Abilities`. These `4-dimensional-shading holographic NFTs` can be captured to `gain power` or `sold on exchanges` for crypto income.

#### Game Modes
'''
auto_battler = '''
#### Auto Battler

`Auto Battler` is a `multiplayer strategy game` where players `battle each other` using `automated units`. Illuvium's `Auto Battler` mode `differs from traditional Auto Battlers` by `replacing multiplayer with computer-controlled enemies`. This `unique approach` may `limit player engagement` and `reduce the game's appeal`.
'''
open_world = '''
#### Overworld

The `Overworld` is an `open-world environment` where players `explore the Illuvium world` and `collect resources`. The `Overworld` is `similar to other open-world games` and may `not offer a unique experience` to players.
'''
arena = '''
#### Arena

The `Arena` is a `multiplayer mode` where players `battle each other` using `Illuvials`. The `Arena` is `similar to other Auto Battlers` and may `not offer a unique experience` to players.
'''

investors = '''
#### Investors

|||
|---|---|
|**Lead Investors**|
|Framework Ventures|This `Venture Capital Firm` `specializing` in `blockchain` and `crypto` has been a `strong supporter` of Illuvium since its early days. They led two funding rounds, injecting $USD$ $5$ $Million$ in `March 2021` and another $USD$ $10$ $Million$ in `May 2023`. Their continued faith `highlights` `Illuvium's long-term potential`.
|**Other Notable Investors**||
|Polemos|This `Crypto-Focused VC Firm` invested $USD$ $2$ $Million$ in `February 2022`, demonstrating `confidence` in `Illuvium's ability to disrupt the gaming industry`.
|11 Other Institutional Investors|While `details remain undisclosed`, `Illuvium's total investor count` stands at $12$, indicating `broad institutional backing` for the project.
|**Types of Investors**|
|Venture Capital Firms|The `majority` of Illuvium's investors are prominent VCs operating in the blockchain and gaming space. This suggests their `belief in the project's ability to generate significant returns`.
|Individual Investors|While `details are scarce`, the project likely attracted `individual investors` through `token sales and community engagement`.
'''

revenue = '''
#### Revenue Generation

Illuvium `generates revenue` from 
* In-game fees `(Exchange Fees and Wagering Fees)`
* Illuvials `purchases` on the `IlluviDEX exchange`
* `DeFi staking mechanisms` that convert `in-game profits from ETH` to `synthetic Illuvium` (sILV), distributed fairly to staked ILV token holders.
'''
price_dist = '''
* **Lowest Price Range** : A `significant frequency bar` just above $USD$ $500$ at the beginning of the histogram suggests a `high occurrence of Illuvium prices` in the `lowest range (0-250 USD)`.
* **Diminishing Frequencies** : As `prices increase`, `frequency bars decrease rapidly`, notably in the `USD 250-500` range. This pattern continues, with progressively smaller bars for higher price ranges.
* **Sparse Occurrences Beyond 500 USD** : Beyond the $USD$ $500$ mark, `most bars display` very few occurrences, indicating a `scarcity of data points in higher price ranges`.
'''
moving_avg_30 = '''
The `price line exhibits significant volatility`, with a `sharp peak in the center of the graph` where the price spikes dramatically before falling. 
The `rolling average line is smoother`, representing the `average price over a 30-day period` and `reducing the impact of short-term fluctuations`.
'''
scatter = '''
#### Correlation Plot: Normalized Prices and Market Cap

The plot illustrates a positive correlation between two variables, with the `x-axis` denoted as "*Normalized Prices*" and the `y-axis` labeled as "*Normalized Market Cap*." The plotted points on the graph indicate a discernible upward trend, depicting a direct and proportional relationship between the normalized market capitalization and the normalized prices.

Furthermore, the scatter plot includes an inset legend that references "*Volume_normalized*" alongside a color gradient scale.
'''
ilv_price_mcap = '''
|||
|---|---|
|**Observations**|
|Price (Blue Line)| The `price fluctuates over time`, with `significant volatility observed`, particularly in two time periods where price peaks notably.
|Market Cap (Orange Dots)| The market capitalization follows a `trend similar` to the price, with significant fluctuations.
|Volume (Green Dots)| Volume shows `less variation` compared to the price and market cap, with `occasional spikes` aligning with price peaks.
|**Analysis**|
|Price and Market Cap|The highest peak for both price and market cap occurs shortly after the start of 2022, followed by a sharp decline and a period of lower values and reduced volatility.
||Toward the end of the observed period, both price and market cap exhibit an increasing trend with moderate volatility.
|Volume|Volume does not show extreme peaks but has spikes that sometimes correspond to changes in price and market cap, indicating reactive trading behavior.
'''

dily_active_address = '''
**Correlation between Price and User Activity:**
  - A spike in New and Active Addresses aligns with a Price peak around January 2022, suggesting a correlation between price movements and user engagement.

**Decline in New and Active Addresses:**
  - Despite Price fluctuations, there's a gradual decline in both New and Active Addresses over time. Zero Balance Addresses remain stable, indicating potential user inactivity or account abandonment.

**Intermittent Spikes in Activity:**
  - Even with a lower Price, intermittent spikes in user activity occur, possibly tied to specific events or external factors rather than consistent Price changes.


**Rise in Zero Balance Addresses:**
  - Towards the later timeline, there's an increase in Zero Balance Addresses, suggesting the creation of addresses not actively funded or utilized. This may reflect a shift in user behavior or market dynamics.
'''

trans = '''
- **Data Representation:**
  - The y-axis on the left depicts Volume in USD, reaching up to 600M (millions), while the right y-axis represents another scale, potentially price or another metric, with a maximum value of 1500.

- **Timeframe Representation:**
  - The x-axis spans from July 2021 to a date beyond July 2023, with data points approximately at monthly intervals.

- **Key Observations:**
  - A significant peak in both price and volume (USD and otherwise) is evident around the end of 2021 or the beginning of 2022.
  - Spikes in volume (USD) correspond with notable changes in price, suggesting a correlation between these two metrics.
  - The red line, likely indicating the count of transactions ('Transc'), remains relatively flat and close to the bottom of the graph. However, it also has a peak around the same time as the volume and price peaks.
'''

etherum_ = '''
- **Price Fluctuations:**
  - Both Ethereum and Illuvium exhibit significant volatility, characterized by multiple peaks and troughs.

- **Ethereum's Price Trends:**
  - Ethereum's price shows sharp increases and subsequent declines, with a notable peak near 2021, followed by a decline and subsequent rise.

- **Illuvium's Price Dynamics:**
  - Illuvium's price data, starting from around 2021, displays a dramatic spike at one point followed by a sharp decline.
'''

voli = '''
  - The blue line represents "Volatility," plotted on the left vertical axis. Significant spikes in January 2022 indicate a period of very high volatility, followed by a decrease and stabilization at a lower level.
  - The black line represents "Price," plotted against the right vertical axis. Notable fluctuations, including a peak around January 2022, seem to correlate with the volatility spike. Subsequently, the price declines significantly before gradually increasing, possibly indicating a recovery or stabilization phase post-July 2023.
'''

price_corr_tweet = '''
* Tweet Count : The tweet count exhibits a `discernible upward trend` starting from mid-2023. 
`Significant spikes` are observed, indicating `heightened social media activity` and `increased interest` in Illuvium during this period.

* Illuvium Price : The frequency of Illuvium price data points follows a `steady increase from March to mid-July`. A `notable drop occurs post-mid-July`, followed by a `sharp rise in November` and `December 2023`, reaching its `peak frequency` at the `year's end`.

* Price & Social Media Correlation : While a `straightforward correlation` is not `evident`, `noteworthy peaks` in `tweet volume occasionally align` with `increased frequency` in Illuvium price data points, particularly towards the year's end.
'''

sentiment_corr = '''
* Overall Sentiment : The `majority of sentiment scores cluster around 0.25`, indicating a `generally slight positive sentiment` across the tweets.

* Strong Sentiment Peaks : `Fewer tweets show strong positive or negative sentiment` (scores near 1 or -1). Notably, there is a `distinct peak around the -0.75 area`, suggesting a `concentration of tweets with strongly negative sentiments`.

* Skewed Distribution: The `sentiment distribution is asymmetrical`, favoring the `positive side`. This indicates a `higher prevalence of tweets with positive sentiment` compared to negative sentiment.
'''

ilv_axs_weth = '''
#### Cryptocurrency Price Movements Over Time

The graph displays the price movements of three assets over time, with each cryptocurrency represented by a different colored line (blue for *ILV*, green for *AXS*, and orange for *WETH*).

The vertical axis of the graph is labeled "*Price*," indicating the value of the cryptocurrencies, while the horizontal axis is labeled "*Date*," although the format of the dates may not be standard. The lines on the graph illustrate the changes in price for each cryptocurrency over the represented time period.
'''

wc = '''
#### Analysis of Prominent Terms

Prominent terms such as `game`, `team`, `update`, `play`, and `PvP` (player versus player) indicate a strong focus on gaming elements and player engagement. Additionally, the presence of words like `live`, `share`, `new`, and `first wave` suggests an active community response, possibly related to a new game release or significant updates.

Furthermore, the occurrence of terms such as `discord`, `link`, `beta`, and `collect` points to discussions around community platforms, beta testing, and in-game actions, reflecting an environment where player interaction, community involvement, and game development are central themes.
'''

pair = '''
### Token Performance Correlation Analysis

The correlation heatmap for the token's performance indicates varying degrees of correlation between different metrics, such as `staking`, `liquidity pools`, and `gaming activities`. Positive correlations between certain metrics might suggest interconnectedness or shared influences, while negative correlations could imply divergent movements or counteracting effects.

The matrix of plots further illustrates the distribution and trends of the token's performance metrics over time. It provides insights into the relationships between different variables, potentially highlighting patterns or anomalies in the data.
'''

future_1 = '''
## Iluvium: Navigating Opportunities and Challenges in Blockchain-Based Gaming
'''
market = '''
#### Market Landscape
One key factor contributing to `Iluvium's` potential success is the burgeoning popularity of `blockchain-based gaming`. With the global gaming industry projected to reach `$200 billion by 2023`, the incorporation of blockchain technology is anticipated to propel substantial growth. `Iluvium's` distinctive approach positions it strategically to emerge as a leader in this evolving market.
'''
team = '''
#### Team Dynamics
The expertise of `Iluvium's` team, comprised of seasoned `blockchain developers`, `game designers`, and `marketing professionals`, adds a layer of assurance to the platform's success. This diverse skill set positions the team well for navigating the complexities of the `blockchain gaming landscape`.
'''
future = '''
#### Community Traction
`Iluvium` has already gained considerable traction in both the `blockchain` and `gaming communities`. The platform's `initial coin offering (ICO)` sold out in a mere `30 minutes`, underscoring strong investor interest. Support from prominent `blockchain investors` and `influencers` further validates `Iluvium's` potential impact in the space.

#### Potential Challenges
Despite promising prospects, `Iluvium` faces potential challenges on its journey. `Regulatory uncertainties` surrounding `blockchain-based gaming` pose a significant hurdle. Governments globally are grappling with the regulatory framework for cryptocurrency and blockchain technology, which could impact `Iluvium's` growth trajectory.

`Competition` from other `blockchain-based gaming platforms` is another challenge. While `Iluvium's` innovative approach to `DeFi` and `NFTs` distinguishes it, the competitive landscape remains robust, with numerous projects vying for user and investor attention.

#### Conclusion
`Iluvium's` future appears promising, contingent upon its ability to navigate challenges and capitalize on opportunities. Continued innovation, community building, and adept management of regulatory dynamics will be pivotal in establishing `Iluvium` as a major player in the dynamic and evolving `blockchain-based gaming industry`.
'''

helper.set_background('Assets/Background/ILV Background.jpg')


def main():

    st.image('Assets/Logo/ILV Logo.webp' , width = 100)

    st.title("Illuvium Price Analysis")
    st.markdown('By Chirag Chetnani and Ayush Singhal') # Planned to be palced as footer
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.markdown(about_1)
    st.image('Assets/Characs/Illuvial.webp' , width = 200)

    col_1 , col_2 , col_3 = st.columns(3)

    col_1.markdown(auto_battler)
    col_1.image('Assets/World/ILV Auto.jpg' , width = 200)

    col_2.markdown(open_world)
    col_2.image('Assets/World/ILV Over.jpg' , width = 200)

    col_3.markdown(arena)
    col_3.image('Assets/World/ILV Arena.jpg' , width = 200)

    st.image('Assets/Tweets/Karein Warwick 2.png')

    st.markdown(investors)
    st.image('Assets/About/ILV Money.png' , width = 800)

    st.markdown(revenue)
    st.image('Assets/About/ILV Revenue Generation.png' , width = 800)

    # Fetch Illuvium data
    illuvium_df = pd.read_csv('ilv.csv')
    axs = pd.read_csv('axs.csv')
    weth = pd.read_csv('weth.csv')
    eth = pd.read_csv('eth.csv')
    ilv_history = pd.read_csv('ilv_history.csv')

    # Display first 10 rows
    # st.subheader("Illuvium Price Data (First 10 rows)")
    # st.dataframe(illuvium_df.head(10))

    # Display summary statistics
    st.subheader("Summary Statistics")
    st.write(illuvium_df[illuvium_df.columns[2:]].describe())

    # Plot Illuvium Price Over Time
    st.subheader("Illuvium Price Over Time")
    illuvium_df.index = pd.to_datetime(illuvium_df.index, unit='ms')
    axs.index = pd.to_datetime(axs.index, unit='ms')
    weth.index = pd.to_datetime(weth.index, unit='ms')
    st.line_chart(illuvium_df['prices'])

    st.markdown('The line on the graph shows a significant peak in the middle, indicating a substantial increase in price followed by a decline and then leveling off.')

    # Histogram of Illuvium Prices
    st.subheader("Distribution of Illuvium Prices")
    
    plt.hist(illuvium_df['prices'], bins=30, edgecolor='black')
    plt.xlabel('Price (USD)')
    plt.ylabel('Frequency')
    st.pyplot()

    st.markdown(price_dist)

    # Plot Illuvium Daily Returns
    st.subheader("Illuvium Daily Returns")
    illuvium_df['Daily Returns'] = illuvium_df['prices'].pct_change()
    st.line_chart(illuvium_df['Daily Returns'])

    st.markdown('This information suggests that Illuvium has experienced notable fluctuations in its daily returns over the observed time period.')

    # Plot Illuvium Price with 30-Day Rolling Average
    st.subheader("Illuvium Price with 30-Day Rolling Average")
    illuvium_df['Rolling Average'] = illuvium_df['prices'].rolling(window=30).mean()
    st.line_chart(illuvium_df[['prices', 'Rolling Average']])

    st.markdown(moving_avg_30)

    # scatter plot
    # Normalize data
    illuvium_df['prices_normalized'] = (illuvium_df['prices'] - min(illuvium_df['prices'])) / (max(illuvium_df['prices']) - min(illuvium_df['prices']))
    illuvium_df['MCap_normalized'] = (illuvium_df['MCap'] - min(illuvium_df['MCap'])) / (max(illuvium_df['MCap']) - min(illuvium_df['MCap']))
    illuvium_df['Volume_normalized'] = illuvium_df['Volume'] / 10**8

    # Scatter plot
    sns.set(style="whitegrid")  # Set the style to whitegrid for streamline appearance

    # Streamlit app
    st.markdown('## Scatter Plot')

    # Scatter plot for ILV
    st.subheader('Scatter Plot for ILV')
    fig_ilv, ax_ilv = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x='prices_normalized', y='MCap_normalized', hue='Volume_normalized', data=illuvium_df, ax=ax_ilv)
    plt.xlabel('Normalized Prices')
    plt.ylabel('Normalized Market Cap')
    plt.title('ILV Scatter Plot')
    st.pyplot(fig_ilv)

    st.markdown(scatter)

    # Convert 'Time' to datetime format
    illuvium_df['Time'] = pd.to_datetime(illuvium_df['Time'], unit='ms')

    # Streamlit app
    st.markdown('## Iluvium Price, Market Cap, and Volume Over Time')

    # Plotting all three columns in a single plot
    fig, ax = plt.subplots(figsize=(12, 8))

    ax.plot(illuvium_df['Time'], illuvium_df['prices'], label='Price', marker='o')
    ax.plot(illuvium_df['Time'], illuvium_df['MCap'], label='Market Cap', marker='o')
    ax.plot(illuvium_df['Time'], illuvium_df['Volume'], label='Volume', marker='o')

    ax.set_xlabel('Time')
    ax.set_ylabel('Values')
    ax.legend()
    st.markdown(ilv_price_mcap)

    # Display the plot using Streamlit
    st.pyplot(fig)

    st.markdown('## Historical In/Out of the Money')
    # Convert DateTime to datetime format
    ilv_history['DateTime'] = pd.to_datetime(ilv_history['DateTime'])

    # Create the plot
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=ilv_history['DateTime'], y=ilv_history['In'], fill='tozeroy', name='In'), secondary_y=False)
    fig.add_trace(go.Scatter(x=ilv_history['DateTime'], y=ilv_history['At'], fill='tozeroy', name='At'), secondary_y=False)
    fig.add_trace(go.Scatter(x=ilv_history['DateTime'], y=ilv_history['Out'], fill='tozeroy', name='Out'), secondary_y=False)
    fig.add_trace(go.Scatter(x=ilv_history['DateTime'], y=ilv_history['Price'], name='Price', line=dict(color='white')), secondary_y=True)
    fig.layout.yaxis2.showgrid = False

    # Display the plot in Streamlit
    st.plotly_chart(fig)

    ilv_active_adress = pd.read_csv("ilv_active_adress.csv")

    # Convert 'DateTime' column to datetime format
    ilv_active_adress['DateTime'] = pd.to_datetime(ilv_active_adress['DateTime'])

    # Streamlit app title
    st.markdown(' ## Daily Active Addresses')

    # Create the plot using Plotly
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=ilv_active_adress['DateTime'], y=ilv_active_adress['New Addresses'], fill='tozeroy', name='New Addresses'), secondary_y=False)
    fig.add_trace(go.Scatter(x=ilv_active_adress['DateTime'], y=ilv_active_adress['Active Addresses'], fill='tozeroy', name='Active Addresses'), secondary_y=False)
    fig.add_trace(go.Scatter(x=ilv_active_adress['DateTime'], y=ilv_active_adress['Zero Balance Addresses'], fill='tozeroy', name='Zero Balance Addresses'), secondary_y=False)
    fig.add_trace(go.Scatter(x=ilv_active_adress['DateTime'], y=ilv_active_adress['Price'], name='Price', line=dict(color='white')), secondary_y=True)
    fig.layout.yaxis2.showgrid = False

    # Display the plot in Streamlit
    st.plotly_chart(fig)
    st.markdown(dily_active_address)

    ilv_transaction = pd.read_csv("Transc.csv")

# Convert 'Date' column to datetime format
    ilv_transaction['Date'] = pd.to_datetime(ilv_transaction['Date'])

    # Streamlit app title
    st.markdown(' ## Transaction Data')

    # Create the plot using Plotly
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=ilv_transaction['Date'], y=ilv_transaction['Volume USD'], fill='tozeroy', name='Volume USD'), secondary_y=False)
    fig.add_trace(go.Scatter(x=ilv_transaction['Date'], y=ilv_transaction['Price'], name='Price', line=dict(color='white')), secondary_y=True)
    fig.add_trace(go.Scatter(x=ilv_transaction['Date'], y=ilv_transaction['Volume'], fill='tozeroy', name='Volume'), secondary_y=False)
    fig.add_trace(go.Scatter(x=ilv_transaction['Date'], y=ilv_transaction['Transc'], fill='tozeroy', name='Transc'), secondary_y=False)
    fig.layout.yaxis2.showgrid = False

# Display the plot in Streamlit
    st.plotly_chart(fig)
    st.markdown(trans)
    

    # Display the plot using Streamlit
    # # Correlation Matrix
    # st.subheader("Correlation Matrix")
    # st.write(illuvium_df.corr())
    # st.pyplot(sns.heatmap(illuvium_df.corr(), annot=True, cmap='coolwarm', fmt=".2f"))
    
    ################# Compare all ##############################################

    eth['Date'] = pd.to_datetime(eth['DateTime'])
    # illuvium_df['Date'] = pd.to_datetime(illuvium_df['Time'], unit='ms')

    # Streamlit app
    st.markdown('## Ethereum vs Iluvium Prices Over Time')

    # Plotting the data
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(eth['Date'], eth['Price'], label='Ethereum', marker='o')
    ax.plot(illuvium_df['Time'], illuvium_df['prices'], label='Iluvium', marker='o')

    # Adding labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Price (USD)')
    ax.set_title('Ethereum vs Iluvium Prices Over Time')
    ax.legend()

    # Display the plot using Streamlit
    st.pyplot(fig)
    st.markdown(etherum_)
    
    sns.set(style="whitegrid")  # Set the style to whitegrid for streamline appearance

    # Streamlit app
    st.markdown('## Price Trends')

    # Line plot for all assets
    st.subheader('Price Trends for ILV, AXS, and WETH')
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plotting lines
    sns.lineplot(data=illuvium_df, x=illuvium_df.index, y='prices', label='ILV', color='blue', ax=ax)
    sns.lineplot(data=axs, x=axs.index, y='prices', label='AXS', color='green', ax=ax)
    sns.lineplot(data=weth, x=weth.index, y='prices', label='WETH', color='orange', ax=ax)

    # Customize plot
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    st.pyplot(fig)

    st.markdown(ilv_axs_weth)

    # Load data using the helper function
    df = help('illuvium.csv')

  # Extract relevant data
    ilv = extract('ILV', df)
    axs = extract('AXS', df)

    # Reshape data to long form for Plotly Express
    ilv_long = ilv.melt(id_vars=['Date'], var_name='Metric', value_name='Value')
    axs_long = axs.melt(id_vars=['Date'], var_name='Metric', value_name='Value')

    # Plot ILV data using Plotly Express
    fig_ilv = px.line(ilv_long, x='Date', y='Value', color='Metric', title='Dynamic Price Plot Over Time',
                      labels={'Value': 'Price'})
    fig_ilv.update_xaxes(title_text='Date')
    fig_ilv.update_yaxes(title_text='Price')
    st.plotly_chart(fig_ilv)

    # Plot AXS data using Plotly Express
    fig_axs = px.line(axs_long, x='Date', y='Value', color='Metric', title='AXS Price Plot Over Time',
                      labels={'Value': 'Price'})
    fig_axs.update_xaxes(title_text='Date')
    fig_axs.update_yaxes(title_text='Price')
    st.plotly_chart(fig_axs)

    # Your existing code for correlation heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(ilv.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap for ILV Tokens')
    st.pyplot()

    # Your existing code for pairplot
    sns.pairplot(ilv, vars=ilv.columns[:4])
    plt.suptitle('Pairplot for ILV Tokens', y=1.02)
    st.pyplot()

    st.markdown(pair)

    # # Your existing code for ILV returns histogram
    # plt.figure(figsize=(10, 6))
    # sns.histplot(ilv.pct_change().dropna()['Illuvium.8_Gaming_ethereum-staking_Tokens(USD)_ILV'], bins=30, kde=True)
    # plt.title('Distribution of ILV Returns')
    # plt.xlabel('Daily Returns')
    # plt.ylabel('Frequency')
    # st.pyplot()

    # Your existing code for ILV description
    st.write(ilv.describe())



    df = pd.read_csv('TwExportly_illuviumio_tweets_2023_12_15 (1).csv')
    st.markdown("## Illuvium Tweet Analysis")

    # Process date and count tweets
    counts_df = process_date(df)

    # Display tweet counts by date
    st.subheader("Tweet Counts by Date")
    st.dataframe(counts_df)

    # Merge both dataframes on 'Date'
    merged_df = pd.merge(counts_df, df, on='Date', how='inner')

    # Create a dual-axis plot
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plot the tweet count as a line on the first axis
    ax1.plot(merged_df['Date'], merged_df['Total Tweets'], label='Tweet Count', color='blue')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Tweet Count', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    # Create a second y-axis for the price histogram
    ax2 = ax1.twinx()
    ax2.hist(merged_df['Date'], bins=30, alpha=0.7, color='green', label='Illuvium Price')

    # Set labels for the second y-axis
    ax2.set_ylabel('Frequency', color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    # Show legend
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    st.markdown(price_corr_tweet)

    # Show the plot
    plt.title('Tweet Count (Line) and Illuvium Price (Histogram) Over Time')
    st.pyplot()
    
    ilv_volatile = pd.read_csv('ilv_volatile.csv')

    # Convert 'DateTime' column to datetime format
    ilv_volatile['DateTime'] = pd.to_datetime(ilv_volatile['DateTime'])

    # Streamlit app title
    st.markdown('## Volatility and Price')

    # Create the plot using Plotly
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=ilv_volatile['DateTime'], y=ilv_volatile['Volatility'], fill='tozeroy', name='Volatility'), secondary_y=False)
    fig.add_trace(go.Scatter(x=ilv_volatile['DateTime'], y=ilv_volatile['Price'], name='Price', line=dict(color='white')), secondary_y=True)
    fig.layout.yaxis2.showgrid = False

    # Display the plot in Streamlit
    st.plotly_chart(fig)
    st.markdown(voli)

    # Extract the 'text' column
    text_list = list(df['text'])

    # Combine all text into a single string
    combined_text = ' '.join(map(str, text_list))

    # Preprocess the text
    text_without_emojis = remove_emojis(combined_text)
    text_without_stopwords = remove_stopwords(text_without_emojis)
    stemmed_text = stem_text(text_without_stopwords)
    filtered_text = filter_words(stemmed_text)

    # Generate word cloud
    st.subheader("Word Cloud")
    generate_wordcloud(filtered_text)

    st.markdown(wc)

    # Apply sentiment analysis to each tweet
    df['Sentiment'] = df['text'].apply(get_sentiment)

    # Plot the sentiment distribution
    st.subheader("Sentiment Distribution")
    plt.figure(figsize=(8, 6))
    df['Sentiment'].hist(bins=20, edgecolor='black', alpha=0.7)
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment Polarity')
    plt.ylabel('Frequency')
    st.pyplot()

    st.markdown(sentiment_corr)

   # st.markdown("<img src = 'https://pbs.twimg.com/media/GBeCXPnXsAAyFdo?format=png&name=small' width = 400>")
    # st.markdown("<img src = 'https://pbs.twimg.com/media/GAo1h6DbYAAFQ1X?format=jpg&name=large' width = 400>")

    st.markdown(future_1)

    st.markdown(market)
    st.image('Assets/Market/GBC.jpg' , width = 500)
    st.image('Assets/Market/US.png')

    st.markdown(team)
    col_1 , col_2 , col_3 , col_4 , col_5 = st.columns(5)
    col_1.markdown('#### Karien Warwick')
    col_1.image('Assets/Team/Karien Warwick.jpg' , width = 100)
    col_2.markdown('#### Aron Warwick')
    col_2.image('Assets/Team/Aron Warwick.jpeg' , width = 100)
    col_3.markdown('#### Grant Warwick')
    col_3.image('Assets/Team/Grant Warwick.jpeg' , width = 100)
    col_4.markdown('#### John Averly')
    col_4.image('Assets/Team/John Averly.jpeg' , width = 100)
    col_5.markdown('#### Danny Wilson')
    col_5.image('Assets/Team/Danny Wilson.jpg' , width = 100)

    st.markdown(future)


    # plot_price_and_tweet_histogram(illuvium_df, counts_df)

if __name__ == "__main__":
    main()
