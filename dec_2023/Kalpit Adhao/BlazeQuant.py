#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import yfinance as yf
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
# import data
from streamlit_image_comparison import image_comparison
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np
theme_plotly = None
from streamlit_player import st_player
st.set_option('deprecation.showPyplotGlobalUse', False)


# In[99]:


def home():
    from streamlit_player import st_player

    st.header("About Injective")
    st.write("Injective is an open, interoperable blockchain optimized for DeFi applications. Injective is smart contracts-enabled and utilizes a Tendermint PoS consensus mechanism. INJ is the native token that enables community members to participate in governance, validation, burn auctions and more.")
    st.subheader("What is Injective?")
    st_player("https://www.youtube.com/watch?v=4l8jiMOzR80")
    st.write("Injective (INJ) is a layer-one blockchain that aims to power the next generation of decentralized finance (DeFi) applications. These applications may include decentralized spot and derivatives exchanges, prediction markets, and lending protocols. Injective strives to provide core financial infrastructure primitives that applications can leverage, such as a fully decentralized on-chain orderbook. It also aims to support all forms of financial markets, including spot, perpetual, futures, and options, all fully on-chain. The blockchain is compatible with Ethereum, IBC-enabled blockchains, and non-EVM chains like Solana. Injective is built with the Cosmos SDK and uses a Tendermint-based Proof-of-Stake consensus mechanism, which allows for instant transaction finality and high performance.")
    st.subheader("How does Injective work?")
    st.write("Injective operates using a Tendermint-based Proof-of-Stake (PoS) consensus mechanism, which provides instant transaction finality and the ability to sustain high performance. It also features a decentralized cross-chain bridging infrastructure, making it compatible with Ethereum, IBC-enabled blockchains, and non-EVM chains such as Solana. Injective's core exchange module aims to include an advanced on-chain order book and matching engine for spot, perpetual, futures, and options markets. It also aims to offer resistance to Miner-Extractable Value (MEV) through frequent batch auction order matching, and strives to have zero gas fees for users. Smart contracts are implemented on Injective through CosmWasm, allowing for multi-chain smart contract transactions to occur seamlessly.")
    st.subheader("What are the potential use cases for Injective?")
    st.write("Injective aims to provide a platform for a wide range of DeFi applications. It offers a robust infrastructure and financial primitives such as an on-chain orderbook, which can be leveraged to build decentralized spot and derivatives exchanges, prediction markets, lending protocols, and more. The INJ token, Injective's native utility token, is used across a diverse range of functions such as protocol governance, dApp value capture, PoS security, developer incentives, and staking. Injective also aims to support a diverse array of trading and yield generation activities across distinct layer-1 blockchain networks such as Cosmos and Ethereum.")
    st.subheader("History of Injective")
    st.header("")
    intervals=["1d","1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "5d", "1wk", "1mo", "3mo"]
    interval=st.selectbox("Select time interval for stock data",intervals)            
    number = st.number_input('Enter number of days of data you would like:', value=1000, step=10)
    periods=str(number)+"d"
    df = yf.download(tickers='INJ-USD', period=periods, interval=interval)
    df['Date']=df.index
    df
    data=df
    # Calculate VWAP
    data['VWAP'] = (((data['High'] + data['Low'] + data['Close']) / 3) * data['Volume']).cumsum() / data['Volume'].cumsum()

    l=[]
    k=0
    for i in range(len(df)):
       k=k+df['Volume'][i]
       l.append(k)
    df['Cum_Vol']=l
    theme_plotly = None
    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
    # fig.add_trace(go.Bar(x=df['Date'], y=df['Volume'],name='Volume'), secondary_y=False)
    fig.add_trace(go.Line(x=df['Date'], y=df['Cum_Vol'], name='Cumulative Volume'), secondary_y=True)
    fig.update_layout(title_text=f'Cumulative Trading Volume')
    fig.update_layout(autosize=True,width=700,height=500,margin=dict(l=50,r=50,b=100,t=100,pad=4))
    fig.update_yaxes(title_text='Cumulative Volume', secondary_y=False)
    fig.update_yaxes(title_text='Date', secondary_y=True)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
    st.subheader(f'Historic Price Graph of-INJ')
#             st.subheader(choice)
            #     df = transactions_daily.query("Blockchain == @options")
    theme_plotly = None
    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(go.Bar(x=df['Date'], y=df['Volume'],name='Volume'), secondary_y=False)
    fig.add_trace(go.Line(x=df['Date'], y=df['Close'], name='Closing Price'), secondary_y=True)
    fig.update_layout(title_text=f'Historical Daily Closing Price of INJ')
    fig.update_layout(autosize=True,width=700,height=500,margin=dict(l=50,r=50,b=100,t=100,pad=4))
    fig.update_yaxes(title_text='Volume', secondary_y=False)
    fig.update_yaxes(title_text='Closing Price', secondary_y=True)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
    # fig.add_trace(go.Bar(x=df['Date'], y=df['Volume'],name='Volume'), secondary_y=False)
    fig.add_trace(go.Bar(x=df['Date'], y=df['Volume'],name='Volume'), secondary_y=False)
    fig.add_trace(go.Line(x=data['Date'], y=data['VWAP'], name='VWAP'), secondary_y=True)
    fig.update_layout(title_text=f'VWAP')
    fig.update_layout(autosize=True,width=700,height=500,margin=dict(l=50,r=50,b=100,t=100,pad=4))
    fig.update_yaxes(title_text='VWAP', secondary_y=False)
    fig.update_yaxes(title_text='VWAP', secondary_y=True)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# In[25]:


def peers():
    import streamlit as st
    st.header("Peer Comparisions")
    st.subheader("Price plots of INJ and its peers")
    import pandas as pd
    import pandas_datareader.data as web
    import plotly.graph_objs as go
    import yfinance as yf
    def getData(crypto):
       start1 = '2021-01-01'
       end1 = '2023-03-29'
       df = yf.download(crypto, start=start1, end=end1)
       return df
    cryptos = ['INJ-USD', 'KNC-USD', 'SUSHI-USD', 'BAL-USD']
    data = {crypto: getData(crypto) for crypto in cryptos}
    fig = go.Figure()
    col=['red','yellow','blue','green']
    i=0
    for crypto, df in data.items():
       fig.add_trace(go.Scatter(x=df.index, y=df['Close'],line=dict(color=col[i]), name=crypto))
       i=i+1
    # fig.show()
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    import yfinance as yf

# Fetch data
    bitcoin = yf.download('BTC-USD', start='2023-09-10', end='2023-12-10')
    ethereum = yf.download('ETH-USD', start='2023-09-10', end='2023-12-10')
    injective = yf.download('INJ-USD', start='2023-09-10', end='2023-12-10')
    knc = yf.download('KNC-USD', start='2023-09-10', end='2023-12-10')
    sushi = yf.download('SUSHI-USD', start='2023-09-10', end='2023-12-10')
    bal = yf.download('BAL-USD', start='2023-09-10', end='2023-12-10')

    import pandas as pd

# Create a DataFrame
    data = pd.DataFrame({
       'Bitcoin': bitcoin['Close'],
       'Ethereum': ethereum['Close'],
       'Injective': injective['Close'],
         'knc': knc['Close'],
       'sushi': sushi['Close'],
       'bal': bal['Close']
    })
    import seaborn as sns
    import matplotlib.pyplot as plt

    # Create a heatmap
    st.subheader("Correlation between INJ and it's peers")
    fig, ax = plt.subplots()
    sns.heatmap(data.corr(), ax=ax)
    st.pyplot(fig)

#     import yfinance as yf
#     import cvxpy as cp
#     import matplotlib.pyplot as plt
#     for i in range(len(cryptos)):
#         inj = yf.Ticker(cryptos[i])
#         hist = inj.history(period="max")
#         returns = hist['Close'].pct_change().dropna()
#         volatility = cp.Variable()

#         # Convert the pandas Series to a CVXPY constant
#         returns_const = cp.Constant(returns.values)

#         # Calculate the sum of the squares of the differences
#         diff = cp.sum_squares(returns_const - volatility)

#         model = cp.Problem(cp.Minimize(diff), [])
#         model.solve()
#         st.write(f"Volatility of {cryptos[i]}",float(volatility.value))
    import pandas as pd
    import pandas_datareader.data as web
    import plotly.graph_objs as go
    import yfinance as yf
    def getData(crypto):
       start1 = '2021-01-01'
       end1 = '2023-12-12'
       df = yf.download(crypto, start=start1, end=end1)
       df["Vol"] = df["Close"].pct_change().rolling(252).std()
       return df
    cryptos = ['INJ-USD', 'KNC-USD', 'SUSHI-USD', 'BAL-USD','BTC-USD','ETH-USD']
    data = {crypto: getData(crypto) for crypto in cryptos}
    fig = go.Figure()
    col=['red','yellow','blue','green','grey','black']
    i=0
    for crypto, df in data.items():
       fig.add_trace(go.Scatter(x=df.index, y=df['Vol'],line=dict(color=col[i]), name=crypto))
       i=i+1
    # fig.show()
    st.subheader("Volatility plot of INJ and its peers")
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    st.write("Above is a plot of volatilities of INJ and related assets. The recent price surge in INJ has surely impacted it's volatility in the present times. We can observe the volatilities are converging with time leading to lowered values")
    import pytrendseries
    data=yf.download("INJ-USD",period="1000d")
    filtered_data = data[['Close']]
    # filtered_data.columns = ['close_price']
    filtered_data.index = pd.to_datetime(filtered_data.index)
    filtered_data = filtered_data.sort_index()
    trend = "downtrend"
    window = 126 #6 months

    trends_detected = pytrendseries.detecttrend(filtered_data, trend=trend, window=window)
    import pytrendseries
    import matplotlib.pyplot as plt
    import seaborn as sns; sns.set_style("white")
    import streamlit as st

    trend = "downtrend"
    window = 126 #6 months

    trends_detected = pytrendseries.detecttrend(filtered_data, trend=trend, window=window)

    fig, ax = plt.subplots(figsize=(15,5))
    sns.histplot(trends_detected["drawdown"]*100, kde=True, bins=30, ax=ax)
    plt.ylabel("")
    plt.box(False)
    plt.annotate('Maximum Drawdown', xy=((trends_detected["drawdown"].max()-0.005)*100, 1),
                xycoords='data',
               xytext=(-105, 30), textcoords='offset points',color="red",
               weight='bold',
               arrowprops=dict(arrowstyle="->", color="r",
                              connectionstyle='arc3,rad=-0.1'))
    plt.annotate('Quantile 97,5%', xy=((trends_detected["drawdown"].quantile(0.975)-0.005)*100, 0.2),
                xycoords='data',
               xytext=(-135, 30), textcoords='offset points',color="red",
               weight='bold',
               arrowprops=dict(arrowstyle="->", color="r",
                              connectionstyle='arc3,rad=-0.1'))
    plt.xlabel("Drawdown (%)")
    plt.ylabel("Density", rotation=0, labelpad=-30, loc="top")
    st.subheader("Analyzing downtrends in time series")
    # Display the plot on Streamlit
    st.pyplot(fig)


# In[101]:


# peers()


# In[20]:


def sent():
    
    st.header("Recent Tweets and their Sentiments")
    tweet=['Myself, @ade_shina01 and  @OlafRiche were discussing about #INJ hitting $20 before on 15th of this month, lol not even 10th yet and is 19. If you’re not surprise by the @Injective_ movement then nothing will surprise you.','Dont say you were not informed about the #injective native token #INJ because our next best targets now is $25 before January. @Injective_is unstoppable. and is the best coin ever','$INJ hits the price target of $18.01 and trading at $18.87 Are we going to see $22.34 soon? it is really great 🚀 With both short-term and long-term moving averages signaling a bullish trend and the RSI at 57.5 seems promising.  #INJ is trying to break the support at $18.01 and reach the $20…','It is the year 2026 and you are finally rich.  Everyone wants to know your secret to financial freedom,  And you tell them In 2023 you bought and held: #KUJI #INJ which was the best decision','I wanna tell you about the @Injective_ Taipei Meetup during #TaipeiBlockchainWeek  Get ready for a night of fun, networking, and all things #Injective planned for you. #builders, #blockchain enthusiasts, and #investors will come together for #INJ  Taipei Meetup']
    popularity=[300,1200,1000,723,923]
    link=['https://twitter.com/BabakekereOfKP/status/1733125564217606401','https://twitter.com/HolyMoses21/status/1733082518335717440','https://twitter.com/MarketCoinpedia/status/1732983652500607334','https://twitter.com/Cosmos_Tic/status/1733410253696278567','https://twitter.com/Haezl_Crypto/status/1732855619416133664']
    tweets=pd.DataFrame()
    tweets['tweet']=tweet
    tweets['tweet view count']=popularity
    tweets['url']=link
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    from textblob import TextBlob
    nltk.download('punkt')
    nltk.download('stopwords')
    def clean_tweet(tweet):
       stop_words = set(stopwords.words('english'))
       word_tokens = word_tokenize(tweet)
       filtered_tweet = [word for word in word_tokens if word not in stop_words]
       return ' '.join(filtered_tweet)
    tweets['cleaned_tweets'] = tweets['tweet'].apply(clean_tweet)
    def get_sentiment(tweet):
      return TextBlob(tweet).sentiment.polarity

    tweets['sentiment'] = tweets['cleaned_tweets'].apply(get_sentiment)

    import requests
    import streamlit.components.v1 as components

#     def theTweet(tweet_url):
#         api = "https://publish.twitter.com/oembed?url={}".format(tweet_url)
#         response = requests.get(api)
#         res = response.json()["html"]
#         return res
    class Tweet(object):
        def __init__(self, s, embed_str=False):
            if not embed_str:
                # Use Twitter's oEmbed API
                # https://dev.twitter.com/web/embedded-tweets
                api = "https://publish.twitter.com/oembed?url={}".format(s)
                response = requests.get(api)
                self.text = response.json()["html"]
            else:
                self.text = s

        def _repr_html_(self):
            return self.text

        def component(self):
            return components.html(self.text, height=700)
    tab1, tab2, tab3, tab4 = st.tabs(["Tweet 1", "Tweet 2", "Tweet 3","Tweet 4"])
    with tab1:
            
            t = Tweet(link[0]).component()
            st.subheader("Sentiment Score  of above Tweet")
            st.write(tweets['sentiment'][0])

    with tab2:

            t = Tweet(link[1]).component()
            st.subheader("Sentiment Score  of above Tweet")
            st.write(tweets['sentiment'][1])

    with tab3:
            t = Tweet(link[2]).component()
            st.subheader("Sentiment Score  of above Tweet")
            st.write(tweets['sentiment'][2])
    with tab4:
           t = Tweet(link[3]).component()
           st.subheader("Sentiment Score  of above Tweet")
           st.write(tweets['sentiment'][3])
#     for i in range(len(link)):
#         t = Tweet(link[i]).component()
#         st.subheader("Sentiment")
#         st.write(tweets['sentiment'][i])
    st.header("Socials")
    st.write("Some highlights about Injective on social media 943 unique individuals are talking about Injective and it is ranked #13 in most mentions and activity from collected posts. In the last 24 hours, across all social media platforms, Injective has an average sentiment score of 3 out of 5. Finally, Injective is becoming more newsworthy, with 5 news articles published about Injective. This is a 60% increase in news volume compared to yesterday. On Twitter, people are mostly bullish about Injective. There were 44.23% of tweets with bullish sentiment compared to 9.18% of tweets with a bearish sentiment about Injective. 46.58% of tweets were neutral about Injective. These sentiments are based on 1960 tweets. On Reddit, Injective was mentioned in 13 Reddit posts and there were 20 comments about Injective. On average, there were more upvotes compared to downvotes on Reddit posts and more upvotes compared to downvotes on Reddit comments.")
    
    st.subheader("Socials Sentiment of the past 7 days")
    df=pd.read_csv('ITB_inj_telegram_sentiment_undefined_2023-12-15T17_53_47.431Z.csv')
    lists=[(df['Positive']),(df['Neutral']),(df['Price']),(df['Negative'])]
    labels = ['Positive', 'Neutral', 'Price', 'Negative']
    import matplotlib.pyplot as plt
    for i in range(len(lists)):
       plt.plot(lists[i], label=labels[i])
    plt.legend()
    st.pyplot(fig=None)
    st.write("Below we can observe a significant correlation between Positive reviews v/s Price of token")
    st.table(df.corr())
    st.write("")
    st.write("Below we see fundrate has been increasing for INJ")
    st.image("fundrate.png", width=700)
    st.write("Another thing to notice below is the increased volume of derivatives market which was accompanied by the recent price surge indicating a good correlation")
    st.image("derivatives.png", width=700)
    st.write("Overall Sentiment using technicals")
    st.image("senti.png", width=700)


# In[ ]:





# In[119]:


# sent()


# In[21]:


def srb():
    from streamlit_player import st_player
    from mplfinance.original_flavor import candlestick_ohlc
    import matplotlib.dates as mpl_dates
    import matplotlib.pyplot as plt
    st.header("Support Resistance Breakout")
    st.write("Support and resistance are two foundational concepts in technical analysis. Understanding what these terms mean and their practical application is essential to correctly reading price charts.")
    st.write("Technical analysts use support and resistance levels to identify price points on a chart where the probabilities favor a pause or reversal of a prevailing trend.") 
    st.write("Support occurs where a downtrend is expected to pause due to a concentration of demand.")
    st.write("Resistance occurs where an uptrend is expected to pause temporarily, due to a concentration of supply.") 
    st.write("Market psychology plays a major role as traders and investors remember the past and react to changing conditions to anticipate future market movement.")
    # st_player("https://www.youtube.com/watch?v=K5dnTdg7Lz8")

    showWarningOnDirectExecution = False
    st.set_option('deprecation.showPyplotGlobalUse', False)

    def get_stock_price(symbol):
      df = yf.download('INJ-USD', start='2023-02-01', threads= False)
      df['Date'] = pd.to_datetime(df.index)
      df['Date'] = df['Date'].apply(mpl_dates.date2num)
      df = df.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]
      return df

    def is_support(df,i):
      cond1 = df['Low'][i] < df['Low'][i-1] 
      cond2 = df['Low'][i] < df['Low'][i+1] 
      cond3 = df['Low'][i+1] < df['Low'][i+2] 
      cond4 = df['Low'][i-1] < df['Low'][i-2]
      return (cond1 and cond2 and cond3 and cond4)

    def is_resistance(df,i):
      cond1 = df['High'][i] > df['High'][i-1] 
      cond2 = df['High'][i] > df['High'][i+1] 
      cond3 = df['High'][i+1] > df['High'][i+2] 
      cond4 = df['High'][i-1] > df['High'][i-2]
      return (cond1 and cond2 and cond3 and cond4)

    def is_far_from_level(value, levels, df):
        ave =  np.mean(df['High'] - df['Low'])
        return np.sum([abs(value - level) < ave for _, level in levels]) == 0
    def plot_all(levels, df):
        fig, ax = plt.subplots(figsize=(16, 9), dpi=300)
        candlestick_ohlc(ax,df.values,width=0.6, colorup='green', colordown='red', alpha=0.8)
        date_format = mpl_dates.DateFormatter('%d %b %Y')
        ax.xaxis.set_major_formatter(date_format)
        for level in levels:
            plt.hlines(level[1], xmin=df['Date'][level[0]], xmax=max(df['Date']), colors='blue', linestyle='--')
        fig.show()
    #         fig_html = mpld3.fig_to_html(fig)
    #         components.html(fig_html, height=600)
        st.pyplot(fig=None)
    # stock_code = choice
    df = get_stock_price('INJ-USD')
    levels = []
    for i in range(2,len(df)-2):
      if is_support(df,i):
        l = df['Low'][i]
        if is_far_from_level(l, levels, df):
          levels.append((i,l))
      elif is_resistance(df,i):
        l = df['High'][i]
        if is_far_from_level(l, levels, df):
          levels.append((i,l))

    plot_all(levels, df)

    def has_breakout(levels, previous, last):
      for _, level in levels:
        cond1 = (previous['Open'] < level) # to make sure previous candle is below the level
        cond2 = (last['Open'] > level) and (last['Low'] > level)
      return (cond1 and cond2)

    def detect_level_method_1(df):
      levels = []
      for i in range(2,df.shape[0]-2):
        if is_support(df,i):
          l = df['Low'][i]
          if is_far_from_level(l, levels, df):
            levels.append((i,l))
        elif is_resistance(df,i):
          l = df['High'][i]
          if is_far_from_level(l, levels, df):
            levels.append((i,l))
      return levels
    def detect_level_method_2(df):
      levels = []
      max_list = []
      min_list = []
      for i in range(5, len(df)-5):
          high_range = df['High'][i-5:i+4]
          current_max = high_range.max()

          if current_max not in max_list:
              max_list = []
          max_list.append(current_max)
          if len(max_list) == 5 and is_far_from_level(current_max, levels, df):
              levels.append((high_range.idxmax(), current_max))

          low_range = df['Low'][i-5:i+5]
          current_min = low_range.min()
          if current_min not in min_list:
              min_list = []
          min_list.append(current_min)
          if len(min_list) == 5 and is_far_from_level(current_min, levels, df):
              levels.append((low_range.idxmin(), current_min))
      return levels

    # lists to store the screened results
    screened_list_1 = [] 


    # for symbol in stock_list:
    #   try: 
    df = get_stock_price('INJ-USD')
    st.subheader("Prediction-")
    levels_1 = detect_level_method_1(df)
    if (has_breakout(levels_1[-5:], df.iloc[-2], df.iloc[-1])):
        st.write("Less likely to have a Breakout in future")
    else:
        st.write("Might have a breakout in the near future")


