import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load AXS data
# URL of the CSV file
#data_url = 'https://github.com/nikhil-chopra-0513/AXS-analysis/blob/main/AXS%20Token/axs_price_data%20(1).csv'

# Load data from the CSV file
axs_data = pd.read_csv("AXS Token/axs_price_data (1).csv")



# Function to display overview
def display_overview():
    st.subheader('AXS Data Overview')
    st.write(axs_data.head())

# Function for mean, median, mode etc
def display_statistics():
    st.subheader('AXS Statistics')
    mean_price = axs_data['price'].mean()
    max_price = axs_data['price'].max()
    min_price = axs_data['price'].min()
    std_price = axs_data['price'].std()
    st.metric(label="Mean Price", value=round(mean_price, 2))
    st.metric(label="Max Price", value=round(max_price, 2))
    st.metric(label="Min Price", value=round(min_price, 2))
    st.metric(label="Standard Deviation", value=round(std_price, 2))
    st.line_chart(axs_data.set_index('timestamp')['price'])

# Function to display line chart
def display_line_chart():
    st.subheader('AXS Price Over Time')
    st.line_chart(axs_data.set_index('timestamp')['price'])


# Function to calculate market cap
def calculate_market_cap(df):
    timestamp_column = 'timestamp'
    price_column = 'price'

    df[timestamp_column] = pd.to_datetime(df[timestamp_column])
    df = df.sort_values(by=timestamp_column)

    df['market_cap'] = df[price_column] * df[price_column].shift(1)
    total_market_cap = df['market_cap'].sum()

    st.write('## Market Cap DataFrame:')
    st.write(df)

    st.write(f'## Total Market Cap: {total_market_cap}')

# Function to calculate total volume automatically
def calculate_total_volume_auto(axs_data):
    timestamp_column = 'timestamp'
    price_column = 'price'

    axs_data[timestamp_column] = pd.to_datetime(axs_data[timestamp_column])
    axs_data = axs_data.sort_values(by=timestamp_column)

    axs_data['timestamp_diff'] = axs_data[timestamp_column].diff().dt.total_seconds().fillna(0)
    axs_data['volume'] = axs_data['timestamp_diff'] * axs_data[price_column]
    total_volume = axs_data['volume'].sum()

    st.write('## Total Volume DataFrame:')
    st.write(axs_data[['timestamp', 'price', 'volume']])

    st.write(f'## Total Volume: {total_volume}')

#	Tokenomic

def Tokenomic():
    st.title("Axie Infinity (AXS) Token Information")

    st.markdown("The Axie Infinity (AXS) token is part of the Axie Infinity game, a play-to-earn game where players can collect pets called Axies to fight other players and earn money. The AXS token plays a crucial role in the game's ecosystem, enabling players to fully control and own the game's ecosystem. Players can vote on existing governance proposals and propose new governance decisions. They can also monetize their stake in the project's governance system by staking AXS through the staking portal.")

    st.markdown("The AXS token has a total supply of 270 million. The initial distribution of AXS tokens is as follows:")

    distribution_data = {
        "Play-to-earn": 32400000,
        "Public Sale": 29700000,
        "Staking Rewards": 16962000,
        "Ecosystem Fund": 13162500,
        "Advisors": 11700000,
        "Sky Mavis": 22275000,
        "Private Sale": 6480000
    }

    st.write("Distribution:")
    for category, amount in distribution_data.items():
        st.write(f"{category}: {amount}")
    # Create pie chart
    fig = px.pie(values=list(distribution_data.values()), names=list(distribution_data.keys()), title="AXS Token Distribution")
    st.plotly_chart(fig)



def Socil_Activities():
    st.title("Axie Infinity (AXS) Overview")

    st.markdown("Axie Infinity (AXS) is a digital pet universe built on the Ethereum blockchain. The AXS token is the ERC-20 utility token of the platform and is used for governance, staking, and payment within the game.")

    st.markdown("The level of social activity of the Axie Infinity project is assessed as Medium. This suggests that the project has a reasonable level of community engagement and interaction, but it's not as high as some other projects in the crypto space.")

    st.header("Community Activities:")
    st.markdown("- **Governance:** AXS token holders participate in governance votes, influencing the evolution of the platform.")
    st.markdown("- **Staking:** Players stake their AXS tokens to earn weekly rewards, generating income and adding to the social activity.")
    st.markdown("- **Payment:** Players use the AXS token for games and payments within the Axie Infinity universe.")
    st.markdown("- **Community Treasury:** To be launched after staking features are implemented, governed by AXS stakers.")
    
    st.header("Investment Rounds:")
    st.markdown("The Axie Infinity project has gone through various investment rounds:")
    st.markdown("- Series A round in May 2021")
    st.markdown("- Series B round in October 2021")
    st.markdown("- Funding round in April 2022")

    st.markdown("These investment rounds have attracted significant interest from the crypto community.")

    st.markdown("In conclusion, the Axie Infinity (AXS) token has a medium level of social activity, with the community actively participating in governance, staking, and payment within the game, and investing in the project through various funding rounds.")


#Governance mech

def Governance_Mechanism():
    st.title("Axie Infinity Shards (AXS) Token Overview")

    st.markdown("The Axie Infinity Shards (AXS) token is an ERC-20 governance token for the Axie Universe. AXS holders can participate in key governance votes, stake their tokens, play the game, and earn rewards. The goal of the AXS token is to align the incentives between the game players and the developers in novel and exciting ways.")

    st.markdown("The AXS token is used to incentivize players to hold on to their tokens so they can claim additional rewards. It also aims to decentralize the ownership and governance of Axie Infinity, with the vision of becoming the first game truly owned and operated by the community that plays it.")

    st.markdown("In early 2021, the Community Treasury went live. The Community Treasury receives revenues generated by Axie Infinity as well as a portion of staking rewards. This treasury will be governed by AXS stakers once the network has become sufficiently decentralized.")

    st.header("Community Treasury Inflows:")
    st.markdown("- 4.25% of all Axie NFT marketplace transactions.")
    st.markdown("- The AXS portion of the breeding fee.")
    st.markdown("- More streams will be added in the future from cosmetic sales, tournament entry fees, licensing fees, and more as new opportunities present themselves.")

    st.markdown("In the early days of Axie Infinity, staking issuance will be high, encouraging a high portion of staked AXS without requiring an additional source of funding. However, as the issuance allocation drops over time, there will need to be another source of funding to encourage a high percentage of staked AXS. This is a potential use for the Community Treasury, which will have a sustainable source of funding from fees related to Axie Infinity.")
     



    

# Main Streamlit app
def main():
    st.title('AXS Token Data Analytics')

    # Sidebar navigation
    menu_options = ['Overview', 'Price Over Time', 'AXS Statistics', 'Calculate Market Cap', 'Calculate Total Volume', 'Tokenomic', 'Social Activities', 'Governance Mechanism']
    selected_option = st.sidebar.radio('Navigation', menu_options)

    # Display selected section
    if selected_option == 'Overview':
        display_overview()
    elif selected_option == 'Price Over Time':
        display_line_chart()
    elif selected_option == 'AXS Statistics':
        display_statistics()
    elif selected_option == 'Calculate Market Cap':
        calculate_market_cap(axs_data)
    elif selected_option == 'Calculate Total Volume':
        calculate_total_volume_auto(axs_data)
    elif selected_option == 'Tokenomic':
        Tokenomic()    
    elif selected_option == 'Social Activities':
        Socil_Activities()    
    elif selected_option == 'Governance Mechanism':
        Governance_Mechanism()  
 

if __name__ == '__main__':
    main()
