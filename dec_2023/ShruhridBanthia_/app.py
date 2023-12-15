import streamlit as st
import pandas as pd
import requests
from datetime import datetime, timedelta
import altair as alt
from PIL import Image


# Set background to light
st.set_page_config(layout="wide")
st.title("Decentraland (MANA) Price Analysis")

# Section 1: Introduction to Decentraland
with st.container():
    st.header("1. Introduction to Decentraland")
    st.markdown(
        """
    
    ### Whitepaper Analysis
    
    Decentraland is an Ethereum-based virtual ecosystem. It has revolutionized the digital landscape by offering users the ability to buy and sell digital properties, engage in games, trade collectibles, and participate in social interactions within a shared virtual world. Decentralanad is goverened by DAO, Decentralized Autonomous Organization that eliminates the need for a central governing agency.

    Originating in 2015 and officially launched in 2017, Decentraland gained prominence in 2021 as the cryptocurrency market and NFTs surged in popularity. The MANA tokens, initially priced at 0.02 USD, saw a substantial increase, reaching values between 6000 USD and 100,000 USD per parcel. Notably, major brands like Samsung, Adidas, Atari, and Miller Lite joined the platform, acquiring virtual "properties."
    
    Decentraland's architecture revolves around three key concepts: The World, consisting of 3D units called Parcels; The District, formed through DAO voting; and The Marketplace, the hub of Decentraland's economy. The technical aspects involve three layers – Consensus, Assets, and Real-time – ensuring efficient operation of the decentralized virtual space.
    
    Tokenomics in Decentraland involve two distinct tokens: LAND, and MANA, an ERC20 token serving as a governance token. MANA is the native token of the Decentraland ecosystem. It is used to purchase LAND, pay for goods and services within the virtual world and buy items from the marketplace. LAND is a non-fungible token (NFT) that represents a 16m x 16m plot of virtual land(parcels). Estate is a collection of LAND parcels grouped together. 
    
    The project faces competition from platforms like The Sandbox, Rarible, Vault Hill, and Odyssey, each offering unique features within the blockchain and metaverse spaces.

    *Source: [Decentraland Whitepaper](https://decentraland.org/whitepaper.pdf)*
    """
    )