# In[18]:


def tech():
    st.header("Hypothesis for possible price surge of INJ")
    st.write("INJ has seen a huge price surge mostly because of increase in social activity, historically INJ's prices surges when it has increased social activity and overall positive sentiment and also has corr with eth and btc")
    st.write("It is observed that INJ's Price increase was also part of the reason that Bitcoin and ETH have been increasing as there has been a huge pump by the whales into the crypto space")
    import yfinance as yf
    kl=[]
    pr=[]
    # Download historical data as dataframe
    stf=['2022-07-07','2022-09-09','2023-01-01','2023-07-07','2023-12-12']

    for i in range(len(stf)):
        data = yf.download(['INJ-USD', 'BTC-USD'], start=stf[i], end='2023-12-14')
        correlation = data['Close'].corr()
        kl.append(correlation['INJ-USD'][0])
        pr.append((data['Close']['INJ-USD'].pct_change()+1).cumprod()[1])
    # kl
    rel=pd.DataFrame()
    rel['Date']=stf
    rel['Price Correlation']=kl
    rel['Cummulative Returns of INJ']=pr
    df=rel
    df1=pd.DataFrame()
    df1['pr']=pr
    df1['cor']=kl
    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
    # fig.add_trace(go.Bar(x=df['Date'], y=df['Volume'],name='Volume'), secondary_y=False)
    fig.add_trace(go.Line(x=df['Date'], y=df['Price Correlation'],name='Price Correlation'), secondary_y=False)
    fig.add_trace(go.Line(x=df['Date'], y=df['Cummulative Returns of INJ'], name='Cummulative Returns of INJ'), secondary_y=True)
    fig.update_layout(title_text=f'Cummulative Returns of INJ')
    fig.update_layout(autosize=True,width=700,height=500,margin=dict(l=50,r=50,b=100,t=100,pad=4))
    fig.update_yaxes(title_text='Price Correlation', secondary_y=False)
    fig.update_yaxes(title_text='Cummulative Returns of INJ', secondary_y=True)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    st.subheader("Correlation between Cummulative returns of INJ and Correlation between price of INJ and BTC - ")
    print(df1.corr())
    st.subheader(df1.corr()['cor'][0])
    st.write("Above hypothesis is strongly backed by the above data results, as the correlation between the price of inj and btc increases we see an increase in inj returns, social activity also plays a big role in this sudden price surge")
    st.write("As the crypto market surges, whales keep looking for ALT-Coins which have potential and it turned out to be INJ as INJ has increased by almost 85% in just the last 5 days")
    st.header("Analyzing different protocols in INJ")
    df=pd.read_csv('chain-dataset-Injective.csv')
    df = df.transpose()
    df = df.iloc[1:, :]
    lists=[list(df[1]),list(df[3]),list(df[4]),list(df[5]),list(df[6])]
    labels = ['Helix', 'Astroport', 'White Whale Dex', 'Levana Perps','Black Panther']
    import matplotlib.pyplot as plt
    for i in range(len(lists)):
       plt.plot(lists[i], label=labels[i])
    plt.legend()
