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
# def plot_price_and_tweet_histogram(price_data, counts_data):
#     # Plot 'Price' data
#     plt.figure(figsize=(10, 6))
#     plt.plot(price_data.index, price_data['Price'], label='Illuvium Price', color='blue')
#     plt.xlabel('Date')
#     plt.ylabel('Price (USD)')
#     plt.title('Illuvium Price Over Time')
#     plt.legend()
#     st.pyplot()

#     # Plot histogram of tweet counts
#     plt.figure(figsize=(10, 6))
#     plt.bar(price_data.index, counts_data['Total Tweets'], color='green', alpha=0.7)
#     plt.xlabel('Date')
#     plt.ylabel('Tweet Count')
#     plt.title('Tweet Count Histogram Over Time')
#     st.pyplot()


# import plotly.express as px

# def extract(token) :

#     data = requests.get(f'https://api.coingecko.com/api/v3/coins/{token}/market_chart?vs_currency=USD&days=max').json()
#     open_close = requests.get(f'https://api.coingecko.com/api/v3/coins/{token}/ohlc?vs_currency=usd&days=max').json()

#     if 'error' in data.keys() : warnings.warn('Token Not available')
#     else :

#         prices = pd.DataFrame(data['prices'] , columns = ['Time' , 'Price'])
#         mcap = pd.DataFrame(data['market_caps'] , columns = ['Time' , 'MCap'])
#         volume = pd.DataFrame(data['total_volumes'] , columns = ['Time' , 'Volume'])

#         open_close = pd.DataFrame(open_close , columns = ['Time' , 'Open' , 'High' , 'Low' , 'Close'])

#         prices = prices.merge(mcap)
#         prices = prices.merge(volume)
#         prices = prices.merge(open_close , how = 'outer')

#         return prices

#     return None

# Function to fetch Illuvium price data
# def fetch_illuvium_data():
#     end_date = datetime.now()
#     start_date = end_date - timedelta(days=730)  # Last two years
#     url = f'https://api.coingecko.com/api/v3/coins/illuvium/market_chart?vs_currency=USD&days=max'
#     response = requests.get(url)
#     data = response.json()
#     prices = data["prices"]
#     return pd.DataFrame(prices, columns=["Date", "Price"]).set_index("Date")

about_1 = f'''
`Illuvium` is among the `Largest CryptocCurrencies`, valued at over {str('$')}{float(96.37)}$. What sets it apart is its `consistent price` of around {str('$')}{float(263.2)}$, unlike competitors struggling to reach $1$. 

`But does Illuvium live up to the hype...?`

#### About Illuvium

`Illuvium`, a `Decentralized Gaming Ecosystem` on the `Ethereum Blockchain`, offers an `Open-World Fantasy` battle experience. Driven by `NFTs`, players `collect and trade unique creatures` (Illuvials) for battles, exploration, and potential rewards. The game `integrates DeFi elements`, combining a `Collectible NFT RPG` and `Auto-Battler` on the `Immutable X L2 Network`.

#### Roots and Building the Ecosystem

Founded by the `Warwick Brothers` in `September 2020`, Illuvium attracted a `team of experienced developers` and `raised funds` through multiple rounds. Illuvium successfully fuses `AAA-quality open-world RPG` with `blockchain technology`.

#### Illuvials

Illuvials, `Deadly Beasts` in the `Alien World`, possess `Hybrid Synergies` and `Unique Abilities`. These `4-dimensional-shading holographic NFTs` can be captured to `gain power` or `sold on exchanges` for crypto income.

#### World/Modes

`Illuvium` features three interactive `AAA Games`: 

* Auto Battler - Illuvium's `departure` from the `multiplayer setup` in `AutoBattler`, opting for `computer-controlled enemies`, may lead to `player boredom`. Competing games like `League of Legends` offer more dynamic experiences.
* Overworld (monster world) - The `open-world` concept in Illuvium `may struggle` due to `perceived emptiness`, offering `limited engagement` beyond resource collection and crafting, reflecting a diminishing interest in such gameplay dynamics.
* Arena (arena) - This mode `replicates AutoBattler` with a `multiplayer` component but lacks the innovation needed to stand out.

#### Revenue Generation

Illuvium `generates revenue` from 
* In-game fees `(Exchange Fees and Wagering Fees)`
* Illuvials `purchases` on the `IlluviDEX exchange`
* `DeFi staking mechanisms` that convert `in-game profits from ETH` to `synthetic Illuvium` (sILV), distributed fairly to staked ILV token holders.

'''

