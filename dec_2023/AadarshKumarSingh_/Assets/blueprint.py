import streamlit as st
from PIL import Image
from .twitter import sa2

def img(file, cap):
    image_path = file
    image = Image.open(image_path)
    st.image(image, caption=cap, use_column_width=True)

def red():
    st.title("Ocean Token Ecosystem Overview")
    img("Assets/im2.jpg", "Ocean Timeline")

    # Abstract
    st.header("Abstract")
    st.write("""
    The Ocean Token project aims to level the playing field for AI and data by creating an open, permissionless, and secure data economy.
    It has entered a new phase focusing on driving data value-creation loops, targeting users in the last mile – data dapp developers, data scientists, and crypto enthusiasts.
    """)

    # Introduction
    st.header("1. Introduction")

    # Subsection 1.1
    st.subheader("1.1. Ocean Foundations")
    st.write("""
    Ocean Protocol, established in 2017, has evolved through various phases (V1 to V4) to create the foundation for an open data economy.
    The protocol has introduced features like data sovereignty, privacy via Compute-to-Data, ERC20 datatokens, Data Farming, and veOCEAN staking.
    """)

    # Subsection 1.2
    st.subheader("1.2. A New Phase: Drive Value Creation Via User Focus")
    #----------------------------------------------------------------------------
    st.subheader("Objective:")
    st.write("The primary goal is to drive data value-creation loops, emphasizing users in the 'last mile' of the data economy.")

    st.subheader("Hypothesis:")
    st.write("Sustainability and growth in the Data Economy depend on individuals making money through creating, monetizing, and reinvesting data value.")
    st.subheader("Strategy:")
    st.write("Ocean aims to be the orchestrator and tooling for complex value loops. The focus shifts towards helping users generate income through data activities.")

    st.subheader("Data Value-Creation Loop:")
    st.markdown("1. **Acquire Data:** Users obtain data through purchase or by investing money to create it.")
    st.markdown("2. **Build AI Model:** Develop AI models using acquired data.")
    st.markdown("3. **Make Predictions:** Generate predictions based on the AI model.")
    st.markdown("4. **Choose Actions:** Users take actions (e.g., buying or selling assets) based on predictions.")
    st.markdown("5. **Earn Money:** Execute actions to make money, creating a loop for reinvestment.")

    st.subheader("Focus on Decentralized Finance (DeFi) & Large Language Models (LLMs):")
    st.subheader("Analysis:")
    st.write("DeFi: Identified as the most promising and mature vertical due to quick data value creation loops.")
    st.write("LLMs: Recognized as highly promising, especially with the release of ChatGPT and increased attention to AI technologies.")

    st.subheader("Strategy:")
    st.write("Ocean core team started biasing towards DeFi and LLMs in activities, data challenges, research, and funding programs.")

    st.subheader("Scaling Strategies:")
    st.markdown("- **Loops First:** Establish sustainable data-value creation loops.")
    st.markdown("- **Scaling Efforts:** Extend technology and integrations to facilitate more capabilities for developers and data engineers.")
    st.markdown("- **Long-Term Growth:** Aim for long-term growth until Ocean becomes ubiquitous for orchestration and monetization.")
    #----------------------------------------------------------------------------
    img("Assets/im3.jpg", "Data Value-Creation Loop")
    
    # Subsection 1.3
    st.subheader("1.3. 2023+ Ocean Core Team Goals & Setup")
    st.write("""
    The Ocean core team has reorganized itself into three streams: Eagle Rays (Stream 1) for developers, Thresher (Stream 2) for data scientists, and Sailfish (Stream 3) for crypto enthusiasts.
    """)

    img("Assets/im4.jpg", "Ocean Core Team's Aim")
    # Subsection 1.4
    st.subheader("1.4. Key Performance Indicators (KPIs)")
    #------------------------------------
    st.subheader("Transition of Approach:")
    st.write("The Ocean core team has transitioned from building out a product specified by a whitepaper and annual roadmaps to doing 'whatever it takes' to drive data value creation.")

    st.subheader("Measure of Success:")
    st.write("The measure of success has shifted from 'was X built' to 'how well are metrics for the data economy growing?'")

    st.subheader("Key Metrics Tracked:")
    st.write("The main metric is data consume volume (DCV) in USD on Ocean, i.e., how much money is spent buying & consuming data and AI assets in a given time period.")
    st.write("Other key performance indicators (KPIs) include:")
    st.markdown("- Ocean transactions")
    st.markdown("- Dapps deployed using Ocean")
    st.markdown("- Data scientists using Ocean")
    st.markdown("- Assets published on Ocean")
    st.markdown("- OCEAN locked")

    st.subheader("Internal Measures:")
    st.write("The Ocean core team has set up internal measures for these metrics and will make them public when ready.")

    st.subheader("Analysis:")
    st.write("The transition in approach reflects a shift towards a more dynamic and adaptive strategy, aligning with the goal of driving data value creation.")
    st.write("Focusing on key metrics such as DCV, transactions, deployed dapps, data scientists, published assets, and locked OCEAN provides a comprehensive view of the ecosystem's health and growth.")
    st.write("Public disclosure of internal measures demonstrates a commitment to transparency and accountability.")
    #----------------------------
    
    img("Assets/im5.jpg", "KPIs for Ocean Core Team")

    # 2. Stream 1: Eagle Rays - DApp Developers
    st.header("2. Stream 1: Eagle Rays - DApp Developers")

    # Subsection 2.1
    st.subheader("2.1. Overview")
    st.write("""
    The Eagle Rays team focuses on enhancing the developer experience and support for building sustainable dapps on the Ocean stack.
    The objective is to enable developers to create income-generating dapps within a month of interaction with the Ocean Protocol development team.
    """)

    img("Assets/im6.jpg", " ")

    # Subsection 2.2
    st.subheader("2.2. Activities")
    st.write("""
    - **Gather Community Feedback:** Conduct one-on-one conversations with data dapp teams to understand challenges and gather feedback.
    - **Improve Developer Support:** Provide proactive support to dapp developers from design to implementation, defining tiers of guidance and technical support.
    - **Run a Dapp Dashboard:** Launch a Dapp Dashboard to highlight projects building on Ocean, fostering community and awareness.
    - **Create Demos & Scaffolding:** Develop demos and templates to showcase Ocean's capabilities, releasing one demo per month.
    - **Host Workshops & Hackathons:** Organize technical workshops and hackathons to engage the developer community.
    """)

    # Subsection 2.3
    st.subheader("2.3. Support for Developers")
    st.write("""
    The Eagle Rays team will offer referrals and funding support for promising teams through initiatives like Ocean Shipyard, Ocean Ventures, and the Ocean Ecosystem Fund.
    """)

    # Subsection 2.4
    st.subheader("2.4. Expected Outcomes")
    st.write("""
    - A vibrant community of data dapp builders.
    - A reduction in the time it takes for developers to build sustainable dapps on the Ocean stack.
    - Increased visibility and support for dapps through the Dapp Dashboard.
    - More comprehensive understanding of Ocean's potential through demos and workshops.
    - Referral and funding opportunities for promising teams.
    """)

    # 3. Stream 2: Thresher - Data Scientists
    st.header("3. Stream 2: Thresher - Data Scientists")

    # Subsection 3.1
    st.subheader("3.1. Overview")
    st.write("""
    The Thresher team aims to help data scientists monetize their data and algorithms on the Ocean Protocol.
    The focus is on making it easy for data scientists to create and sell compelling data feeds while growing the community of data scientists participating in the Ocean ecosystem.
    """)

    # Subsection 3.2
    st.subheader("3.2. Activities")
    st.write("""
    - **Run Objective Data Challenges:** Utilize data challenges like Predict-ETH to guide data scientists in creating and selling data feeds.
    - **Run Subjective Data Challenges:** Conduct challenges with qualitative metrics, driving insights, community, and partnerships.
    - **Ship Compelling Data Feeds:** Create open and forkable data feeds, starting with predictions of ETH.
    - **Reduce Friction in Data Scientist Flows:** Enhance the ease of using Ocean in Python-based workflows, especially in monetizing algorithms.
    - **Other Tools for Demonstration:** Develop tools to showcase capabilities and drive adoption among potential users.
    """)

    # Subsection 3.3
    st.subheader("3.3. Support for Data Scientists")
    st.write("""
    The Thresher team will offer support in the form of hackathons, referrals, and funding opportunities to facilitate the monetization efforts of data scientists.
    """)

    # Subsection 3.4
    st.subheader("3.4. Expected Outcomes")
    st.write("""
    - Increased participation of data scientists in objective and subjective data challenges.
    - Creation and adoption of compelling and monetizable data feeds.
    - Improved integration of Ocean into Python-based data workflows.
    - Enhanced support and resources for data scientists through hackathons and tools.
    """)

    # 4. Stream 3: Sailfish - Crypto Enthusiasts
    st.header("4. Stream 3: Sailfish - Crypto Enthusiasts")

    # Subsection 4.1
    st.subheader("4.1. Overview")
    st.write("""
    The Sailfish team focuses on expanding the Data Farming initiative and serving crypto enthusiasts, especially web3-native Ocean participants.
    The mission is to help these enthusiasts earn in the Ocean ecosystem through activities like staking, curating, and supporting DeFi-oriented dapp builders.
    """)

    # Subsection 4.2
    sa2()
    st.subheader("4.2. Activities")
    st.write("""
    - **Launch & Complete DF Main:** Execute the final phase of Data Farming, automating OCEAN vesting and related processes.
    - **Refine DF Rewards:** Improve the reward function to maximize the impact of emissions in driving traction.
    - **Serve DeFi Dapp Builders Better:** Enhance support for builders focusing on the DeFi side of OCEAN, veOCEAN, and Data Farming.
    - **Other KPI-Driving Activities:** Experiment with various strategies to drive key performance indicators.
    """)

    img("Assets/im7.jpg", " ")
    # Subsection 4.3
    st.subheader("4.3. Support for Crypto Enthusiasts")
    st.write("""
    The Sailfish team offers support to crypto enthusiasts through initiatives like Data Farming, providing opportunities for earning rewards.
    """)

    # Subsection 4.4
    st.subheader("4.4. Expected Outcomes")
    st.write("""
    - Successful completion of DF Main with automated and on-chain processes.
    - Continuous refinement of DF rewards to optimize impact.
    - Better support and engagement with DeFi-oriented dapp builders.
    - Improvement in key performance indicators like the number of OCEAN holders and APYs.
    """)

    # Conclusion
    st.header("5. Conclusion")
    st.write("""
    The Ocean Token project has evolved from building core infrastructure to entering a new era focused on driving data value-creation loops.
    With dedicated streams for developers, data scientists, and crypto enthusiasts, the project aims to empower users in the last mile of the data economy.
    The success of Ocean will be measured by key performance indicators reflecting the growth and impact of the data economy it fosters.
    """)