#     plt.show()
#     st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    st.pyplot(fig=None)
    st.write("On further analysis we observe Levana Perps and Black Panther have been the ones who have suddenly gained a high amount of volume while it has not been the case with other protocols. It is quite evident that Levana Perps and Black Panther have been huge contributers for the recent price surge in INJ")
    lists=[(df[5]),(df[6])]
    labels = ['Levana Perps','Black Panther']
    import matplotlib.pyplot as plt
    for i in range(len(lists)):
       plt.plot(lists[i], label=labels[i])
    plt.legend()
#     plt.show()
#     st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    st.pyplot(fig=None)
    st.subheader("Possible reasons for volume surge for Levana Perps")
    st.write("The recent funding for Levana Perps can be attributed to its unique approach to solving the risk of illiquidity, a common problem in other perps platforms. Levana Perps does not maintain an internal mark price concept. Instead, the spot market price is used for entry price and calculation of PnL within the system. This allows the protocol to remain stable even with little internal volume.")
    st.write("Levana Perps also introduces a concept called a delta neutrality fund to further incentivize a balanced protocol. Unlike funding payments, the delta neutrality fund takes lump-sum payments at position open, update, and close.")
    st.write("Furthermore, Levana Perps has the ability to list high staking rewards token. The unique feature of Levana Perps is that traders pay a borrow fee on counter-side collateral, which can be multiple times lower than the notional size of the position. This gives traders the ability to hedge high staking reward tokens cheaply, making it viable to earn delta-neutral yield from staking")
    st.write("In conclusion, the recent funding for Levana Perps can be attributed to its unique approach to managing risk, its innovative use of a delta neutrality fund, and its ability to list high staking rewards tokens, among other features. These features make it an attractive platform for traders and liquidity providers.")
    st.write("")
    st.subheader("Possible reasons for volume surge for Black Panther")
    st.write("Black Panther Finance has recently clinched an impressive third place in the Injective Hackathon, positioning itself as a formidable force showcasing strength and innovation. This success is more than just a ranking; it symbolizes Black Panther Finance’s creative approach to revolutionizing the Injective community.")
    st.write("The integration between Injective and Black Panther brings forth a plethora of advantages for users and the broader DeFi ecosystem. By combining the strengths of both platforms, users can expect enhanced liquidity, reduced trading fees, and increased trading options with the availability of various synthetic assets.")