# Section 3: Price-related Analysis
with st.container():
    st.header("2. MANA Token Price Analysis")
    
    st.subheader("Overview")
    st.markdown(
        """
        This section contains the in-depth analysis of the price of Decentraland MANA token in USD all the way since it's inception in 2017 to December 2023. 

        This analysis is divided into three parts for better understanding of the long term and short term trends:
        - __Historical Price Analysis:__ This section contains the analysis of the price of the token from 28th October 2017 to 12th December 2023. 
        - __Last 3 Years Price Analysis:__ This section contains the analysis of the price of the token from 3rd January 2021 to 12th December 2023. 
        - __2023 Price Analysis:__ This section contains the analysis of the price of the token in 2023 till 12th December.

        The data sources for the analysis are:
        - [CoinMarketCap](https://coinmarketcap.com/currencies/decentraland/historical-data/)
        - [Coingecko](https://https://www.coingecko.com/en/coins/decentraland/historical_data#panel)

        Before diving deep into the analysis, let us first understand some terms and concepts related to the price of the token.

        - __Open Price:__ The price of the token at the start of the day. *(in USD)*
        - __Close Price:__ The price of one unit of token at the end of the day. *(in USD)*
        - __Market Cap:__ The market capitalization of one unit of token at the end of the day. *(Price of one share * Number of shares)* *(in USD)*
        - __Volume:__ The trading volume of one unit of token at the end of the day.
        - __High Price:__ The highest price of one unit of token in the day. *(in USD)*
        - __Low Price:__ The lowest price of one unit of token in the day. *(in USD)*
        - __Range:__ The difference between the highest and lowest price of the token in the day. *(High Price - Low Price)* *(in USD)*
        - __Difference:__ The difference between the close and open price of the token in the day. The higher the difference indicates higher the growth of the price of the token on that particular day. *(Close Price - Open Price)* *(in USD)*
        - __High Time:__ The time of the day when the price of the token was the highest. *(in PST)*
        - __Low Time:__ The time of the day when the price of the token was the lowest. *(in PST)* 
        - __Moving Average:__ The Moving Average of the token. *(Average of the prices of the token in the last 20 days)*
        """)
        # - __Close Ratio:__ The ratio of the closing price to the highest price of the token in the day. *(Close Price / High Price)*
        # - __Price To Metcalf Ratio__: The ratio of the price of the token to the Metcalf's law value of the token. *(Price / Metcalf's law value)*
        # - __Metcalf's Law Value__: The Metcalf's law value of the token. *(Market Cap / Number of users)*
        # - __Boilinger Band:__ The Boilinger Band of the token. *(Moving Average + 2 * Standard Deviation)*
    st.markdown("---")
    st.subheader("Historical Price Analysis")

    st.markdown(
        """
        #### Initial Analysis
        The following plot shows the price of a unit of token, the market cap and the trading volume of the MANA token.
        """
    )
    image_path = "Images/mana_historic_price.png"
    image = Image.open(image_path)
    st.markdown('**Historic Trends Visualization**')
    st.image(image)

    st.markdown(""" **Comments on the plot:** """)
    st.markdown("""
            - The standout inference from the plot is the huge increase in the price of the token in the last quarter of 2021. This was due to the announcement of the __Metaverse__ by Facebook on 28th October 2021. A report on 1st of November 2021 by [Blockchain.news](https://blockchain.news/news/metaverses-mana-token-price-leaps-after-facebook-rebrand-to-meta) states "the price of a MANA token, which can be used in a metaverse leapt 164 percent in 12 hours."
            - The sudden metaverse frenzy brought a short lived spike in the price and market cap of the token, and rather much shorter lived spike in the total volume of the token.
                """)
    
    st.markdown(""" --- """)
    st.markdown(
        """
        ### Year-Wise Price Development 

        The following plots show the price development of the MANA token in each year since its inception in 2017. The prices have been normalized on a scale of 0 to 1 for better comparison minimizing the effect of varied mean prices through the years.
""")
    
    col1, col2 = st.columns(2)
    col1.markdown("**Price Development in 2017|20|21**")
    col2.markdown("**Price Development in 2018|19|22|23**")
    image_path = "Images/mana_norm_price_dev_20_21.png"
    image = Image.open(image_path)
    col1.image(image)
    image_path = "Images/mana_norm_price_dev_18_19_22_23.png"
    image = Image.open(image_path)
    col2.image(image)
    col1.markdown("**Using 20-Day MVA**")
    col2.markdown("**Using 20-Day MVA**")
    image_path = "Images/mana_norm_price_dev_20_21_smooth.png"
    image = Image.open(image_path)
    col1.image(image)
    image_path = "Images/mana_norm_price_dev_18_19_22_23_smooth.png"
    image = Image.open(image_path)
    col2.image(image)
    col1.markdown("**Inference and Comments**")
    col1.markdown("""
                  - The price of the token has remained nearly constant in the first half of each of the years.
                  - The price of the token has seen a sudden spike in the second half of each of the years.
                  - The 2017 spike was due to the **early sale of the token**.
                  - The first minor peak in February 2020 occured just after **Decentraland went public and set up the DAO.**
                  - As per Report in [Nonfungible.com](https://https://nonfungible.com/news/metaverse/discovery-of-decentraland) the peak was short lived due to the pandemic related lockdowns, but it grabbed pace again in the second half of the year because "**Decentraland stepped up its collaborations with the arts sector**"
                  - The 2021 spike was due to the announcement of the __Metaverse__ by Facebook on 28th October 2021.
        """)
    col2.markdown("**Inference and Comments**")
    col2.markdown("""
        - The price of the token has overall shown a downward trend in the years 2018, 2019, 2022 and 2023.
        - In April 2018 the price of the token saw a sudden rise. [Nonfungible.com](https://https://nonfungible.com/news/metaverse/discovery-of-decentraland) states that "the developers announced on April 23rd the **release of the SDK (development kit) alpha to start building and modeling scenes according to their wishes."** This led to the sudden rise in the price of the token.
        - The year 2022 is often called the **"crypto winter"**. The price of the token has seen a downward trend in the year 2022. This is due to the fact that the crypto market was in a bear run in the year 2022.
        - The steady rise and thereafter stability of the price in the first half of 2019 was due to the fact that Decentraland released the **"Drag and Drop Builder"** allowing an increased user base.
    """)
    
    st.markdown("---")
    st.subheader("Token Price Variables Analysis for the past 3 years")
    st.markdown(
        """
        Here we identify the correlation between the various price related variables present in the data.
        """
    )
    image_path = "Images/mana_correlation_3_year.png"
    st.markdown('**Correlation Visualization**')
    image = Image.open(image_path)
    st.image(image)

    st.markdown(
        """
        - In the correlation plot above, we can use these rules to get an idea of the interdependence between various currencies:
            - Darker colors indicate stronger correlations, while lighter colors indicate weaker correlations.
            - Positive correlations (when one variable increases, the other variable tends to increase) represented by warm colors.
            - Negative correlations (when one variable increases, the other variable tends to decrease) represented by cool colors.
        - High positive correlation is seen among price related variables the following variables:
            - Open price, Close price, High price, Low price, Market Cap
        - Interestingly Volume is not that strongly correlated with them. It's correlation is around 0.5. This indicates that the **price** of the token is **not very dependent on the trading volume** of the token.
        - There is a **high positive correlation** between **volume and range**. This indicates that the higher the trading volume, the higher the range of the price of the token might be for a given day.
        """
    )

    
    st.markdown("---")
    st.subheader("Token Price Variables Analysis for 2023")

    st.markdown("""We have seen the correlation between various price related variables for the past 3 years. Now, let us see the correlation between various price related variables for the year 2023. Along with this we will also analyze the correlation between the High Time and the Low Time of the token price for the year 2023.""")

    col1, col2 = st.columns(2)
    col1.markdown("**Correlation among price related variables**")
    col2.markdown("**Correlation between High Time and Low Time**")
    image_path = "Images/mana_correlation_1_2023.png"
    image = Image.open(image_path)
    col1.image(image)
    image_path = "Images/mana_correlation_time_2023.png"
    image = Image.open(image_path)
    col2.image(image)

    col1.markdown("""
        - The correlation among price related variables is very similar to that of the past 3 years.
                  """)
    col2.markdown("""
        - The correlation between the High Time and the Low Time is -0.43. This indicates that the **time of the day** when the price of the token is **highest** is **inversly dependent** on the time of the day when the price of the token is **lowest**. This is an interesting observation. This would also mean that the **erratic nature** of the price of the token is **not very high.** This indicates that the hourly(or minute by minute) volatility is not very high.
                  """)

    st.markdown("---")
    st.subheader("Do the Day of the Week Affect the Price of the Token?")

    st.markdown("""
    An interesting aspect of token price fluctuations is the weekly price trend. 
    The following plots show the distribution of the top 10 extreme differences in the daily price(close - open) of the MANA token for the past 3 years and that of 2023. Incase of the same day having multiple entries in the top 10 extreme difference list we stack them together.  
    """)

    col1, col2 = st.columns(2)
    col1.markdown(""" **Result for top 10 extreme difference in past 3 years** """)
    col2.markdown(""" **Result for top 10 extrem difference in 2023** """)
    image_path = "Images/top_10_dates_3_year.png"
    image = Image.open(image_path)
    col1.image(image)
    image_path = "Images/top_10_dates_2023.png"
    image = Image.open(image_path)
    col2.image(image)

    col1.markdown("""
        - The Facebook to Meta announcement on 28th October plays the dominant role. Creating the **largest extreme difference on Friday Saturday, 30th October 2021**. The scale of the reaction(rise of **2.7 USD in two days**) to this announcement also skews the distribution of the extreme differences in the past 3 years.
        - The consecuent day of Sunday, 31st October 2021 saw a repurcussive reaction to the meteoric growth with an **extreme lower difference of -0.6 USD.**
                """)
    
    col2.markdown("""
        - There are a numebr of interesting observations here.
        - **Friday** has the **highest number and magnitude of high extreme difference.** While it does not have even a single entry in the top 10 lowest differences.
        - There is a **steady increase in the contribution to the highest highs of the token as we move through the week.** This is inline with the statement at [CorporateFinanceInstitute](https://corporatefinanceinstitute.com/resources/cryptocurrency/best-time-to-buy-cryptocurrency/) that states, "Generally, cryptocurrency prices start low on Monday and rise throughout the week. When the weekend hits, prices tend to drop until market activity begins the following Monday." 
        - It would be conclusive to infer that beginning of the week, Monday(also Sunday), is the best time to buy the token. While Friday might just be the best time to sell the token.
        """)
    
    st.markdown("---")
    st.subheader("Is there a particular time of the day when the price of the token is highest or lowest?")

    st.markdown("""
        The following scatter plot shows the distribution of the High Time and the Low Time with respect to the time (normalized for 0 to 24) and the day of the year 2023. The larger the size of the dot, the higher the high at the high time. Similarly, the larger the size of the dot, the lower the low at the low time.
""")
    image_path = "Images/Daily_Extreme_Value.png"
    image = Image.open(image_path)
    st.image(image)

    st.markdown("""
        - The distribution tends to be more concentrated towards the midnight hours of PST time. Given that both High time and low time occur more frequently in the midnight hours, it is safe to assume that the price of the token is more volatile in the midnight hours.
        - This volatility often tends to be so high that they contribute the the highest highs and the lowest lows of the token price of that day.
            
""")
    st.markdown("---")

