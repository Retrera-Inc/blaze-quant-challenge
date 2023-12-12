import streamlit as st
from PIL import Image

def ocean_token_analysis():
    st.title("Ocean Token Analysis")

    st.header("1. Overview")
    st.write("""
    The Ocean Token is undergoing significant enhancements with the introduction of veOCEAN and the resumption of Data Farming (DF). 
    These changes aim to provide token holders with new opportunities to earn rewards through locking OCEAN and participating in data curation.
    """)

    st.header("2. Key dates")
    st.write("""
    DF will follow phases as before. When it resumes, it will be with a new “DF/VE Alpha” phase for 4 weeks. 
    “DF Beta” and “DF Main” phases will follow, as previously targeted.
    - Mon Sep 26: veOCEAN goes live. You can lock your OCEAN for veOCEAN at df.oceandao.org (linked from Ocean homepage)
    - Thu Sep 29: Counting for DF resumes. As the previous DF round was DF4 (week 4), counting will start for DF5.
    - Thu Oct 6: First ve rewards distribution to veOCEAN holders available. Rewards = DF5 payout + cut of Ocean fees. DF6 counting starts.
    - Thu Oct 13: DF6 ends, DF7 starts (DF/VE Alpha week 3)
    - Thu Oct 20: DF7 ends, DF8 starts (DF/VE Alpha week 4)
    - Thu Oct 27: DF8 ends, DF9 starts (DF Beta week 1)
    - Thu Nov 3: DF9 ends, DF10 starts (DF Beta week 2)
    - And so on, for each week
    We will iteratively improve DF over weeks and months as we evolve from Alpha to Beta to Main.
    veOCEAN holders can claim their rewards distribution via the webapp, or smart contracts directly.
    """)

    st.header("3. veOCEAN")
    
    st.subheader("3.1 veOCEAN Overview")
    st.write("""
    ve tokens have been introduced by several projects such as Curve and Balancer. These tokens require users to lock project tokens in return for ve<project tokens>.
    In exchange for locking tokens, users can earn rewards. The amount of reward depends on how long the tokens are locked for. Furthermore, veTokens can be used for voting via data asset curation.
    We are rolling out veOCEAN to give token holders the ability to lock OCEAN to earn yield, and curate data.
    """)

    st.subheader("3.2 veOCEAN Core Idea")
    st.write("""
    The core idea is: lock OCEAN for longer for higher rewards and more voting power. A locker can be passive, though they earn more if active.
    You receive proportionally more veOCEAN for longer lock times, as follows:
    lock 1 OCEAN for 1 week → get 0.0048 veOCEAN = 1 / (4 * 52) [but you only get rewards if >1 week]
    lock 1 OCEAN for 2 weeks → get 0.0096 veOCEAN = 2/ (4 * 52)
    …
    lock 1 OCEAN for 1 year → get 0.25 veOCEAN
    lock 1 OCEAN for 2 years → get 0.50 veOCEAN
    lock 1 OCEAN for 3 year → get 0.75 veOCEAN
    lock 1 OCEAN for 4 years → get 1.0 veOCEAN
    """)

    st.subheader("3.3 veOCEAN Earnings")
    st.write("""
    veOCEAN holders have earnings from two sources:
    - Community fees. Every transaction in Ocean Market and Ocean backend generates transaction fees, some of which go to the community. 
      50% of the community fees will go to veOCEAN holders; the rest will go to OceanDAO grants, etc. All earnings here are passive.
    - Data Farming: veOCEAN holders will get each weekly DF rewards allocation, except a small carveout for DF Crunch. 
      For DF rewards, veOCEAN holders can be passive, though they will earn more if active.
    """)

    image_path = "Assets/im1.jpg"
    cap = "Flow of Value"
    image = Image.open(image_path)
    st.image(image, caption=cap, use_column_width=True)
    st.header("4. Data Farming")

    st.subheader("4.1 DF Overview")
    st.write("""
    DF incentivizes for growth of data consume volume in the Ocean ecosystem. 
    It rewards OCEAN to veOCEAN holders who curate towards data assets with high consume volume. 
    DF’s aim is to achieve a minimum supply of data for network effects to kick in, and once the network flywheel is spinning, to increase growth rate.
    """)

    st.subheader("4.2 DF Schedule")
    st.write("""
    DF has these phases:
    - [completed] DF Alpha. Counting started Thu June 16, 2022. 10K OCEAN rewards were budgeted per week. 
      Rewards were distributed at the end of every week, for the activity of the previous week. It ran 4 weeks.
    - [new] DF/VE Alpha. Counting starts Thu Sep 29,2022. 10K OCEAN rewards are budgeted per week. 
      Rewards are distributed at the end of every week, for the activity of the previous week. It runs 4 weeks. 
      The aim is to test technology, learn, and onboard data publishers.
    - DF Beta. Counting starts Thu Oct 27, 2022. Rewards are up to 100K OCEAN per week. 
      It runs up to 20 weeks. The aim is to test the effect of larger incentives, learn, and refine the technology.
    - DF Main. Immediately follows DF Beta. Rewards are up to 1.6M OCEAN per week. 
      It runs for decades; at least 503.4M OCEAN total is committed.
    """)

    st.subheader("4.3 DF Reward Function")
    st.write("""
    The reward going to a veOCEAN holder for a given Ocean data asset depends on the amount of veOCEAN they allocated to the asset, 
    and how much that asset is being consumed ($ volume). Reward is:
    RFij = Sij * Cj
    where
    Sij is the amount of veOCEAN that user i has allocated to asset j
    Cj is data consume volume for asset j, in $
    veOCEAN holders receive rewards pro-rata according to RFij
    """)

    st.subheader("4.4 Data Assets that Qualify")
    st.write("""
    Data assets that have veOCEAN allocated towards them get DF rewards.
    The data asset may be of any type — dataset (for static URIs) or algorithm for Compute-to-Data. 
    The data asset may be fixed price or free price. If fixed price, any token of exchange is alright (OCEAN, H2O, USDC, ..).
    To qualify for DF, a data asset must also :
    - Have been created by Ocean smart contracts, deployed by OPF to production networks
    - Visible on Ocean Market
    - Can’t be in purgatory
    """)

    st.header("5. Evolution of OceanDAO")
    st.write("""
    With veOCEAN, OceanDAO evolves to be more like CurveDAO:
    - ve is at the heart with v = voting (in data asset curation) and e = escrowed (locked) OCEAN. 
      The longer the lockup, the more voting and rewards, which reconciles near- and long-term DAO incentives.
    - The DAO has increased bias to automation, and to minimizing the governance attack surface. 
      The 143.8M OCEAN that was originally earmarked for a DAO treasury will go into DF instead. 
      And, 143.8M OCEAN earmarked for grants will go to DF (>21.5M OCEAN remains for grants). 
      This is on top of 215.7M OCEAN previously allocated. Therefore DF now has 503.4M OCEAN allocated; this is 35.7% of total OCEAN supply (1.41B OCEAN).
    """)

    st.header("6. Walk-Through Numbers")
    st.write("""
    Update Mar 16, 2023: Please see “Ocean Data Farming Main is Here” for a more up-to-date discussion of OCEAN emission schedule and expected APYs.
    """)

    st.header("7. On Security")
    st.write("""
    veOCEAN core contracts use veCRV contracts with zero changes, on purpose: the veCRV contracts have been battle-tested for two years and have not had security issues.
    We have built a new contract for users to point their veOCEAN towards given data assets (“allocate veOCEAN”). 
    These new contracts do not control the veOCEAN core contracts at all. 
    In the event of a breach, the only funds at risk would be the rewards distributed for a single week; 
    and we would be able to redirect future funds to a different contract.
    We have an ongoing bug bounty via Immunefi for Ocean software, including veOCEAN and DF components. 
    If you identify an issue, please report it there and get rewarded.
    """)

    st.header("8. Conclusion")
    st.write("""
    veOCEAN goes live on Mon Sep 26, and Data Farming resumes three days later. 
    veOCEAN (with DF) has passive rewards for locking OCEAN for veOCEAN, and higher rewards for veOCEAN holders who actively allocate veOCEAN towards data with high Data Consume Volume (DCV).
    """)

