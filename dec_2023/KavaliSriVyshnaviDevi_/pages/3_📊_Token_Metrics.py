import streamlit as st


st.set_page_config(page_title="Token Metrics", page_icon="📊")

st.title("Token Metrics")
# Token Metrics
tvl = 7.88  # in billion
dai_supply = 5.82  # in billion
collateralization_ratio = 148
stability_fee = 2
governance_participation = {'highest_turnout': 9.2, 'average_turnout': 5.8}
number_of_vaults = {'active': 18250, 'average_per_day': 126}
vault_debt = {'total': 4.23, 'average_size': 231000}
dsr = {'current_rate': 0.42, 'total_deposited': 1.98}
mkr_token_metrics = {'circulating_supply': 988068, 'top_holders': 'Multisignature wallets, venture capital firms, and decentralized exchanges'}
smart_contract_activity = {'daily_transaction_volume': 1.27, 'most_recent_upgrade': 'October 25th, 2023'}
oracle_metrics = {'uptime': 99.99, 'latency': 2}
community_metrics = {'twitter_followers': 254000, 'forum_active_users': 1850}



# Usage Metrics
st.subheader("TVL, Dai Supply, Collateralization Ratio, Stability Fee")
st.write(f"TVL (Total Value Locked): ${tvl} billion")
st.write(f"Circulating Supply of Dai: {dai_supply} billion")
st.write(f"Collateralization Ratio: {collateralization_ratio}%")
st.write(f"Stability Fee: {stability_fee}%")

# Governance Participation
st.subheader("Governance Participation")
st.write(f"Recent Snapshot Proposal with Highest Voter Turnout: Proposal MKR-147 with {governance_participation['highest_turnout']}% of MKR circulating supply")
st.write(f"Average Voter Turnout in the Past Six Months: {governance_participation['average_turnout']}%")

# Number of Vaults
st.subheader("Number of Vaults")
st.write(f"Active Vaults: {number_of_vaults['active']}")
st.write(f"Average Vaults Created Per Day (Past Month): {number_of_vaults['average_per_day']}")

# Vault Debt
st.subheader("Vault Debt")
st.write(f"Total Outstanding Vault Debt: ${vault_debt['total']} billion")
st.write(f"Average Vault Debt Size: ${vault_debt['average_size']}")

# Dai Savings Rate (DSR)
st.subheader("Dai Savings Rate (DSR)")
st.write(f"Current DSR: {dsr['current_rate']}% (Annualized)")
st.write(f"Amount of Dai Deposited in DSR Contract: ${dsr['total_deposited']} billion")

# Maker (MKR) Token Metrics
st.subheader("Maker (MKR) Token Metrics")
st.write(f"Circulating Supply of MKR: {mkr_token_metrics['circulating_supply']} tokens")
st.write(f"Top Holders of MKR: {mkr_token_metrics['top_holders']}")

# Smart Contract Activity
st.subheader("Smart Contract Activity")
st.write(f"Average Daily Transaction Volume: ${smart_contract_activity['daily_transaction_volume']} billion")
st.write(f"Most Recent Smart Contract Upgrade: {smart_contract_activity['most_recent_upgrade']}")

# Oracle Metrics
st.subheader("Oracle Metrics")
st.write(f"Chainlink Uptime: {oracle_metrics['uptime']}%")
st.write(f"Oracle Latency: {oracle_metrics['latency']} seconds")

# Community Metrics
st.subheader("Community Metrics")
st.write(f"Twitter Followers: {community_metrics['twitter_followers']}")
st.write(f"Forum Active Users (Per Month): {community_metrics['forum_active_users']}")
