# Gala_Token_analysis.py
import streamlit as st
from PIL import Image
import pandas as pd



def overview_page():

    
    img=Image.open("C:\\Users\\HARSHA\\Downloads\\gala_logo.jpg")
    #st.image(img,output_format='auto')
    st.columns(3)[1].image(img)

   
    
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>GALA Token Analysis</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div style="text-align: center;">
            <h2>Overview</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("## The gaming industry")
    st.write("Echoing the momentum of GameFi (gaming and finance) and the great success of Axie Infinity, Gala Games was launched in 2019 to pursue technology development and innovation in play-to-earn (P2E) blockchain gaming. The global market size of blockchain gaming exceeded 4.6 billion dollar in 2022 and is expected to reach around 65.7 billion dollar by 2027, establishing itself as one of the most promising sectors revolutionized by blockchain technology.")
    st.write("""### What is Gala?""")
    st.write("The 'GALA' token is the digital utility token of the Gala Games and Entertainment ecosystem. The goal of introducing 'GALA' is to provide a convenient and secure method of payment and settlement between participants who interact within the Gala Games and Entertainment ecosystem.")
    #st.image("path_to_overview_image.png", use_column_width=True)  # Replace with the actual path to your overview image

    st.markdown("## GALA Games")
    img=Image.open("C:\\Users\\HARSHA\\Downloads\\games.jpg")
    st.columns(3)[1].image(img)
    
    # Set background color to snow blue
    st.markdown(
        """
        <style>
        .gala-music-box {
            background-color: #f2f4f8;
            padding: 20px;
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # GALA game content inside the styled box
    st.markdown(
        """
        <div class="gala-music-box">
            <p>Gala Games was created by industry leading game developers who came together to bring value back to the players with the help of Web3 and blockchain tech. Its founders saw major problems with the way today’s leading game publishers demand that players continually spend to keep enjoying a game they love. Scrapping the old model, Gala is creating a huge platform with AAA-level games (many free to play) designed to give players more freedom, control, and rewards than ever.Since its launch, Gala Games has grown exponentially, with an ever-expanding roster of games and a vibrant community of players. The ecosystem has attracted talented developers and game creators, further enriching the gaming experience offered by the platform.</p>
            <p>Their primary objective was to decentralize the gaming industry and serve a diverse range of gamers seeking a robust shift in the way gaming operated_</p>
        </div>
        """,
        unsafe_allow_html=True
    )


    # GALA music Section
    st.markdown("## GALA Music")
    img=Image.open("C:\\Users\\HARSHA\\Downloads\\gala_music.jpg")
    st.columns(3)[1].image(img)
    
    st.markdown(
        """
        <style>
        .gala-music-box {
            background-color: #f2f4f8;
            padding: 20px;
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # GALA Music content inside the styled box
    st.markdown(
        """
        <div class="gala-music-box">
            <p>In the world of Music, there has been a substantial disconnect between the artists and their supporters. Instead of selling a song to fans directly, artists have to partner up with a record label or various streaming services to gain traction. Unfortunately, these services often give the artist very little back in revenue. Furthermore, some of the most popular platforms require a monthly subscription fee without allowing users to own the songs. Artists may also need to provide exclusivity to a particular streaming platform which limits their audience.</p>
            <p>While this may be convenient, Gala Games and Entertainment is providing an alternative through Blockchain. Artists can now sell their music directly to their supporters. In addition, their fans can own an original copy of the song as an NFT, and the NFTs have more benefits than just owning a physical copy. </p>
            <p>One of the remarkable things people can do is participate in Listen and Earn, made possible through a decentralized music streaming platform. Node owners, NFT owners, and listeners, can all participate in this ecosystem to support artists, earn rewards and engage with their favorite artists in ways they could never do before. </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    #White paper
    st.write("**White paper**")
    def create_download_link(label, filename):
        download_link = f'<a href="{filename}" download="{label}">{label}</a>'
        return download_link

# Create a link to download the PDF
    pdf_link = create_download_link("Download PDF", "C:\\Users\\HARSHA\\Downloads\\Gala_Music_Whitepaper.pdf")

# Display the link using st.markdown
    st.markdown(pdf_link, unsafe_allow_html=True)

    # GALA Games Section
    st.markdown("## GALA Films")
    img=Image.open("C:\\Users\\HARSHA\\Downloads\\gala_film.jpg")
    st.columns(3)[1].image(img)
    st.markdown(
        """
        <style>
        .gala-music-box {
            background-color: #f2f4f8;
            padding: 20px;
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # GALA Music content inside the styled box
    st.markdown(
        """
        <div class="gala-music-box">
            <p>Like music, the film industry has also had its share of problems. Films and shows have been widely available to watch on DVDs or Blu-rays.</p>
            <p>Gala Games and Entertainment strives to develop an alternative to the current system. Film creators will be able to sell their content directly to supporters and allow them to access unique experiences. Like Music, Gala Film will have a Watch and Earn ecosystem that will enable creators to, Node Operators, Owners, and Supporters to enjoy, earn rewards and benefit from it. This is possible due to the integration of Blockchain technology and the Gala Node ecosystem.</p>
        </div>
        """,
        unsafe_allow_html=True
    )


    

def tokenomics_page():
    st.markdown(
        """
        <div style="text-align: center;">
            <h2>GALA Tokenomics</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("""### Key Metrics""")
    st.write("Note: Metrics was recorded on 14th Dec 2023,data points could be different on the date you read this.")
    
    def display_crypto_data():
        data = {
            "Metric": ["Market Cap (Ranked-74)", "Volume (24h)(Ranked-77)", "Volume/Market Cap (24h)", "Circulating Supply", "Total Supply", "Max. Supply", "Fully Diluted Market Cap"],
            
            "Value": ["$849,595,109(+6.43%)", "$117,741,432(+6.22%)", "13.18%", "26,647,198,927 GALA", "28,676,359,063 GALA", "50,000,000,000 GALA", "$1,588,861,250"],
            
        }

        df = pd.DataFrame(data)
            
        st.markdown(
            """
            <style>
            .snow-blue-background {
                background-color: #f2f4f8;
                padding: 10px;
                border-radius: 10px;
            }
            </style>
            """,
            unsafe_allow_html=True
            )

        # Display the DataFrame with snow blue background and without the Percentage Change column
        st.table(df.style.set_properties(**{'background-color': '#f2f4f8'}))
    

# Main part of the app
    st.write("""#### Crypto Data Table""")
    display_crypto_data()

    #All time high
    st.write("""### All Time High Data""")
    
    # Set background color to snow blue
    st.markdown(
        """
        <style>
        .snow-blue-background {
            background-color: #f2f4f8;
            padding: 20px;
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display "All Time High Data" with snow blue background
    st.markdown(
        """
        <div class="snow-blue-background">

            - All Time High (ATH) Price: $0.8367 
            - All Time High (ATH) Date: Nov 26, 2021 (2 years ago)
            - All Time High (ATH) Change: -96.11% 
        </div>
        """,
        unsafe_allow_html=True
    )
    img=Image.open("C:\\Users\\HARSHA\\Pictures\\Screenshots\\Screenshot 2023-12-14 180544.png")
    st.image(img,caption="All time high data graph  credit=coin market cap",use_column_width=True)
    #Token holder
    st.write("""### Token Holders""")

    st.markdown(
        """
        - The top 100 holders collectively own 73.96% (21,210,762,567.55 Tokens) of Gala.
        - Total Token Holders: 215,548
        """
    )
    img=Image.open("C:\\Users\\HARSHA\\Pictures\\Screenshots\\Screenshot 2023-12-14 214013.png")
    st.image(img,caption="Top 100 Gala Token holders  credit=Etherscan.io",use_column_width=True)


    st.write("""### Market cap""")
    st.write("""##### Gala is 6th among 28 gaming tokens""")
    img=Image.open("C:\\Users\\HARSHA\\Pictures\\Screenshots\\top gaming token by marketcap.png")
    st.image(img,caption="Preview of Top gaming token by marketcap ",use_column_width=True)

    #need to add image here

    #historical token price

   #The tokenomics
   
    st.write("""### GALA Allocation""")

    st.write(
        "$GALA tokens are initially minted as Node rewards from Gala Games Founder’s Nodes operators. "
        "This reward is split 50:50 between Founder's Node Operators and the Gala Conservativeship."
    )


    st.write("""### GALA Supply and Emission""")

    st.write(
        "- Max total supply: 50 Billion.\n"
        "- Daily emissions depend on Circulating Supply, reduced when burned or used in ecosystem activities.\n"
        "- Dynamic daily emission rate based on totalSupply.\n"
        "- Emission tranches based on totalSupply, with decreasing rates."
    )

    st.write("""### GALA Funding""")

    st.write(
        "$GALA emission to Founder’s Nodes started on September 11, 2020, with no token sale. "
        "The project was independently funded with no investment rounds."
    )


    st.write("""### GALA Supply""")

    st.write(
        "Approximately 2B $GALA are reserved by the Gala Games team. On May 15, 2023, they burned approximately 20.9B tokens, "
        "reinforcing transparency and sustainability commitments."
    )


    st.write("""### GALA Utility""")

    st.write(
        "- Used as gas token on Gala Games’ Layer-1 blockchain, GalaChain.\n"
        "- All $GALA used as gas is burned.\n"
        "- $GALA is used for transactions and NFT purchases, resulting in burned tokens."
    )


    st.write("""### GALA Founder’s Nodes""")
    st.write(
        "- 50,000 Founder’s Nodes power Gala Games.\n"
        "- Run by licensed operators, receiving a portion of daily $GALA distribution.\n"
        "- Operators vote on ecosystem decisions via Gala Games Node software.\n"
        "- Active Founder’s Node operators may receive a portion of NFTs minted for the gaming ecosystem."
    )
    st.write("""## Analysis""")
    st.markdown("- A sudden increase in volume might indicate a surge in interest, news, or significant price movement.")
    st.markdown("- In 2023, the token's performance has shown some improvement, although it still remains far from its peak period in late 2021.The token's value rose to 0.0624 at the end of January this year. However, following this surge, the price experienced a downturn. A notable low point occurred during the start of June when the token's value dropped to 0.01879.")
    st.markdown("- Below is the data for the number tokenholders by the amount they invest and for the time they hold the tokens over a period of 3 months ")
    img=Image.open("C:\\Users\\HARSHA\\Downloads\\hhh.png")
    st.image(img,use_column_width=True)
    st.write("**Moving Average and Bollinger Bands**")
    st.write("- Rolling Mean: Smoothens short-term fluctuations in Gala token prices, revealing underlying trends.")
    st.write("- Bollinger Bands: Helps identify potential reversal points and measures price volatility.Consists of an upper and lower band around the rolling mean.")
    st.write("**Plot with Rolling Mean and Bollinger Bands**")
    st.write("- Overlays Gala token closing prices with the rolling mean and Bollinger Bands.")
    st.write("- Aids in identifying potential buy/sell signals based on the deviation from the rolling mean.")
    img=Image.open("C:\\Users\\HARSHA\\Downloads\\Screenshot 2023-12-16 120929.png")
    st.image(img,caption="Data from Dec14 2021-Dec 12 2023",use_column_width=True)

def governance_mechanism_page():
    st.markdown(
        """
        <div style="text-align: center;">
            <h2>Governance Mechanism</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("Gala places a strong emphasis on community involvement and decentralized governance. Through on-chain voting and proposals, GALA token holders can actively participate in shaping the future of the platform.")
    st.write("One of the features the Gala team promotes is incentivizing players to run their own nodes for an opportunity to earn the GALA cryptocurrency, limited edition NFTs and the chance to contribute to the growth of the ecosystem. To operate their own node, users must buy a license for roughly $100.The Gala Games platform is run by a distributed network of nodes ensuring decentralization rather than a central server controlled by a single entity. These nodes offer their computational resources to contribute to the ecosystem, vote on community proposals, and help guide the network’s development.")
    st.write("Gala network consensus voting is only available to Founder node operators. The majority of proposals will be about which games to add to the Gala Games platform, but there are other types of votes as well. Learn more about the governance process")
    st.write("Triple Proof Node System: Gala uses a hybrid consensus mechanism, which incorporates **Proof-of-Work (PoW)**, **Proof-of-Stake (PoS)**, and **Proof-of-Storage**. The network is supported by three distinct node types which are the Founder nodes, Paid nodes, and Free nodes.")
    st.write("There are four main types of nodes that power Gala’s network. These nodes are owned by users that supply computational power needed to run the games hosted by Gala and are rewarded with GALA and/or NFTs for their contributions.")
    st.markdown(
        """
        <style>
        body {
            background-color: #f2f4f8;
        }
        .snow-blue-background {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.write("""### Founder’s Nodes""")
    st.markdown(
        "- Allow owners to vote on the evolution of the project by using GALA.\n"
        "- Only 50,000 Founder Nodes are available and can be purchased from Gala using the GALA token.",
        unsafe_allow_html=True
    )

    st.write("""### Game Nodes""")
    st.markdown(
        "- Users who host gaming servers may be granted special allowances and considerations in the games they support (NFTs, ability to invite other players, etc.).",
        unsafe_allow_html=True
    )

    st.write("""### Player Nodes""")
    st.markdown(
        "- Decentralized music players that allow network listeners to play and share music in the form of NFTs.",
        unsafe_allow_html=True
    )

    st.write("""### Film Nodes""")
    st.markdown(
        "- Host entertainment and film experiences, analogous to Player Nodes.",
        unsafe_allow_html=True
    )
    img=Image.open("C:\\Users\\HARSHA\\Pictures\\Screenshots\\gala_nodes_governance.png")
    st.image(img, use_column_width=True)
    

    
def revenue_model_page():
    st.markdown(
        """
        <div style="text-align: center;">
            <h2>Revenue Model and Fee structure</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Game Sales and NFTs:")
    st.markdown("Gala Games generates revenue through the sale of blockchain-based non-fungible tokens (NFTs) associated with in-game items, characters, and assets. These NFTs can be bought, sold, and traded on the Gala Games platform, often using the Gala token (GALA) as the native cryptocurrency.")

    st.subheader("Platform Fees:")
    st.markdown("Gala Games charge fees on transactions that occur within its platform. This can include fees on the sale and transfer of NFTs, as well as other in-platform transactions.")

    st.subheader("Play-to-Earn Mechanisms:")
    st.markdown("Some games on the Gala Games platform may incorporate play-to-earn mechanisms, allowing players to earn cryptocurrency or other rewards by participating in the game. Gala Games may take a percentage of these earnings as part of its revenue model.")

    st.header("Gala Games Fee Structure")

    st.subheader("Transaction Fees:")
    st.markdown("Gala Games charge transaction fees on various activities within its platform, such as the buying and selling of NFTs or other in-game assets. These fees contribute to the platform's revenue.")

    st.subheader("Development and Publishing Fees:")
    st.markdown("Game developers on the Gala Games platform may have specific agreements regarding revenue sharing and fees. Gala Games may take a percentage of the revenue generated by developers through the sale of in-game items, NFTs, and other transactions.")

    st.subheader("GALA Token Utility:")
    st.markdown("The Gala token (GALA) is the native cryptocurrency of the Gala Games ecosystem. Fees and payments within the platform may be denominated in GALA, and holding GALA tokens may confer certain benefits or discounts.")
def project_milestone_page():
    img=Image.open("C:\\Users\\HARSHA\\Downloads\\792774 (1).jpg")
    st.columns(3)[1].image(img)
    st.markdown(
        """
        <div style="text-align: center;">
            <h2>Significant Project Milestone</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.write("""### Gala Games Platform""")

    st.write("The platform officially launched in 2019 and quickly gained popularity among gamers and blockchain enthusiasts.")

    st.write("""#### Revolutionizing the Gaming Industry:""")
    st.markdown(
        "- The team includes brilliant minds behind popular titles such as Command and Conquer, Doom, Unreal, Halo, Left 4 Dead, Call of Duty, and many more.\n"
        "- Gala has 19 live games, and over 40 titles in development, covering 22 game genres.\n"
        "- As of this year’s plan, Gala has committed in excess of $300M to game projects, 50% of which has already been deployed."
    )


    st.write("""### GALA Music""")

    st.write("GALA Music is becoming a home for music discovery and emerging talent. This is built on the Gala chain.")
    st.markdown(
        "- GALA Music token is separate from $GALA, set to launch soon.\n"
        "- 32 artists have already been released.\n"
        "- 500+ artists are waiting to get on the platform.\n"
        "- 150+ tracks can be streamed."
    )


    st.write("""### Gala Film""")

    st.write("Gala Film was launched during Galaverse 2022 and currently has 7 titles in flight.")
    st.markdown(
        "- 2.6K early Gala film content holders.\n"
        "- Launch of the Cinema club.\n"
        "- RZR marks Gala Film’s debut project, setting a new standard in how entertainment is presented to global audiences."
    )


    st.write("""### GalaChain (Project GYRI)""")

    st.markdown(
        "- GalaChain is specifically designed to handle the transaction throughput needed for games to grow and scale.\n "
        "- While providing provable and verifiable ownership to token holders. With the ability to scale horizontally to handle.\n "
        "- An infinite number of games, GalaChain is designed to be the backbone of the Gala Games and Entertainment ecosystem."
    )
    
    

def risk_evaluation_page():
    img=Image.open("C:\\Users\\HARSHA\\Downloads\\OIP (1).jpg")
    st.columns(3)[1].image(img)
    st.markdown(
        """
        <div style="text-align: center;">
            <h2>Risk Evaluation</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.write("""### Market Sentiment""")

    st.write(
        "Market sentiment refers to the overall attitude or perception of investors and traders towards a particular cryptocurrency or asset. "
        "Market sentiment can play a critical role in determining its price predictions. Positive news and developments in the gaming industry or the blockchain ecosystem, in general, can drive demand and push up the price. Any negative news can impact the growth."
    )

    st.write(
        "Overall, GALA has a surprisingly good risk: reward ratio at 1.91 – however, this is overshadowed by the potential damage and disruption liable to stem from the unfurling legal drama."
    )

    st.write(
        "“Gala Games co-founders’ legal battle over token allegations”"
    )

    st.write(
        "As the legal battles escalate, Gala Games faces an uncertain future, with accusations of token theft, corporate mismanagement, and waste casting a shadow over the project."
    )


    st.write("""### Competition""")

    st.write(
        "The gaming industry is highly competitive, and there are other blockchain-based gaming platforms that GALA competes with. "
        "In addition to other blockchain-based gaming platforms, GALA also competes with traditional gaming platforms. As a result, if GALA is unable to differentiate itself from traditional gaming platforms or compete with other blockchain-based gaming platforms, it may struggle to gain adoption and could experience a decrease in demand for its tokens, leading to a decline in its price."
    )
    img=Image.open("C:\\Users\\HARSHA\\Downloads\\Screenshot 2023-12-16 102313.png")
    st.image(img,caption="Comparison with AXS over a period of 1 month",use_column_width=True)


    st.write("""### GALA Tokens and Gala Music Tokens""")

    st.write(
        "As Gala is set to launch its music tokens separate from its $GALA tokens, it is creating confusion among users and adopters. "
        "This clearly needs to be addressed so that users understand why Gala Music needs its own token to meet its utility needs."
    )


    st.write("""### Regulation""")

    st.write(
        "The regulatory environment around cryptocurrencies and blockchain technology is constantly changing and evolving, and any changes in regulations or government policies can impact the price of GALA."
    )

    st.write(
        "For example, if a government were to introduce strict regulations on cryptocurrencies, it could potentially limit the adoption of GALA’s platform and lead to a decrease in demand for GALA tokens."
    )


    st.write("""### Burn and Re-make Process of Gala""")

    st.write(
        "Token supply is an important factor that can impact the price of cryptocurrencies, including GALA. A cryptocurrency’s supply is the total number of tokens or coins in circulation, and it plays a crucial role in determining its price."
    )

    st.write(
        "There seems to be confusion among users as well as influencers on social media regarding the burn and mint process of Gala tokens, which is creating misinterpretation of max supply and the circulating supply in the market. This can be issued to maintain the transparency of the process and build trust."
    )
    
    img=Image.open("C:\\Users\\HARSHA\\Pictures\\Screenshots\\Screenshot 2023-12-15 123526.png")
    st.image(img,use_column_width=True)

def future_prospects_page():
    
    st.markdown(
        """
        <div style="text-align: center;">
            <h2>Future Prospects</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write(
        "Looking ahead, Gala Games has an ambitious roadmap with exciting developments planned for the ecosystem. "
        "This includes the launch of several upcoming games for desktop and mobile users. Genres for these games will include RPG, survival, strategy, tabletop, and more."
    )

    st.markdown(

        "- In 2023, the performance of the token has shown some improvement, although it remains far from its peak period in late 2021.The announcement in January about Gala Films, the movie division of the company, working on projects with renowned Hollywood actors Dwayne “The Rock” Johnson and Mark Wahlberg, led to a significant price increase. "
     )
    st.write("- The token’s value rose to $0.06241 on January 28. However, following this surge, the price experienced a downturn. A notable low point occurred on June 10, when the token’s value dropped to '0.01879'."
     )
    st.write("- This decline coincided with news of Crypto.com suspending its institutional operations in the United States. Despite these challenges, the token has shown signs of recovery, reaching approximately '0.035' in recent weeks."
    )

    
    
    st.subheader("Gala in Metaverse")
    
    img=Image.open("C:\\Users\\HARSHA\\Downloads\\Screenshot 2023-12-16 104016.jpg")
    st.image(img,use_column_width=True)

    st.markdown(
        "- VOX, Gala's metaverse IP, will bring games, music, and film together.The VOX's highest priority is the building of VOXverse, a dynamic metaverse designed through a partnership with the legendary creator of The Sims, Will Wright."
     )
    st.write("- The potential resurgence of the metaverse could favorably impact the token, but whether this will materialize is yet to be determined."
    )

    st.subheader("Partnerships")

    st.markdown(
        "- Gala Chain levels up by Partnering with DWF Labs for Ecosystem Growth. This new strategic partnership will usher in a new phase of rapid growth for the adoption of our L1, GalaChain. "
    )
    st.write("- DWF Labs is a well-known and worldwide digital asset market maker, as well as a multistage web3 investment firm."
    )

    st.write(
        "- Gala predicts to hit 1 billion users soon using GalaChain, where they are not limiting themselves to game or entertainment but multiple industries, like travel, manufacturing, health care, and social media (to only name a few).1 billion users could be a mere stepping stone."
    )
    st.write("Tweet link: ")

    tweet_html = f'<blockquote class="twitter-tweet"><p lang="en" dir="ltr">.<a href="https://twitter.com/DWFLabs?ref_src=twsrc%5Etfw">@DWFLabs</a> 🤝<br><br>Let&#39;s build some cool stuff together!<a href="https://t.co/qq5J1rAzoI">https://t.co/qq5J1rAzoI</a></p>&mdash; Gala Games (@GoGalaGames) <a href="https://twitter.com/GoGalaGames/status/1722694641617908216?ref_src=twsrc%5Etfw">November 9, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'
# Display the embedded tweet using st.markdown
    st.markdown(tweet_html, unsafe_allow_html=True)

    st.subheader("Gala Chain Academy")

    st.write(
        "Gala is planning to launch the Gala Chain Academy for people to learn how to build on top of Gala Chain. Being decentralized and allowing people to build with Gala is critical to the long-term success of creating a broadly decentralized ecosystem.Through this, Gala is looking for new games to bring into the ecosystem."
    )
    st.subheader("Can GALA reach $1?")
    st.markdown("Thanks to its growing library of games and partnerships with major game developers, GALA is well on its way to becoming the go-to platform for cryptocurrency gaming. Considering its past performance and the fact that its value has already hit the 0.8367 level, it is very likely that Gala will reach an average price value of $1.")


def main():
    

    # Navigation
    pages = {
        "Overview": overview_page,
        "Tokenomics": tokenomics_page,
        "Governance Mechanism": governance_mechanism_page,
        "Revenue Model and Fees": revenue_model_page,
        "Project Milestone": project_milestone_page,
        "Potential Risk Evaluation": risk_evaluation_page,
        "Future Prospects": future_prospects_page,
    }

    # Sidebar with Slider and Dropdown Menu
    selected_option = st.sidebar.selectbox("Select a section for analysis", list(pages.keys()))
    

    # Display the selected page
    pages[selected_option]()

reference_websites = [
    "Coin Market Cap",
    "CoinBase",
    "Gala Support Centre",
    "CoinSutra",
    "BlockChain Reporter",
    "CoinTelegraph"
]

# Dropdown box for selecting a reference website
selected_website = st.sidebar.selectbox("List of Reference website", reference_websites)

if __name__ == "__main__":
    main()