price_corr_tweet = '''

* Tweet Count : The tweet count exhibits a `discernible upward trend` starting from mid-2023. 
`Significant spikes` are observed, indicating `heightened social media activity` and `increased interest` in Illuvium during this period.

* Illuvium Price : The frequency of Illuvium price data points follows a `steady increase from March to mid-July`. A `notable drop occurs post-mid-July`, followed by a `sharp rise in November` and `December 2023`, reaching its `peak frequency` at the `year's end`.

* Price & Social Media Correlation : While a `straightforward correlation` is not `evident`, `noteworthy peaks` in `tweet volume occasionally align` with `increased frequency` in Illuvium price data points, particularly towards the year's end.
'''

moving_avg_30 = '''
The `price line exhibits significant volatility`, with a `sharp peak in the center of the graph` where the price spikes dramatically before falling. 
The `rolling average line is smoother`, representing the `average price over a 30-day period` and `reducing the impact of short-term fluctuations`.
'''

sentiment_corr = '''

* Overall Sentiment : The `majority of sentiment scores cluster around 0.25`, indicating a `generally slight positive sentiment` across the tweets.

* Strong Sentiment Peaks : `Fewer tweets show strong positive or negative sentiment` (scores near 1 or -1). Notably, there is a `distinct peak around the -0.75 area`, suggesting a `concentration of tweets with strongly negative sentiments`.

* Skewed Distribution: The `sentiment distribution is asymmetrical`, favoring the `positive side`. This indicates a `higher prevalence of tweets with positive sentiment` compared to negative sentiment.
'''

price_dist = '''

* Lowest Price Range : A `significant frequency ba`r just above `500` at the beginning of the histogram suggests a `high occurrence of Illuvium prices` in the `lowest range (0-250 USD)`.
* Diminishing Frequencies : As `prices increase`, `frequency bars decrease rapidly`, notably in the 250-500 USD range. This pattern continues, with progressively smaller bars for higher price ranges.
* Sparse Occurrences Beyond 500 USD : Beyond the 500 USD mark, `most bars display` very few occurrences, indicating a scarcity of data points in higher price ranges.
'''

future = '''
## Iluvium: Navigating Opportunities and Challenges in Blockchain-Based Gaming

#### Market Landscape
One key factor contributing to `Iluvium's` potential success is the burgeoning popularity of `blockchain-based gaming`. With the global gaming industry projected to reach `$200 billion by 2023`, the incorporation of blockchain technology is anticipated to propel substantial growth. `Iluvium's` distinctive approach positions it strategically to emerge as a leader in this evolving market.

#### Team Dynamics
The expertise of `Iluvium's` team, comprised of seasoned `blockchain developers`, `game designers`, and `marketing professionals`, adds a layer of assurance to the platform's success. This diverse skill set positions the team well for navigating the complexities of the `blockchain gaming landscape`.

#### Community Traction
`Iluvium` has already gained considerable traction in both the `blockchain` and `gaming communities`. The platform's `initial coin offering (ICO)` sold out in a mere `30 minutes`, underscoring strong investor interest. Support from prominent `blockchain investors` and `influencers` further validates `Iluvium's` potential impact in the space.

#### Potential Challenges
Despite promising prospects, `Iluvium` faces potential challenges on its journey. `Regulatory uncertainties` surrounding `blockchain-based gaming` pose a significant hurdle. Governments globally are grappling with the regulatory framework for cryptocurrency and blockchain technology, which could impact `Iluvium's` growth trajectory.

`Competition` from other `blockchain-based gaming platforms` is another challenge. While `Iluvium's` innovative approach to `DeFi` and `NFTs` distinguishes it, the competitive landscape remains robust, with numerous projects vying for user and investor attention.

#### Conclusion
`Iluvium's` future appears promising, contingent upon its ability to navigate challenges and capitalize on opportunities. Continued innovation, community building, and adept management of regulatory dynamics will be pivotal in establishing `Iluvium` as a major player in the dynamic and evolving `blockchain-based gaming industry`.

'''