#     st.write("The recent funding for Black Panther can be attributed to its unique approach to managing risk, its innovative use of a delta neutrality fund, and its ability to list high staking rewards tokens, among other features.")
    
  


# In[106]:


# 
def buy_and_hold():
    st.header("Buy and Hold")
    st.write("Here we analyze the buy and hold results of INJ token which can be checked for any timeframe we want")
#         image="pexels-pixabay-259027.jpg"
#         st.image(image, use_column_width=True)
    st_player("https://www.youtube.com/watch?v=cNOsE7p8DRw")
    st.write("1m gives data worth of 7 days")
    st.write("2m,5m,15m,30m,90m gives data worth of 60 days")
    st.write("1h gives data worth of 730 days")
#         sp500 = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]["Symbol"]
#         sp500_list = sp500.tolist()
#     df1=pd.read_csv('sec_bhavdata_full.csv')
#     l=[]
#     for i in range(len(df1)):
#         l.append(df1['SYMBOL'][i]+'.NS')
#     l=l[1:]
    showWarningOnDirectExecution = False
    st.set_option('deprecation.showPyplotGlobalUse', False)
#     activities=l
#     activities[0]="TATASTEEL.NS"
    choice='INJ-USD'
#         activities1=["Get Data using Specific Period & Intervals","Get Data Using Custom Start and End Dates"]
#         choice1=st.selectbox("Fetch Data",activities1)