# Section 4: Competition Analysis
with st.container():
    st.header("3. Market Competition Analysis")
    # df = display_multiple_plots()
    # df.index = pd.to_datetime(df.index, unit="ms")
    # st.line_chart(df)

    # Additional analysis or features can be added here
    st.write(
        """
    Explore additional market competition analysis or features in this section.
    You can analyze trends, identify key events, or present other relevant insights.
    """
    )

    st.subheader("Overview")
    st.markdown(
        """
    To understand the competition related Decentraland MANA we can analyse the data corresponding to similar cryptocurrencies. These are the top five cryptocurrencies similar to MANA which are direct competitors in the market:
    #### [SAND](https://coinmarketcap.com/currencies/the-sandbox/)
    - The Sandbox essentially operate on the same idea. The Sandbox is a community-driven platform where creators can monetize voxel assets and gaming experiences on the blockchain. Similar to various Metaverse real estate, users can engage, create virtual structures, and get incentives by selling certain goods on the platform. Briefly, The Sandbox is a virtual world where players can build, own, and monetize their gaming experiences in the Ethereum blockchain using the platform’s utility token SAND.
    
    #### [AXS](https://coinmarketcap.com/currencies/axie-infinity/)
    - Axie Infinity is another metaverse platform where gamers earn rewards based on their participation. The platform is built on the Ethereum blockchain and it is a decentralized application (dApp) that allows players to collect, breed, raise, battle, and trade token-based creatures known as Axies. These Axies are adorable creatures that are similar to Pokemon and CryptoKitties. 
    - They can as well play against AI-controlled Axies to earn reward. The platform’s utility token is AXS. The token is used for governance and staking on the platform. It is also used to purchase in-game items and pay for transaction fees.
    
    #### [ILV](https://coinmarketcap.com/currencies/illuvium/)
    - Illuvium as another competitor against Decentraland has a similar concept to Axie Infinity. Players combat Illuvials with the intention of capturing them to battle other players.
    - The game structure provides an option of combining Illuvials to make them stronger, putting their owners at an advantage during duels with other players. Lastly, these Illuvials can be traded as NFTs and the platform uses ILV as its utility token.
    
    ### [STX](https://coinmarketcap.com/currencies/stacks/)
    - Stacks is a blockchain that enables smart contracts and apps on Bitcoin. It is a layer-1 blockchain that uses the security of the Bitcoin network to secure its smart contracts. The platform’s utility token is STX. It is used for governance and staking on the platform.
    
    ### [THETA](https://coinmarketcap.com/currencies/theta-network/)
    - Theta aims to decentralize video streaming, operating a peer-to-peer video delivery network. The company’s promises are like many metaverse business plans: reduce costs, transfer power from companies to the masses and eliminate intermediaries. 
    - According to Theta, this vision would give a bigger piece of the pie to content creators and make video cheaper for consumers.
    
    *Source: [Coinbase](https://coinmarketcap.com/currencies/decentraland/historical-data/), [Forbes](https://www.forbes.com/advisor/in/investing/cryptocurrency/top-metaverse-coins/)*
    
    In this section, we will be comparing the Decentraland MANA token with these 5 competitors. We will be comparing the price, market capitalization, and trading volume of these tokens. We will also perform some experiments to analyse the correlation and return on investmen between these tokens.
    """
    )

    # Exploratory Data Analysis Section
    st.subheader("Exploratory Data Analysis")
    image_path = "Images/data_example.png"
    image = Image.open(image_path)
    st.image(image, caption="Example Data")
    col1, col2 = st.columns(2)
    metric = """
    The data used for this analysis is taken from CoinMarketCap. The data is taken for the starting from the December of 2019 till date. The data is sample on monthly basis for each of the tokens. The data is then cleaned and preprocessed to remove any null values and outliers. The data is then visualized using various plots to understand the trends and patterns in the data.
    
    #### Metrics
    - Price: The price of the token at the end of the month.
    - Open: The price of the token at the start of the month.
    - High: The highest price of the token in the month.
    - Low: The lowest price of the token in the month.
    - Close: The price of the token at the end of the month.
    - Spread: The difference between the highest and lowest price of the token in the month.
    - Close Ratio: The ratio of the closing price to the highest price of the token in the month.
    - Maket Cap: The market capitalization of the token at the end of the month.
    - Volume: The trading volume of the token at the end of the month.
    - Rank: Current rank of the token in the market.
    
    """
    # col2.markdown(metric)
    st.markdown(metric)

    st.write(
        "*Data source: [CoinMarketCap](https://coinmarketcap.com/currencies/decentraland/)*"
    )
    st.markdown("---")

    st.markdown("### Correlation between the currencies")
    image_path_cap = "Images/correlation.png"
    image_cap = Image.open(image_path_cap)
    st.image(image_cap)
    st.markdown(
        """

        - From the correlation plot, we observe that the correlation between MANA and SAND is __0.94__ which is very high. This is due to the fact that both the tokens have similar use-case and are direct competitors.
        
        - Except for Theta Network, all the other tokens have a correlation of more than __0.8__ with MANA. This is due to the fact that all the tokens are competitors and have similar use-case.
        
        Using these correlation values of Decentraland MANA and their effects, we have analyzed the trends between the currencies with respect to market cap, transaction volume and price.
        """
    )

    col1, col2 = st.columns(2)
    col1.markdown("**Currencies by Market Capitalization:**")
    image_path_cap = "Images/currencies_by_market_cap.png"
    image_cap = Image.open(image_path_cap)
    col1.image(image_cap)
    col2.markdown("**Currencies by Transaction Volume:**")
    image_path_volume = "Images/currencies_by_transactin_volume.png"
    image_volume = Image.open(image_path_volume)
    col2.image(image_volume)
    st.markdown("---")

    st.markdown(
        """
        ### Market Cap
        
        - From the stream plot, we see that the market cap of Theta Network is consistently higher than all the other tokens.
        - The market cap of Decentraland MANA at ATH is __0.67 times__ the market cap of Theta Network at ATH.
        - Decentraland MANA ranks consisntently at around 3rd or 4th position in terms of market cap.
        - One important observation is the consistent dominance of SAND over MANA in terms of market cap.
        - The crpto market __bull__ run of 2021 is clearly visible in both the plots.
        
        - __Qualitatively__, we can reason that Theta Network which address the singular problem of video streaming has a higher market cap than Decentraland MANA which is a virtual reality platform providing streaming, gaming, and other services.
            - This focussed approach of Theta Network is an indicator for better investments and thus a higher market cap.
            - This is also the reason for its dominance over SAND and various other tokens which are aiming to provide a virtual reality platform.
        """
    )
    col1, col2 = st.columns(2)
    col1.markdown("**Market Cap**")
    image_path_cap = "Images/market_cap_per_curr.png"
    image_cap = Image.open(image_path_cap)
    col1.image(image_cap)
    col2.markdown("**Market Cap (Stream)**")
    image_path_volume = "Images/market_cap_per_curr_stream.png"
    image_volume = Image.open(image_path_volume)
    col2.image(image_volume)
    st.markdown("---")

    st.markdown(
        """
        ### Transaction Volume
        
        - In the line chart, we observe that, although similar, the transaction volume of The Sandbox is slightly higher than that of Decentraland MANA.
        - The peak in transaction volumes is observed in the last quarter of 2021 for MANA and almost all other tokens. This was due to the announcement of the __Metaverse__ by Facebook. Numerous new users joined the crypto market and the transaction volume increased.
        - Decentraland MANA ranks consisntently at around 2nd or 3rd position in terms of transaction volume.
        
        - __Qualitatively__, we see that even though the use case of both MANA and SAND is similar, the transaction volume of SAND is higher than that of MANA. Following are the possible speculations for this:
            - SAND was launched much earlier in 2011 as compare to MANA in 2017 and is a more mature platform and has been in the market for a longer time.
            - Compared to MANA, SAND has a higher real estate supply than Decentraland. Moreover, due the maturity, it has better options for users to purchase virtual land.
            - Decentraland MANA has lesser user generated content than SAND, and the gaming experience is not as good as SAND. Thus, the transaction volume is lower.
            
        """
    )
    col1, col2 = st.columns(2)
    col1.markdown("**Transaction Volume**")
    image_path_cap = "Images/trans_volume_per_curr.png"
    image_cap = Image.open(image_path_cap)
    col1.image(image_cap)
    col2.markdown("**Transaction Volume (Stream)**")
    image_path_volume = "Images/trans_volume_per_curr_stream.png"
    image_volume = Image.open(image_path_volume)
    col2.image(image_volume)
    st.markdown("---")

    st.markdown(
        """
        ### Price
        
        - From the line charts and stream plot, we observe that there is one outlier, ILV (Illuvium), whose peak price is much higher than other tokens and is also much higher than the ATH of Decentraland MANA. ILV also has consistently higher prices than other tokens.
        - Excluding ILV, Decentraland MANA ranks around 2nd consistently in terms of price.
        - The latest price of Decentraland MANA is around 0.5 USD as compred to ILV which is around 100 USD. All the other tokens are in price range similar to MANA.
        - The peak in price plot is obtained around last quarter of 2021 which was due to the announcement of the __Metaverse__ and the bull run of the crypto market.
        
        - __Qualitatively__, we can analyse the huge difference between ILV and rest of tokens including Decentraland MANA. Following are the possible speculations for this:
            - ILV is a very new token. It was launched in the mid of 2021. Thus, it has not yet been in the market for a long time resulting in a higher price.
            - Further, ILV is anticipated to be a breakthrough in AAA crypto gaming. This anticipation has led to a huge demand for the token and thus the price is very high.
            - However, overall ILV has smaller market cap and transaction volume than MANA. Once, ILV is more mature and has more users, it will be able to compete with MANA. According to current context, MANA is a better investment than ILV.
        """
    )
    col1, col2 = st.columns(2)
    col1.markdown("**Price per unit of Currency**")
    image_path_cap = "Images/price_per_unit_curr.png"
    image_cap = Image.open(image_path_cap)
    col1.image(image_cap)
    col2.markdown("**Price per unit of Currency (Stream)**")
    image_path_volume = "Images/price_per_unit_curr_stream.png"
    image_volume = Image.open(image_path_volume)
    col2.image(image_volume)
    st.markdown("---")
    st.subheader("Competition in 2023")
    st.markdown(
        """
        Trends observed in 2023 were consistend with overall trends of market capitalization, tranasaction volume and price per unit currency.Excluding, the crypto market bull run of 2021, there was not significant change in trends from 2020 to 2023. Let us analyse the trends in 2023.
        
        """
    )

    st.markdown(
        """
        ### Market Cap in 2023
        
        - Decentraland MANA ranks at around 4th position in terms of market cap in 2023. MANA's ATH is 0.5 times the ATH of Theta Network.
        - All tokens saw an increase in market cap in last three months of 2023. This is due to the fact that the crypto market is growing and more and more people are investing in crypto.
        - From the stream plot, the market cap of Theta Network in 2023 is consistent with overall trend. Due to its focussed approach towards use-case, it has a higher market cap than all the other tokens.
        - One interesting observation is the convergence of market cap at the end of 2023 comapred to the start of 2023.
        
        Qualitatively, the analysis of the overall trend applies to the year of 2023 as well. For improvement in market cap, Decentraland MANA needs to focus on its use-case and provide better user experience.
        """
    )
    col1, col2 = st.columns(2)
    col1.markdown("**Market Cap in 2023**")
    image_path_cap = "Images/market_cap_per_curr_2023.png"
    image_cap = Image.open(image_path_cap)
    col1.image(image_cap)
    col2.markdown("**Market Cap in 2023 (Stream)**")
    image_path_volume = "Images/market_cap_per_curr_2023_stream.png"
    image_volume = Image.open(image_path_volume)
    col2.image(image_volume)
    st.markdown("---")

    st.markdown(
        """
        ### Transaction Volume in 2023
        
        - Decentraland MANA ranks at around 3rd or 4th position in terms of market cap in 2023. MANA observed a decrease in the first half of 2023 and then an increase in the second half of 2023.
        - From the stream plot, The Sandbox performed better than Decentraland MANA in 2023 consistently having around 1.5 times the transaction volume of MANA.
        - All tokens saw an increase in transaction volume in last three months of 2023. This is due to the fact that the crypto market is growing and new users are adopting crypto.
        - One interesting observation is the convergence of transaction volume at the end of 2023 comapred to the start of 2023.
        
        Qualitatively, the analysis of the overall trend applies to the year of 2023 as well. For improvement in market cap, Decentraland MANA needs to focus on its use-case and provide better user experience.
        """
    )
    col1, col2 = st.columns(2)
    col1.markdown("**Transaction Volume in 2023**")
    image_path_cap = "Images/transact_volume_per_curr_2023.png"
    image_cap = Image.open(image_path_cap)
    col1.image(image_cap)
    col2.markdown("**Transaction Volume in 2023 (Stream)**")
    image_path_volume = "Images/transact_volume_per_curr_2023_stream.png"
    image_volume = Image.open(image_path_volume)
    col2.image(image_volume)
    st.markdown("---")

    st.markdown(
        """
        ### Price in 2023
        
        - Excluding ILV, Decentraland MANA ranks at around 2nd position in terms of market cap in 2023. MANA observed a lower price in the end of 2023 as compared to the start of 2023.
        - The latest price of Decentraland MANA is around 0.5 USD as compred to ILV which is around 100 USD. All the other tokens are in price range similar to MANA.
        - In 2023 too, ILV is an outlier with a much higher price than all the other tokens.
        
        Qualitatively, the analysis of the overall trend applies to the year of 2023 as well.
        
        """
    )
    col1, col2 = st.columns(2)
    col1.markdown("**Price per unit of Currency in 2023**")
    image_path_cap = "Images/price_per_unit_curr_2023.png"
    image_cap = Image.open(image_path_cap)
    col1.image(image_cap)
    col2.markdown("**Price per unit of Currency in 2023 (Stream)**")
    image_path_volume = "Images/price_per_unit_curr_2023_stream.png"
    image_volume = Image.open(image_path_volume)
    col2.image(image_volume)
    st.markdown("---")

    st.markdown(
        """
        ### Future of Decentraland MANA
        
        According to _Analytics Insight_, Decentraland stands out as one of the most prominent and promising metaverse projects, earning it a featured spot on our list of upcoming cryptocurrencies poised for significant growth.

        Being the first metaverse project established, Decentraland benefits from a pioneering advantage, evolving into the largest and most valuable virtual world. This position has facilitated strategic partnerships with renowned brands, both on and off the blockchain.

        As a pioneer in the metaverse realm, Decentraland is not only widely recognized but also actively sought after by various brands, such as Samsung, JP Morgan, Adidas, Coca-Cola, Starbucks, and others. These brands have invested in virtual land within Decentraland, intending to develop projects, thereby contributing to increased investor interest and the success of MANA tokens.

        These partnerships have played a crucial role in maintaining an upward trajectory for MANA token prices since their inception. Anticipating a resurgence in the market, we foresee MANA's price recovering in 2023, reclaiming its all-time high, and potentially establishing a new record. This anticipation serves as the primary rationale for its inclusion in our selection of cryptocurrencies expected to experience significant growth this year.

        Moreover, we feature Decentraland due to our expectation that its extensive support base and strategic utilization of various cryptocurrency trends will propel MANA tokens to unprecedented heights in 2023. The incorporation of NFT technology within the metaverse and the anticipated growth in play-to-earn games on its network are poised to initiate substantial trends likely to drive MANA token prices to unprecedented levels.

        """
    )

    st.write(
        "*Source: [AnalyticsInsight](https://analyticsinsight.net/next-cryptocurrency-to-explode-in-2023-which-coins-will-blow-up/)*"
    )
    st.markdown("---")

    st.markdown(
        """
        ## Empirical Analysis
        
        We will be conducting two analysis based on the data from 2020 to 2023.
        
        ### Return on Investment
        
        The plots show the return on investment for each token in the period of 2020 to 2023. The plot for the year 2023 shows the return on an investment made in the beginning of 2023. The plots are calculated using the closing prices at the end of the particular month. The following plots assume an initial investment of 1000 USD in the each token at the beginning. 
        """
    )
    col1, col2 = st.columns(2)
    col1.markdown("**Return on Investment**")
    image_path_cap = "Images/roi_curr.png"
    image_cap = Image.open(image_path_cap)
    col1.image(image_cap)
    col2.markdown("**Return on Investment in 2023**")
    image_path_volume = "Images/roi_curr_2023.png"
    image_volume = Image.open(image_path_volume)
    col2.image(image_volume)

    st.markdown(
        """
        ### Earnings
        
        The plots shows earnings for each token in the period of 2020 to 2023. The plot for the year 2023 shows the earnings made in 2023. The plots are calculated using the closing prices at the end of the particular month. The following plots assume an initial investment of 1000 USD in the each token at the beginning. 
        
        Even though the overall earning of Decentraland MANA is negative, the positive earnings in 2023 indicate that the token in growing and could be a good investment in the future.
        """
    )
    col1, col2 = st.columns(2)
    col1.markdown("**Earnings**")
    image_path_cap = "Images/earnings.png"
    image_cap = Image.open(image_path_cap)
    col1.image(image_cap)
    col2.markdown("**Earnings in 2023**")
    image_path_volume = "Images/earnings_2023.png"
    image_volume = Image.open(image_path_volume)
    col2.image(image_volume)
    st.markdown("---")


