import streamlit as st
import Assets.toke as toke
import Assets.Transaction_overview as Transaction_overview
import base64
from Assets.toke import q_one
from Assets.api import ap
from Assets.on_chain import oc
from Assets.future import fut
from Assets.twitter import sa
import Assets.T_T as T_T
from Assets.blueprint import red
from Assets.token_model import tok_mod
from Assets.Analysis import ocean_token_analysis
from Assets.white_paper import wp


def blueprint():
    red()

def token_model():
    tok_mod()
    
def analysis():
    ocean_token_analysis()

def token_distribution_and_scarcity():
    st.title("Token Distribution and Scarcity")
    st.write("**Large Percentage Held by Few:**")
    st.write("Further investigation into the distribution could reveal whether a significant portion of the token is held by a small number of addresses. "
             "This concentration may pose potential risks such as market manipulation or sell-offs by large holders.")

    st.write("**Vesting Schedules:**")
    st.write("Explore if there are vesting schedules for early investors, team members, or advisors. "
             "Understanding the vesting periods can provide insights into potential sell pressures or long-term commitment from key stakeholders.")

def market_activity_and_price():
    
    st.subheader("Market Activity and Price")
    st.write("**Comparison with Peers:**")
    st.write("Compare OCEAN's trading volume and price movement with similar tokens or projects in the data marketplace sector. "
             "This context can help determine if OCEAN's market activity is in line with industry standards.")

    st.write("**Volatility Analysis:**")
    st.write("Assess the historical volatility of OCEAN to understand how stable or volatile the token's price has been over time. "
             "This analysis can help gauge the risk associated with holding OCEAN.")
    Transaction_overview.cc()
    T_T.cc()
    
def overall_health_and_adoption():
    st.subheader("Overall Health and Adoption")
    st.write("**Development Milestones:**")
    st.write("Look into specific development milestones or recent updates in the Ocean Protocol ecosystem. "
             "Highlight any upcoming features or improvements that might impact the token's utility and adoption.")

    st.write("**Community Engagement:**")
    st.write("Explore qualitative data on community engagement, such as discussions on social media platforms, forums, and developer activity. "
             "A vibrant community is often indicative of sustained interest in the project.")

def potential_risks_and_uncertainties():
    st.subheader("Potential Risks and Uncertainties")
    st.write("**Regulatory Compliance:**")
    st.write("Assess how well Ocean Protocol is positioned to navigate regulatory challenges. "
             "An understanding of the project's compliance measures can provide insights into its resilience in the face of changing regulatory environments.")

    st.write("**Partnerships and Collaborations:**")
    st.write("Investigate the strength and diversity of Ocean Protocol's partnerships. "
             "Strong collaborations with industry players can enhance the project's competitive edge and market position.")

def additional_considerations():
    st.subheader("Additional Considerations")
    st.write("**Utility Analysis:**")
    st.write("Explore the use cases and utility of OCEAN within the Ocean Protocol ecosystem. "
             "Understanding how the token is utilized can shed light on its long-term demand.")

    st.write("**Tokenomics Dynamics:**")
    st.write("Dive deeper into the tokenomics, looking at factors like inflation rate, mechanisms for token burning, and any upcoming changes to the tokenomics. "
             "This can provide insights into the token's supply dynamics.")

    st.write("**User Feedback:**")
    st.write("Consider incorporating user feedback or sentiment analysis from the community. "
             "This qualitative data can complement the quantitative metrics, offering a more holistic view of the project's health.")

def overall_position_and_functionality():
    token_distribution_and_scarcity()
    market_activity_and_price()
    sa()
    overall_health_and_adoption()
    potential_risks_and_uncertainties()
    additional_considerations()

def key_metrics():
    ap()



def tokenomics():
    q_one()

def on_chain_data_insight():
    oc()



def revenue_model_and_fees():
    from Assets.revenue import rev
    rev()

def significant_project_milestone():
    from Assets.milestone import mil
    mil()

def risk_management():
    from Assets.risks import r
    r()

def future_prospects():
    fut()


# Main Streamlit App
def main():
    
    # Sidebar Navigation
    menu = ["Token Model",
            "Token Analysis",
            "Token Blueprint",
            "Position and Funtionality",
            "Key Metrics",
            "Tokenomics", 
            "On Chain Data Insights",
            "Revenue Model",
            "Milestones",
            "Risks",
            "Future Prospects", 
            "White Paper",]
    choice = st.sidebar.selectbox("Navigate", menu, index=0)

    if choice == "Token Model":
        token_model()
    elif choice == "Token Analysis":
        analysis()
    elif choice == "Token Blueprint":
        blueprint()
    elif choice == "Position and Funtionality":
        overall_position_and_functionality()
    elif choice == "Key Metrics":
        key_metrics()
    elif choice == "Tokenomics":
        tokenomics()
    elif choice == "Revenue Model":
        revenue_model_and_fees()
    elif choice == "On Chain Data Insights":
        on_chain_data_insight()
    elif choice == "Milestones":
        significant_project_milestone()
    elif choice == "Risks":
        risk_management()
    elif choice == "Future Prospects":
        future_prospects()   
    elif choice == "White Paper":
        wp()  
if __name__ == "__main__":
    main()