#         if choice1=="Get Data using Specific Period & Intervals":
    intervals=["1d","1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "5d", "1wk", "1mo", "3mo"]
    interval=st.selectbox("Select time interval for stock data",intervals)            
    number = st.number_input('Enter number of days of data you would like:', value=1000, step=10)
    periods=str(number)+"d"
#             period=["1000d","1d", "2d","5d", "7d", "15d", "30d", "60d", "90d", "200d", "500d",  "2000d", "5000d", "7000d","10000d"]
#             periods=st.selectbox("Select time period for stock data",period)
#             choice=st.selectbox("Select Data Selection Mode",activities)
#     try:
    data = yf.download(tickers=choice, period=periods, interval=interval)

#     c1, c2 = st.columns([1,2])
#     with c1:
    data

    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    csv = convert_df(data)

    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='Historical_Data.csv',
        mime='text/csv',
    )

    from backtesting import Backtest, Strategy
    data['Date']=data.index
    df=data
    st.subheader(f'Historic Price Graph of- {choice}')
#             st.subheader(choice)
    #     df = transactions_daily.query("Blockchain == @options")
    theme_plotly = None
    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(go.Bar(x=df['Date'], y=df['Volume'],name='Volume'), secondary_y=False)
    fig.add_trace(go.Line(x=df['Date'], y=df['Close'], name='Closing Price'), secondary_y=True)
    fig.update_layout(title_text=f'Historical Daily Closing Price of {choice}')
    fig.update_layout(autosize=True,width=700,height=500,margin=dict(l=50,r=50,b=100,t=100,pad=4))
    fig.update_yaxes(title_text='Volume', secondary_y=False)
    fig.update_yaxes(title_text='Closing Price', secondary_y=True)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    ret=df['Close'].pct_change().dropna()