scatter = '''
#### Correlation Plot: Normalized Prices and Market Cap

The plot illustrates a positive correlation between two variables, with the `x-axis` denoted as "*Normalized Prices*" and the `y-axis` labeled as "*Normalized Market Cap*." The plotted points on the graph indicate a discernible upward trend, depicting a direct and proportional relationship between the normalized market capitalization and the normalized prices.

Furthermore, the scatter plot includes an inset legend that references "*Volume_normalized*" alongside a color gradient scale.
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



helper.set_background('ilv.jpg')

# Streamlit app
def main():
    st.title("Illuvium Price Analysis")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    # Fetch Illuvium data
    illuvium_df = helper.extract('illuvium')
    axs = helper.extract('axie-infinity')
    weth = helper.extract('weth')

    st.markdown(about_1)

    # Display first 10 rows
    st.subheader("Illuvium Price Data (First 10 rows)")
    st.dataframe(illuvium_df.head(10))

    # Display summary statistics
    st.subheader("Summary Statistics")
    st.write(illuvium_df.describe())

    # Plot Ethereum Price Over Time
    st.subheader("Ethereum Price Over Time")
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
    st.title('Scatter Plot')

    # Scatter plot for ILV
    st.subheader('Scatter Plot for ILV')
    fig_ilv, ax_ilv = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x='prices_normalized', y='MCap_normalized', hue='Volume_normalized', data=illuvium_df, ax=ax_ilv)
    plt.xlabel('Normalized Prices')
    plt.ylabel('Normalized Market Cap')
    plt.title('ILV Scatter Plot')
    st.pyplot(fig_ilv)

    st.markdown(scatter)


    # # Correlation Matrix
    # st.subheader("Correlation Matrix")
    # st.write(illuvium_df.corr())
    # st.pyplot(sns.heatmap(illuvium_df.corr(), annot=True, cmap='coolwarm', fmt=".2f"))
    
    ################# Compare all ##############################################
    sns.set(style="whitegrid")  # Set the style to whitegrid for streamline appearance

    # Streamlit app
    st.title('Price Trends')

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


    # # market analysis using candle stick
    # st.title("Illuvium Price Analysis")

    # # Display first 10 rows
    # st.subheader("Illuvium Price Data (First 10 rows)")
    # st.dataframe(illuvium_df.head(10))

    # # Candlestick chart
    # st.subheader("Illuvium Candlestick Chart")
    # fig = px.candlestick(illuvium_df, x=illuvium_df.index, open=illuvium_df['Price'], high=illuvium_df['Price'],
    #                      low=illuvium_df['Price'], close=illuvium_df['Price'], title='Illuvium Candlestick Chart')
    # fig.update_xaxes(type='category')  # Make sure the x-axis is treated as categorical
    # st.plotly_chart(fig)
    # Load the CSV file
    df = pd.read_csv('TwExportly_illuviumio_tweets_2023_12_15 (1).csv')
    st.title("Illuvium Tweet Analysis")

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

    st.markdown(future)

    # plot_price_and_tweet_histogram(illuvium_df, counts_df)

if __name__ == "__main__":
    main()
