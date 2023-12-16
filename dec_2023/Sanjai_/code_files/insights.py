import streamlit as st

def change_font_color(element, text, font_color):
    st.markdown(f'<{element} style="color: {font_color};">{text}</{element}>', unsafe_allow_html=True)


def insights():
    change_font_color('h1',"Overall Insights on Analysing LPT token",'#50B8E7')
    st.title('Supply and Demand')
    st.write("Even though it follows a Inflation Based model it able to get right amount of demand")
    st.write('It has a market supply of nearly 21 million coins with demand statisfying it ')
    st.write('Its Maximum Supply is Limited to  22 Million LPT coins.')


    st.title("Market Cap and Price of Token")
    st.write("The Market cap of LPT token is 188,609,465 dollar ")
    st.write("The Market Cap is Projected to grow based on its Growth Ratio and the price of the token makes a major reason in this")

    st.title("Token Distribution")
    st.write("LPT token is majorly owned by Community it has a Fair Launch")
    st.write("The 36-month vesting period signals a commitment to the project's long-term vision")
    st.write("LPT tokens are widely distributed")
    st.write("LPT token is more Community drive indicating the potential Growth")

    st.title("Strong Utility")
    st.write("LPT token has strong utility has wide range of benefits like Governance ,Community Incentives etc ")
    st.write("Attracting Wide Range of Investors based on its utilites")

    st.title("Social Media")
    st.write("The presence of social media links for advisory board members and the community-oriented approach demonstrate Livepeer's commitment to engaging with its user base.")

    st.title("Future Growth Potential")

    st.markdown(
        """
    **1. Increased Adoption:** As the demand for decentralized video streaming grows, Livepeer is 
    well-positioned to capture a significant market share. Increased adoption would drive demand 
    for LPT tokens.

    **2. Ecosystem Expansion:** Livepeer's ecosystem may expand to include new features, partnerships, 
    and use cases, enhancing the utility of LPT within the decentralized video streaming landscape.

    **3. Technological Enhancements:** Ongoing technological advancements, such as improvements in 
    transcoding algorithms or scalability solutions, could further solidify Livepeer's position as a 
    leading decentralized video platform.

    **4. Community Engagement:** The active involvement of the community in governance and development 
    activities is crucial for the sustained growth of Livepeer. Community-driven initiatives can 
    contribute to the success of the platform.

    **5. Integration with DeFi:** Integration with decentralized finance (DeFi) protocols or partnerships 
    with other blockchain projects could open up new opportunities for Livepeer and LPT holders.
    """
    )