#         print(ret)
    summary=pd.DataFrame()
    summary["mean"]=ret.describe()["mean"]*252
    summary["std"]=ret.describe()["std"]*np.sqrt(252)

#         summary.plot.scatter(x="std",y="mean",figsize=(12,8),s=50,fontsize=15)
#         for i in summary.index:
#             plt.annotate(i,xy=(summary.loc[i,"std"]+0.002,summary.loc[i,"mean"]+0.002),size=15)
#         plt.xlabel("Annual risk(std)",fontsize=15)
#         plt.ylabel("Annual return",fontsize=15)
#         plt.title("Risk/Return",fontsize=25)
#         plt.show()
#         st.pyplot(fig=None, clear_figure=None)


    hdfc=data.Close.to_frame()
    hdfc["Daily_returns"]=np.log(hdfc.div(hdfc.shift(1)))
    hdfc.dropna(inplace=True)
#         st.write("Return",hdfc.Daily_returns.sum())
    hdfc["Cumulative_returns"]=hdfc.Daily_returns.cumsum().apply(np.exp)
#         st.write("Average Annual Return",hdfc.Daily_returns.mean()*252)
    hdfc['Date']=hdfc.index
    hdfc["Cummax"]=hdfc.Cumulative_returns.cummax()
    hdfc[["Cumulative_returns","Cummax"]].plot(figsize=(12,8),fontsize=15,title="HDFC Buy and Hold+Cummax")
    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(go.Line(x=hdfc['Date'], y=hdfc['Cumulative_returns'],name='Cumulative_returns'), secondary_y=True)
    fig.add_trace(go.Line(x=hdfc['Date'], y=hdfc['Cummax'], name='Cumulative maximum'), secondary_y=True)
    fig.update_layout(title_text=f'Historical Daily Closing Price of {choice}')
    fig.update_yaxes(title_text='Volume', secondary_y=False)
    fig.update_yaxes(title_text='Closing Price', secondary_y=True)
    fig.update_layout(autosize=True,width=700,height=500,margin=dict(l=50,r=50,b=100,t=100,pad=4))
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
#     with c2:
# #             try:
#             from scipy.interpolate import griddata

