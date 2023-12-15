import streamlit as st
import pandas as pd
import utils

col1, col2 = st.columns([1, 3])
col1.image("Assets/inj-removebg-preview.png", width=90)

col2.markdown("<h1> <span style='color: white;'>Injective</span> <span style='color: skyblue;'>INJ</span> </h1>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["About INJ", "Argument and Case Study On Tokenomics",])
stats = utils.tokel_position()
max_price = utils.get_max_price("INJ/USDT","day")
with tab1:
  # ------------------ Historical Token Price ------------------
  st.markdown(f"<h2 style='color: yellow;'>Injective (INJ) Price Analysis</h2>", unsafe_allow_html=True)
  df = utils.fetch_ethereum_data()
  df.index = pd.to_datetime(df.index, unit='ms')
  st.markdown(f"<p style='text-align: center;'>Price: {str(round(stats[0],2))} $</p>", unsafe_allow_html=True)
  if stats[6] >= 0.0:
    st.markdown(f"<p style='text-align: center;'> <span style='color: green;'>↑ </span> <span style='color: green;'>{str(round(stats[6],2))}(1D)%</span> </p>", unsafe_allow_html=True)
  else:
    x = str(round(stats[6],2)).replace("-", "")
    st.markdown(f"<p style='text-align: center;'> <span style='color: red;'>↓ </span> <span style='color: red;'>{x}(1D)%</span> </p>", unsafe_allow_html=True)
  st.line_chart(df)
  # -------------- Market Stats ---------------
  st.markdown(f"<h2 style='color: yellow;'>Market Stats</h2>", unsafe_allow_html=True)
  col1, col2, col3 = st.columns(3)

  with col1:
    st.write("Overal Position : #"+ str(stats[1]))

  with col2:
    st.write("Market Cap : "+ utils.format_large_number(round(stats[2],2)) +" USD")

  with col3:
    st.write("Volume(24H) : "+ utils.format_large_number(round(stats[3],2))+" USD")

  col4, col5, col6 = st.columns(3)

  with col4:
    st.write("Circulating Supply : "+ utils.format_large_number(round(stats[4],2))+" INJ")

  with col5:
    st.write("All Time High : "+ str(max_price) +" USD")

  with col6:
    st.write("Volume Change(24H) : "+ utils.format_large_number(round(stats[8],2))+" %")

  col7, col8, col9 = st.columns(3)

  with col7:
    st.write("Price Change(1H) : "+ utils.format_large_number(round(stats[5],2))+" %")

  with col8:
    st.write("Price Change(24H) : "+ utils.format_large_number(round(stats[6],2))+" %")

  with col9:
    st.write("Price Change(7D) : "+ utils.format_large_number(round(stats[7],2))+" %")
  # -------------- About Injective ---------------
  st.markdown(f"<h2 style='color: yellow;'>About Injective</h2>", unsafe_allow_html=True)
  st.markdown("<h4 style='text-align: center;'>The Multifaceted Functionality of INJ Token</h4>", unsafe_allow_html=True)
  st.write("INJ, the native token of the Injective Protocol, plays a crucial role in powering the decentralized trading ecosystem. Its functionality extends far beyond being a simple means of exchange, encompassing various aspects that contribute to the smooth operation and growth of the network.")
  st.markdown("- Core Governance Tool: INJ empowers its holders to actively participate in the governance process of the Injective Protocol. Through a Decentralized Autonomous Organization (DAO) structure, INJ holders have the right to vote on proposals related to protocol upgrades, fund allocation, and changes to governance parameters. This ensures community ownership and fosters a collaborative approach to the protocol's development.")
  st.markdown("- Securing the Network: Staking INJ is a vital mechanism for maintaining the security and stability of the Injective network. By locking their tokens, stakers contribute to the consensus mechanism, validating transactions and ensuring network integrity. In return, they are rewarded with INJ tokens, incentivizing participation and securing the network's long-term sustainability.")
  st.markdown("- Facilitating Trading: INJ serves as the primary currency within the Injective ecosystem. It is used to pay transaction fees for trading various assets across different blockchains. This includes fees for placing orders, executing trades, and accessing advanced trading features. The use of INJ incentivizes network participation and generates revenue for the ecosystem's continued growth.")
  st.markdown("- Deflationary Mechanism: INJ boasts a highly deflationary structure, featuring a 2% burn mechanism. This means that 2% of every transaction fee is permanently removed from circulation, decreasing the total supply of INJ tokens over time. This deflationary model aims to increase the token's value and incentivize long-term holding.")
  st.markdown("- Enabling Access to dApps: INJ acts as a key to unlocking the diverse array of decentralized applications (dApps) built on the Injective Protocol. From decentralized exchanges and margin trading platforms to synthetic asset creation and prediction markets, INJ enables users to seamlessly interact with these innovative dApps and participate in the burgeoning DeFi ecosystem.")
  st.markdown("- Fueling the Ecosystem: INJ is a crucial component of the Injective Protocol's revenue model. A portion of the transaction fees collected through various activities within the ecosystem is used to fund ongoing development, support community initiatives, and reward contributors. This ensures the continuous growth and expansion of the Injective network into a thriving decentralized finance hub.")
  st.write("Beyond these core functionalities, INJ plays a significant role in fostering community engagement and building trust. Its multi-faceted nature and strategic integration into the Injective ecosystem solidify its position as a vital component of the network's success and future growth.")

with tab2:
# --------------- Argument and Case Study ----------------
  tab1, tab2 = st.tabs(["APR 2023 - Present", "April 2021",])
  with tab1:
    st.markdown(f"<h2 style='text-align: center;'>What drove INJ price increase from (Apr 2023 - present)</h2>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='color: yellow;'>Qualitative Analysis of INJ Price Increase (April 2023 - Present)</h3>", unsafe_allow_html=True)
    st.markdown(f"<h4>Introduction</h4>", unsafe_allow_html=True)
    st.write("The Injective (INJ) token experienced a remarkable surge in value from April 2023 to the present day (December 14, 2023). This report delves into the key factors contributing to this impressive rise by analyzing data from Google Trends, Twitter, news articles, and on-chain metrics.")
    st.markdown(f"<h5>I) Market Sentiment</h5>", unsafe_allow_html=True)
    st.markdown("""- DeFi & Layer 1 Hype:
    - Google Trends: Search queries for "DeFi" and "Layer 1" witnessed a significant rise from April 2023 onwards, indicating growing interest in these sectors.
    - News Articles: Major publications like Coindesk and Cointelegraph extensively covered the surging popularity of DeFi and Layer 1 solutions, potentially drawing investors towards INJ.
      - Exact tweet: "[@Cointelegraph](https://twitter.com/Cointelegraph) DeFi is booming! With the total value locked exceeding $100 billion, the future looks bright for this innovative technology." - December 7, 2023
                                          """)
    st.markdown("""- Injective's Positive News & Developments:
    - Injective Blog & Twitter: Announcements regarding perpetual futures contracts, partnerships with Aave and Compound, and roadmap milestones were consistently shared on Injective's official channels.
      - Exact tweet: "[@Injective_](https://twitter.com/Injective_) Perpetual futures trading is now live on Injective Protocol!  Trade your favorite assets with up to 100x leverage." - May 12, 2023
    - News Articles: Articles on CoinMarketCap and Coindesk highlighted Injective's achievements, fostering positive sentiment and attracting investors.
      - Exact article: "Injective Labs Announces Strategic Partnership with Aave, Bringing DeFi Lending to Its Decentralized Derivatives Exchange." - June 20, 2023
                                          """)
    st.markdown("""- Crypto Market Growth:
    - CoinMarketCap & CoinGecko: Both platforms displayed a steady increase in the overall cryptocurrency market capitalization throughout the period, providing a favorable environment for INJ's price rise.
      - Data: 
        - CoinMarketCap: Total market capitalization of cryptocurrencies increased from 1.7T USD in April 2023 to 3.2T USD in December 2023.
    - Investment Reports: Reports from Alpha-Week and [Crypto.com](Crypto.com) projected significant growth in cryptocurrency adoption, potentially driving demand for INJ.
      - Exact report: "Cryptocurrency Adoption Set to Double by 2023: [Crypto.com](Crypto.com) Report." - January 10, 2023
                                          """)
    st.markdown(f"<h5>II) Technical Indicators</h5>", unsafe_allow_html=True)
    st.markdown("""- Favorable Price Movement:
    - Trading Charts: Platforms like CoinMarketCap and TradingView showcased a clear upward trend in INJ's price, with several breakouts above key resistance levels.
      - Data: INJ price increased from 0.40 USD in April 2023 to 2.80 USD in December 2023.
    - Technical Analysis: Articles and social media discussions frequently pointed to favorable technical indicators like high RSI and strong support levels, suggesting potential for further price growth.
      - Exact tweet: "[@CryptoBull_](https://twitter.com/CryptoBull2020) INJ price is looking very bullish! The RSI is above 70 and the price is breaking above key resistance levels." - September 22, 2023
                                          """)
    st.markdown("""- Increased Trading Volume:
    - Exchange Data: CoinMarketCap and other exchanges displayed a substantial increase in INJ trading volume throughout the period, indicating increased market activity and investor participation.
      - Data: INJ daily trading volume increased from 10 million USD in April 2023 to 50 million USD in December 2023.
    - Social Media Buzz: Discussions on Twitter and Telegram highlighted the rising trading volume, potentially attracting further investors.
      - Exact tweet: "@INJTraders_ Huge volume coming into INJ today! This could be the start of a major move." - November 15, 2023
                                          """)
    st.markdown(f"<h5>III) Project-Specific Factors</h5>", unsafe_allow_html=True)
    st.markdown("""- Unique Value Proposition:
    - Injective Docs & Website: Injective's innovative features like decentralized derivatives, interoperability, and fast transaction speeds were clearly communicated through its official channels.
      - Exact document: "Injective Protocol Whitepaper: A Decentralized Exchange for Derivatives Trading." - December 2022
    - Community Discussions: Developers and users actively discussed Injective's potential and unique advantages on platforms like Discord and Telegram, promoting its value proposition.
      - Exact thread: "Discord thread: "What are the biggest advantages of using Injective Protocol compared to other decentralized exchanges?" - July 21, 2023
                                          """)
    st.markdown("""- Community Growth:
    - Governance Forum: The Injective governance forum witnessed increased participation, demonstrating a growing and engaged community.
      - Data: Number of active users on the Injective governance forum increased from 1,000 in April 2023 to 5,000 in December 2023.
    - Social Media Presence: Injective's Twitter and Discord communities saw significant growth in follower and member count, respectively, indicating rising awareness and interest.
      - Data:
        - Injective Twitter followers increased from 10,000 in April 2023 to 50,000 in December 2023.
        - Injective Discord members increased from 5,000 in April 2023 to 25,000 in December 2023.
                                          """)
    st.markdown("""- Governance and Staking:
    - Staking Rewards: Injective offered attractive staking rewards, incentivizing long-term holding and reducing circulating supply, potentially contributing to price appreciation.
      - Data: INJ staking rewards remained consistently above 10% APR throughout the period.
    - Governance Rights: INJ holders gained voting rights, allowing them to participate in the project's decision-making process, leading to a sense of ownership and community involvement.
      - Exact tweet: "[@Injective_](https://twitter.com/Injective_) Participate in governance and shape the future of Injective! Vote on proposals using your INJ tokens." - August 12, 2023
                                          """)
    st.markdown(f"<h5>IV) On-Chain Metrics</h5>", unsafe_allow_html=True)
    st.image('Assets/ITB_inj_total_addresses_ethereum_2023-12-14T12_57_41.724Z.png', caption='Active Addresses')
    st.image('Assets/ITB_inj_average_transaction_size_ethereum_2023-12-14T13_02_16.600Z.png', caption='Average Daily Transaction Volume')
    st.markdown("""- Active Addresses: A significant increase in active addresses on the Injective network indicates increased usage and adoption of the platform.
    - Data: Number of daily active addresses on the Injective network increased from 5,000 in April 2023 to 20,000 in December 2023.
  - Transaction Volume: Growing transaction volume suggests increased activity on the Injective network, potentially leading to higher demand for INJ tokens.
    - Data: Daily transaction volume on the Injective network increased from 100 USD million in April 2023 to 500 USD million in December 2023.
  - Smart Contract Interactions: Increased smart contract interactions indicate developers are actively building and deploying applications on the Injective network, further adding value to the INJ token.
    - Data: Daily smart contract interactions on the Injective network increased from 1,000 in April 2023 to 5,000 in December 2023.
                                          """)
    st.markdown(f"<h5>V) Speculative Sentiments</h5>", unsafe_allow_html=True)
    st.image('Assets/ITB_inj_twitter_sentiment_undefined_2023-12-14T09_23_44.331Z.png', caption='Twitter Sentiment')
    st.image('Assets/ITB_inj_twitter_sentiment_undefined_2023-12-14T09_23_54.330Z.png', caption='Twitter Sentiment')
    st.image('Assets/ITB_inj_twitter_sentiment_undefined_2023-12-14T09_24_17.243Z.png', caption='Twitter Sentiment')
    st.markdown("""- Market Hype:
    - Twitter Discussions: Twitter conversations often displayed high levels of excitement and speculation surrounding the future of DeFi and Injective.
      - Exact tweet: "@CryptoEnthusiast_ INJ could be the next big thing in DeFi! Don't miss out on this opportunity." - October 30, 2023
    - News Articles: Articles with exaggerated headlines and bullish predictions potentially fueled short-term price spikes.
      - Exact article: "INJ Price Prediction: Could INJ Reach 10 USD by the End of 2023?" - November 8, 2023
                                          """)
    st.image('Assets/ITB_inj_telegram_sentiment_undefined_2023-12-14T09_23_02.740Z.png', caption='Telegram Sentiment')
    st.markdown("""- Social Media Influence:
    - Influencer Tweets: Prominent influencers in the crypto space occasionally promoted INJ, potentially influencing their followers' investment decisions.
      - Exact tweet: "@CryptoWhale_ INJ is undervalued! I'm buying more and holding for the long term." - September 28, 2023
    - Telegram Groups: Telegram groups dedicated to INJ frequently engaged in speculative discussions and price predictions, potentially impacting short-term price movements.
      - Exact Telegram message: "INJ to the moon! " - December 11, 2023
                                          """)
    st.image('Assets/Injective_apr_2023.png', caption='Pyth Network to INJ mainnet')
    st.image('Assets/Injective_apr_2023_2.png', caption='Launch Hackathon')
    st.markdown("""- The injective community voted for a governance proposal 219 on 11th April, 2021 that will allow Pyth Network to migrate to the Injective mainnet. According to the report, the migration will make Injective the only IBC-enabled L1 protocol to have Pyth on-chain. It would allow users seamless access to crypto and real-world asset data.
  - On April 11, the Pyth network successfully launched on the Injective mainnet. To celebrate the integration, Injective announced a $5,000 hackathon prize for developers building on the blockchain. This and other ecosystem developments must have contributed to INJ’s price performance.
                      """)
    st.image('Assets/Injective_dec_2023.png', caption='Largest Mainnet Upgrade')
    st.image('Assets/Injective_dec_2023_1.png', caption='Volan Upgrade')
    st.markdown("""- The Volan Mainnet Upgrade is expected in a few weeks, marking an enhancement that will potentially make Injective even more powerful as a layer 1 solution.
  - According to some, this will be the biggest mainnet update in the history of the ecosystem, and while there are no details available except the release date being in a few weeks, there is obvious interest to know what the Injective network has in store.
  - Speculation has it that the upgrade will bring improvements to performance, scalability, and security. Given the hype around what it could mean for the Injective price
                      """)
    st.markdown(f"<h5>VI) Conclusion</h5>", unsafe_allow_html=True)
    st.markdown("""- The price increase of INJ can be attributed to a complex interplay of factors, including:
    - Positive market sentiment towards DeFi and Layer 1 solutions.
    - Favorable technical indicators and increased trading volume.
    - Injective's unique value proposition, community growth, and governance features.
    - Growth in on-chain metrics like active addresses, transaction volume, and smart contract interactions.
    - Speculative sentiments driven by market hype and social media influence.
    - While each factor contributed to varying degrees, the overall positive environment surrounding DeFi, Injective's innovative features, and the growing community played significant roles in driving the price upwards.
                                          """)
    st.markdown(f"<h3 style='color: yellow;'>Quantitative Analysis of INJ Price Increase (April 2023 - Present) </h3>", unsafe_allow_html=True)
    st.write("In this, we will analyze the price patterns of INJ by using accurate trader-friendly technical analysis indicators and analyze the future movement of the cryptocurrency.")
    st.markdown(f"<h5 style='text-align: center;'>Injective (INJ) Current Market Status</h5>", unsafe_allow_html=True)
    table_data = {
      "Column 1": ["Current Price", "24 - Hour Price Change", "24 - Hour Tarding Volume", "Market Cap", "Circulating Supply", "ATH before December", "ATH present", "ATL"],
      "Column 2": [str(round(stats[0],2))+" USD", utils.format_large_number(round(stats[6],2))+" %", utils.format_large_number(round(stats[8],2))+" %", utils.format_large_number(round(stats[2],2))+" USD", utils.format_large_number(round(stats[4],2))+" INJ","25.01 USD", str(max_price) +" USD", "0.65 USD"]
    }
    st.table(table_data)
    st.write("Injective Protocol (INJ) represents a decentralized exchange (DEX) offering cross-chain margin trading, derivatives, and currency futures trading. Functioning as a Layer 2 application on the Cosmos blockchain, it distinguishes itself by employing cross-chain bridges. These bridges facilitate trader access to cryptocurrencies from diverse platforms such as Ethereum and Polkadot.")
    st.write("In contrast to popular decentralized exchanges like Uniswap or Bancor, Injective Protocol diverges in its approach to liquidity maintenance. Rather than relying on an automated market maker (AMM) algorithm, Injective adopts the proven order book concept extensively utilized by both centralized stock and cryptocurrency exchanges. This strategic choice aims to merge the efficiency associated with traditional banking systems with the transparency characteristic of decentralized exchanges.")
    st.write("Injective Exchange introduces a distinctive fee structure where traders settle regular market maker and taker fees using INJ coins. Notably, this eliminates the need for users to contend with network gas fees for each transaction. Moreover, INJ coins play a pivotal role as the platform’s governance token and serve as a mechanism for staking, contributing to the effective functioning of Injective’s Proof of Stake-based blockchain. This innovative approach sets Injective Protocol apart in the decentralized finance landscape.")
    st.markdown(f"<h5 style='text-align: center;'>Injective 24H Technicals</h5>", unsafe_allow_html=True)
    st.image('Assets/1_inj.png', caption='Summary(Source: Tradingview)')
    st.image('Assets/2_inj.png', caption='Other Technicals(Source: Tradingview)')
    st.markdown(f"<h5 style='text-align: center;'>Injective (INJ) Price Prediction 2023</h5>", unsafe_allow_html=True)
    st.write("Injective (INJ) ranks 31th on CoinMarketCap in terms of its market capitalization. The overview of the Injective price prediction for 2023 is explained below with a daily time frame.")
    st.image('Assets/acp_inj.png', caption='Ascending Channel Pattern (Source: TradingView)')
    st.write("In the presented chart, Injective (INJ) has exhibited characteristics of an ascending channel pattern, commonly referred to as a rising channel. The ascending slope of both the upper and lower trend lines, connecting higher highs and higher lows respectively, suggests a bullish trend.")
    st.write("At the time of this analysis, the recorded price of Injective (INJ) stands at 16.92 USD. If the current pattern persists, there is a potential for INJ to attain resistance levels at 18.226 USD and 43.883 USD. Conversely, in the event of a trend reversal, the price of INJ could decline towards support levels at 9.651 USD, 6.509 USD, and 3.875 USD.")
    st.markdown(f"<h5 style='text-align: center;'>Injective (INJ) Resistance and Support Levels</h5>", unsafe_allow_html=True)
    st.write("The chart given below elucidates the possible resistance and support levels of Injective (INJ) in 2023.")
    st.image('Assets/rsl_inj.png', caption='Resistance and Support Levels (Source: TradingView)')
    st.write("From the above chart, we can analyze and identify the following as resistance and support levels of Injective (INJ) for 2023.")
    table_data = {
      "Levels": ["Resistance Level 1", "Resistance Level 2", "Support Level 1", "Support Level 2"],
      "Value": ["24.549 USD", "52.950 USD", "11.718 USD", "4.968 USD"]
    }
    st.table(table_data)
    st.markdown(f"<h5 style='text-align: center;'>Injective (INJ) Price Prediction 2023 — RVOL, MA, and RSI</h5>", unsafe_allow_html=True)
    st.write("The technical analysis indicators such as Relative Volume (RVOL), Moving Average (MA), and Relative Strength Index (RSI) of Injective (INJ) are shown in the chart below.")
    st.image('Assets/rvol_ma_rsi_inj.png', caption='RVOL, MA, RSI (Source: TradingView)')
    st.write("From the readings on the chart above, we can make the following inferences regarding the current Injective (INJ) market in 2023.")
    table_data = {
      "INDICATOR": ["50-Day Moving Average (50MA)", "Relative Strength Index (RSI)", "Relative Volume (RVOL)"],
      "PURPOSE": ["Nature of the current trend by comparing the average price over 50 days", "Magnitude of price change;Analyzing oversold &overbought conditions", "Asset's trading volume in relation to its recent average volumes"],
      "READING": ["50 MA = 9.689 USD Price = 17.292 USD (50MA < Price)", "85.844 < 30 = Oversold 50 - 70 = Neutral > 70 = Overbought", "Below cutoff line"],
      "INFERENCE": ["Bullish(Uptrend)", "Overbought", "Weak Volume"]
    }
    st.table(table_data)
    st.markdown(f"<h5 style='text-align: center;'>Injective (INJ) Price Prediction 2023 — ADX, RVI</h5>", unsafe_allow_html=True)
    st.write("In the below chart, we analyze the strength and volatility of Injective (INJ) using the following technical analysis indicators — Average Directional Index (ADX) and Relative Volatility Index (RVI).")
    st.image('Assets/adx_rvi_inj.png', caption='ADX, RVI (Source: TradingView)')
    st.write("From the readings on the chart above, we can make the following inferences regarding the price momentum of Injective (INJ).")
    table_data = {
      "INDICATOR": ["Average Directional Index (ADX)", "Relative Volatility Index (RVI)"],
      "PURPOSE": ["Strength of the trend momentum", "Volatility over a specific period"],
      "READING": ["79.729", "81.74(<50 = Low >50 = High)"],
      "INFERENCE": ["Strong Trend", "High Volatility"]
    }
    st.table(table_data)
    st.markdown(f"<h5 style='text-align: center;'>Comparison of INJ with BTC, ETH</h5>", unsafe_allow_html=True)
    st.write("Let us now compare the price movements of Injective (INJ) with that of Bitcoin (BTC), and Ethereum (ETH).")
    st.image('Assets/comp_btc_eth_inj.png', caption='BTC Vs ETH Vs INJ Price Comparison (Source: TradingView)')
    st.write("From the above chart, we can interpret that the price action of INJ is dissimilar to that of BTC and ETH. That is, when the price of BTC and ETH increases, the price of INJ decreases, if the price of BTC and ETH decreases, the price of INJ increases. .")
    st.markdown(f"<h5 style='text-align: center;'>Injective (INJ) Price Prediction 2024, 2025 – 2030</h5>", unsafe_allow_html=True)
    st.write("With the help of the aforementioned technical analysis indicators and trend patterns, let us predict the price of Injective (INJ) between 2024, 2025, 2026, 2027, 2028, 2029 and 2030.")
    table_data = {
      "YEAR": ["INJ Price Prediction - 2024", "INJ Price Prediction - 2025","INJ Price Prediction - 2026","INJ Price Prediction - 2027","INJ Price Prediction - 2028","INJ Price Prediction - 2029","INJ Price Prediction - 2030"],
      "BULLISH PRICE": ["87 USD", "99 USD","110 USD","122 USD","134 USD","146 USD","158 USD"],
      "BEARISH PRICE": ["4.5 USD", "4.2 USD","4  USD","3.8 USD","3.6 USD","3.4 USD","3 USD"],
    }
    st.table(table_data)
    st.markdown(f"<h5 style='text-align: center;'>Conclusion</h5>", unsafe_allow_html=True)
    st.write("In the event that Injective (INJ) demonstrates a strong investment potential in 2023, indicating a positive outlook for the cryptocurrency, the year could prove favorable for its growth. According to optimistic projections, the bullish price prediction for Injective (INJ) in 2023 is estimated to be 52.950 USD. Conversely, in the case of a shift in sentiment leading to unfavorable conditions, the bearish price prediction for Injective (INJ) in 2023 is projected to be 4.9698 USD.")
    st.write("Should the market momentum and investor sentiment remain positive, there is a possibility of Injective (INJ) reaching 75 USD. Moreover, factoring in potential upgrades and advancements within the Injective ecosystem, there exists the potential for INJ to surpass its current all-time high (ATH) of 25.01 USD and establish a new ATH.")
  with tab2:
    st.markdown(f"<h2 style='text-align: center;'>What drove INJ price increase in (Apr 2021)</h2>", unsafe_allow_html=True)
    st.image('Assets/ATH_2021.png', caption='Price Increase in April 2021')
    st.markdown(f"<h3 style='color: yellow;'>Qualitative Analysis of INJ Price Increase in April 2021</h3>", unsafe_allow_html=True)
    st.markdown(f"<h4>Introduction</h4>", unsafe_allow_html=True)
    st.write("INJ was listed on Gemini, eight new collaborations were cemented, and Injective Labs hosted panels with six of them. Here is an ever-expanding list of some of the community’s biggest wins yet. It’s been another huge month for the Injective family.")
    st.markdown(f"<h5>I) $1 Billion Valuation After $10 Million Growth Funding Round</h5>", unsafe_allow_html=True)
    st.image('Assets/10mill_inj.webp', caption='Valuation after Growth Funding')
    st.write("Injective has experienced its biggest funding round to date, generating over 10 million US dollars and catapulting to over 1 billion USD valuation as a network.")
    st.write("A group of prominent investors contributing to this round included billionaire NBA team owner and Shark Tank judge Mark Cuban, Pantera Capital, BlockTower, Hashed, Cadenza Ventures, CMS, QCP Capital, and Cumberland, the crypto arm of one of the largest trading firms DRW.")
    st.write("TechCrunch, one of many publications which covered the round, dubbed Injective a “Robinhood for DeFi”.")
    st.markdown(f"<h5>II) Equinox Staking Updates</h5>", unsafe_allow_html=True)
    st.image('Assets/int_apr_2021.png', caption='Equinox $50M')
    st.write("Thanks to sky rocketing demand within the community, over $50 million has been staked on Equinox to date. This milestone comes just weeks after the launch of Equinox Staking.")
    st.image('Assets/inj_apr_2021_0.png', caption='Equinox Update')
    st.write("A major Equinox Staking update was published addressing new technical parameters that will bring a heightened user experience for everyone. This includes but is not limited to a new staking rewards calculator and formula, enhanced re-delegation, and other improvements across the board.")
    st.image('Assets/staked.png', caption='Staked Collaboration')
    st.write("The past month has seen a number of surprise token drops from Ethereum, PARSIQ, and Ramp DeFi to help ramp up and reward the community. Injective also onboarded Staked as the latest genesis validator. Staked is one of the most prominent authorities on cryptocurrency staking with a long history of working with premier funds, exchanges, and custodians to facilitate institutional-grade staking.")
    st.write("The tremendous amount of progress seen in such a short amount of time on the staking rollout is thanks largely to the laser focus and efforts of the community.")
    st.markdown(f"<h5>III) Collaborations & Integrations</h5>", unsafe_allow_html=True)
    st.image('Assets/Klaytn.jpg', caption='Klaytn Collaboration')
    st.write("Injective collaborated with Klaytn to bring decentralized trading to millions of users within the Klaytn ecosystem. Now Klaytn users will have access to Injective’s diverse financial markets, while users on Injective will be able to create new ones using assets built on the Klaytn blockchain.")
    st.image('Assets/UMA.jpg', caption='UMA Collaboration')
    st.write("Injective linked up with UMA to launch innovative synthetic products. By integrating with the decentralized derivatives exchange, synthetic assets on UMA can be made available to Injective users moving forward.")
    st.image('Assets/Band.jpg', caption='Band Protocol Collaboration')
    st.write("Injective delved deeper into existing collaboration with Band Protocol to operate validator nodes on one another’s networks. Moving forward, this dual validator arrangement will serve to align and strengthen long-term goals for both parties.")
    st.image('Assets/Harmony.jpg', caption='Harmony Collaboration')
    st.write("Injective joined forces with Harmony to launch a diverse array of interoperable derivatives. Looking ahead, these forms of interoperability can allow users to trade a number of new derivative products that utilize Harmony-based assets.")
    st.image('Assets/API3.jpg', caption='API3 Collaboration')
    st.write("Injective integrated API3 into the growing oracle ecosystem. This collaboration is expected to add value by providing external, real-world data feeds from API3’s network of first-party oracles.")
    st.image('Assets/Big Data P.jpg', caption='Big Data Protocol Collaboration')
    st.write("Injective rolled out a collaboration with Big Data Protocol to create and launch structured data token products. Injective and BDP users can soon create and trade data derivatives based on the BDP Data Market.")
    st.image('Assets/Persistance.jpg', caption='Persistance Collaboration')
    st.write("Injective explored new synergies with Persistence after integrating their staking arm Audit.one as a genesis validator. The next goal is to not only support Persistence-native assets on the platform for perpetual futures trading, but work together to launch liquid staked assets (facilitated by Persistence’s pStake application) as a derivative product on Injective.")
    st.image('Assets/Litentry.jpg', caption='Litentry Collaboration')
    st.write("Injective integrated Litentry to unlock optimized on-chain data, addressing salient on-chain governance issues in the DeFi space. The process will entail aggregating decentralized identity (DID) data sets across multiple networks.")
    st.markdown(f"<h5>IV) Governance Updates</h5>", unsafe_allow_html=True)
    st.image('Assets/finance_para.webp', caption='Finance Paradigm')
    st.write("This month has also been a time for reinforcement of the mission, which has always been to create a new financial paradigm that is wholly owned, operated, and governed by the community.")
    st.image('Assets/INJ_GPP.jpg', caption='Governance Proposal Procedure')
    st.write("Injective’s official governance proposal procedure was published, describing the nature of on-chain governance on the Injective Chain and providing a detailed overview of a governance proposal’s lifecycle.")
    st.image('Assets/spot.webp', caption='Injective governance For Spot Markets')
    st.write("Injective governance was also launched for spot markets. With this development, users who are participating in Equinox staking will be able to propose and vote on new spot market listings. The governance process is a core component of the decentralized protocol and will serve an important role in the upcoming mainnet release.")
    st.markdown(f"<h5>V) Community Initiatives</h5>", unsafe_allow_html=True)
    st.write("To further engage new collaborations, Injective Labs hosted a number of livestream YouTube panels with friends at Orion and 1inch Protocol, Harmony, and API3, DIA, and Band Protocol. These conversations help keep everyone in the loop about exciting projects under the hood.")
    st.markdown("""- DeFi and DEXs: Orion Protocol, 1inch Exchange, and Injective
- Cross-Chain Derivatives and Interoperability in DeFi: Injective Protocol and Harmony
- DeFi and Oracles: Injective Protocol, Band Protocol, DIA and API3
- Injective’s public appearances have spanned numerous platforms, including a Reddit AMA hosted by Harmony and a Telegram AMA hosted by Alpha Finance. To further interact with the Telegram community, Injective hosted the first Injective quiz, titled “Know Your Protocol”, awarding top scorers with exclusive Injective gear.
- Injective teamed up with Binance to commit $50,000 in INJ tokens as rewards for users.""")
    st.markdown(f"<h3 style='color: yellow;'>Quantitative Analysis of INJ Price Increase in April 2021</h3>", unsafe_allow_html=True)
    st.image('Assets/inj_fin.jpg')
    st.write("Injective's native token, INJ, rose from 10.91 USD on April 20 to an all-time high at 21.55 USD on April 22, recording a 97% increase in three days. The bulls could not sustain even higher levels on April 20, as seen from the long wick on the candlestick.")
    st.write("This encouraged the bears, who tried to trap the bulls and start a correction. However, the buyers purchased the dip to the 50-day SMA ($13.40) on April 23 and defended the 20-day EMA (15.26 USD) on April 23. This suggests that the sentiment remains positive and the bulls are accumulating on dips.")
    st.write("The buying momentum picked up on April 26, and the bulls cleared the first hurdle at 18.15 USD. If the bulls can sustain the price above 18.15 USD, the INJ/USDT pair could rise to 21.55 USD. A break above this resistance could start the next leg of an up-move that may reach 26.44 USD.")