# Section 5: Social Media Analysis
with st.container():
    st.header("4. Current Social Media Sentiment and Conclusion")
    # Additional analysis or features can be added here
    st.markdown(
        """
    Social media analysis serve as a reflection of the community's sentiment towards the cryptocurrency. It helps in understanding the price volatalities and potential market movements. In this section, we will be relying on the data provided by _Coinbase_ which obtains the data from a paid social media analysis tool called _LunarCRUSH_.
    
    According to _Coinbase_
    - 152 individuals are sharing 157 posts about Decentraland MANA on Twitter and Reddit combined in last 24 hours.
    - It ranks 213 in terms of the mentions and activity on Twitter(among Cryptocurrencies).
    - Based on 220 tweets about Decentraland MANA:
        - 5.45 percent bullish sentiment
        - 10.45 percent show bearish sentiment
        - 84.09 spercent show neutral sentiment

    According to _GFGI.IO_

    It identifies the performance of the token based on it's Fear and Greed Index. 

    - The Fear and Greed Index of Decentraland MANA is 59 percent which is in the range of Neutral.
    - Their AI based investment suggestion suggests to hold the token.


    The above data were recorded as of 4:00 AM IST on 16st December 2021.
    
    *Source:*
    [Coinbase](https://www.coinbase.com/price/decentraland#SocialMediaMetricsSection)
    [GFGI.IO](https://cfgi.io/mana-fear-greed-index/1d?z=1#details)
    """
    )
    st.markdown("---")

    st.markdown("**Conclusion**")
    st.markdown(
        """
        This report is an exhaustive study on the price variation of the Decentraland MANA token. Correlations between various price related variables have been studied. The price development of the token has been studied for the past 3 years. In depth analysis of the data has been done to identify annual, weekly and daily trends in the price of the token. It has been compared with its competitors. Lastly, the social media sentiment analysis has been presented to understand the current market sentiment towards the token.
        """)