#             df = yf.download(tickers=choice, period="1000d", interval="1d")
#             df['Adj_Close']=df['Adj Close']
#             x = np.array(df.Adj_Close)
#             y = np.array(df.Close)
#             z = np.array(df.Volume)


#             xi = np.linspace(x.min(), x.max(), 100)
#             yi = np.linspace(y.min(), y.max(), 100)
#             X,Y = np.meshgrid(xi,yi)
#             Z = griddata((x,y),z,(X,Y))
#             fig = go.Figure(go.Surface(x=xi,y=yi,z=Z))
#             fig.update_layout(title_text=f'3D Mesh Data of {choice}')
#             fig.update_layout(scene=dict(xaxis_title='Adj Close', yaxis_title='Closing', zaxis_title='Volume'))
#             fig.show()
#             st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
# #             except:
#                 pass
    hdfc["Drawdown"]=hdfc["Cummax"]-hdfc["Cumulative_returns"]
#         st.write("Maximum Drawdown",hdfc.Drawdown.max())
    hdfc["Percent_Drawdown"]=(hdfc["Cummax"]-hdfc["Cumulative_returns"])/hdfc["Cummax"]
#         st.write("Maximum Percent Drawdown",hdfc["Percent_Drawdown"].max())
    df['returns'] = df['Close'].pct_change()
    df['cummax'] = df['Close'].cummax()
    df['drawdown'] = df['Close'] - df['cummax']
    df['adj']=df['Close'].min()
    df['adjx']=df['Close'].max()
    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(go.Bar(x=df['Date'], y=df['drawdown'],name='Drawdown'), secondary_y=False)
    fig.add_trace(go.Line(x=df['Date'], y=df['Close'], name='Closing Price'), secondary_y=True)
    fig.add_trace(go.Line(x=df['Date'], y=df['adj'], name='Lowest Price attained',line=dict(color='red')) ,secondary_y=True)
    fig.add_trace(go.Line(x=df['Date'], y=df['adjx'], name='Highest Price attained',line=dict(color='green')), secondary_y=True)
    fig.update_layout(title_text='Drawdown')
    fig.update_yaxes(title_text='Drawdown', secondary_y=False)
    fig.update_yaxes(title_text='Closing Price', secondary_y=True)
    fig.update_layout(autosize=True,width=700,height=500,margin=dict(l=50,r=50,b=100,t=100,pad=4))
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    data['dr']=np.log(data['Close'].div(data['Close'].shift(1)))
    data.dr.sum()
    np.exp(data.dr.sum())
    data['cumre']=data.dr.cumsum().apply(np.exp)
    df['adj']=df['cumre'].min()
    df['adjx']=df['cumre'].max()
#         data['cumre']=data['cumre']*100
    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
#         fig.add_trace(go.Bar(x=df['Date'], y=df['Volume'],name='Volume'), secondary_y=False)
    fig.add_trace(go.Line(x=df['Date'], y=df['cumre'], name='Initial Capital'), secondary_y=True)
    fig.add_trace(go.Line(x=df['Date'], y=df['adj'], name='Lowest Capital Dropped',line=dict(color='red')) ,secondary_y=True)
    fig.add_trace(go.Line(x=df['Date'], y=df['adjx'], name='Highest Capital Attained',line=dict(color='green')), secondary_y=True)
    fig.update_layout(title_text='Initial Capital')
#         fig.update_xaxes(title_text='Date', secondary_y=False)
    fig.update_yaxes(title_text='Initial Capital Change', secondary_y=True)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    class BuyAndHold(Strategy):
        def init(self):
            self.buy()

        def next(self):
            pass

    # Run the backtest
    bt = Backtest(df, BuyAndHold, commission=0.005)
    stats=bt.run()
    l=[]
    l=(stats)
    df=pd.DataFrame(l)

    df['attributes']=df.index
    df['output']=df[0]
    del df[0]

    def convert_df(df):
        return df.to_csv().encode('utf-8')

    csv = convert_df(df)
#             csv
    st.download_button(
        label="Download Backtesting Report",
        data=csv,
        file_name='BUY&HOLD_Backtest.csv',
        mime='text/csv',
    )
#     except:
#         st.warning("Invalid parameters entered please follow the instructions")
        


# In[7]:


import vectorbt as vbt

def ma(df, n):
    return pd.Series(df['Close'].rolling(n, min_periods=n).mean(), name='MA_' + str(n))


# In[114]:


def sma():
        st.header("Simple Moving Average Crossover")
#         image="pexels-anna-nekrashevich-6801648.jpg"
#         st.image(image, use_column_width=True)
        st_player("https://www.youtube.com/watch?v=fIVtszQ3USo")
        st.write("1m gives data worth of 7 days")
        st.write("2m,5m,15m,30m,90m gives data worth of 60 days")
        st.write("1h gives data worth of 730 days")
#      
        showWarningOnDirectExecution = False
        st.set_option('deprecation.showPyplotGlobalUse', False)

        choice='INJ-USD'

        intervals=["1d","1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h"]
        interval=st.selectbox("Select time interval for stock data",intervals)            
        number = st.number_input('Enter number of days of data you would like:', value=1000, step=10)
        periods=str(number)+"d"
#             tb=1
#             period=["1000d","1d", "2d","5d", "7d", "15d", "30d", "60d", "90d", "200d", "500d",  "2000d", "5000d", "7000d","10000d"]
#             periods=st.selectbox("Select time period for stock data",period)
#             choice=st.selectbox("Select Data Selection Mode",activities)
#     try:
        data = yf.download(tickers=choice, period=periods, interval=interval)




        data
        def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(data)

        st.download_button(
            label="Download above data as CSV",
            data=csv,
            file_name='Historical_Data.csv',
            mime='text/csv',
        )
        data1=data
        fast_period=20
        slow_period=50
        feess=0.00
#         fast_period=st.sidebar.slider("fast_period", min_value=0, max_value=200, value=50)
#         slow_period=st.sidebar.slider("slow_period", min_value=fast_period+1, max_value=500, value=200)
#         feess=st.sidebar.slider("Transaction fees", min_value=0.0, max_value=1.0, value=0.001)
        st.sidebar.write("Customize the Default parameters")
        fft=st.sidebar.slider("fast_period", min_value=0, max_value=200, value=20)
        ss=st.sidebar.slider("slow_period", min_value=fft+1, max_value=500, value=50)
        ff=st.sidebar.slider("Transaction fees", min_value=0.0, max_value=1.0, value=0.00)
        if st.sidebar.button("Submit the new input parameters"):
                fast_period=fft
                slow_period=ss
                feess=ff
        AAPL = data

        data['fast'] = ma(data,fast_period)
        data['slow'] = ma(data, slow_period)
        data['Date']=data.index
        theme_plotly = None
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=data['Date'], y=data['Volume'],name='Volume'), secondary_y=False)
        fig.add_trace(go.Line(x=data['Date'], y=data['Close'], name='Closing Price'), secondary_y=True)
        fig.add_trace(go.Line(x=data['Date'], y=data['fast'], name='fast_period'), secondary_y=True)
        fig.add_trace(go.Line(x=data['Date'], y=data['slow'], name='slow_period'), secondary_y=True)
        fig.update_layout(title_text=f'Historical Daily Closing Price of Injective')
        fig.update_yaxes(title_text='Volume', secondary_y=False)
        fig.update_yaxes(title_text='Closing Price', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        df=data

        price = vbt.YFData.download(choice, period=periods,interval=interval).get("Close")



        fast_ma = vbt.MA.run(price, fast_period)
        slow_ma = vbt.MA.run(price, slow_period)
        entries = fast_ma.ma_crossed_above(slow_ma)
        exits = fast_ma.ma_crossed_below(slow_ma)

        pf = vbt.Portfolio.from_signals(price, entries, exits, init_cash=100,fees=feess)
        stats=pf.stats()
        fig = pf.plot_trades()
#             fig.show()
#             st.pyplot(fig=None, clear_figure=None)
        st.subheader("Trades Occured")
        st.plotly_chart(fig)
        st.subheader("Value throughout the Backtest")
        fig2=pf.plot_value()
        fig3=pf.plot_underwater()
        fig4=pf.plot_cum_returns()
        st.plotly_chart(fig2)
        st.subheader("Value throughout the Backtest")
        st.plotly_chart(fig3)
        st.subheader("Cummulative Returns")
        st.plotly_chart(fig4)
#         pf.plot()
        l=[]
        l=(stats)
        df=pd.DataFrame(l)
        df#44
#         print(df)
#         f.append(df)
        c1, c2 = st.columns([1,2])
        with c1:
            st.subheader("Backtesting Report")
            df
            print(df[0])
#         df=pd.DataFrame(l)
#         df['attributes']=df.index
        df['output']=df[0]
        del df[0]
        def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')
        csv = convert_df(df)
#         print(csv)
        st.download_button(
            label="Download the Backtesting Report",
            data=csv,
            file_name='SMA_Backtest.csv',
            mime='text/csv',
        )
        df=pf.entry_trades.records_readable
        with c2:
            st.subheader("Trades Occured")
            df


# In[113]:


# f=[]
# sma()


# In[112]:


# f[0]


# In[110]:


# Create a dictionary linking page names to their respective functions
pages = {
    "Introduction to INJ": home,
#     "🫖About": about,
    "Peers and Trends": peers,
    "Price Surge in INJ":tech,
    "Current Market Sentiment":sent,
    "Support and Resistance Breakout":srb,
    "Buy and Hold":buy_and_hold,
    "Moving Average Crossover Backtesting":sma
}

st.sidebar.title("📈Navigation")
st.sidebar.subheader("Go to👉")
# st.sidebar.expander("Choose a Strategy")

page_choice = st.sidebar.radio("", list(pages.keys()))

# Display the selected page
pages[page_choice]()


# In[69]:


# df=pd.read_csv('chain-dataset-Injective.csv')
# df = df.transpose()
# df = df.iloc[1:, :]
# lists=[list(df[1]),list(df[3]),list(df[4]),list(df[5]),list(df[6])]
# labels = ['Helix', 'Astroport', 'White Whale Dex', 'Levana Perps','Black Panther']

# for i in range(len(lists)):
#    plt.plot(lists[i], label=labels[i])
# plt.legend()
# plt.show()


# In[ ]:




