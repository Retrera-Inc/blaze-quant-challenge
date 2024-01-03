import warnings
warnings.filterwarnings('ignore')
from streamlit_option_menu import option_menu
import base64
import requests
from io import BytesIO
import streamlit as st
from code_files.Tech_analysis import tech_analysis
from code_files.Fundamental_analysis import  fundmental_analysis
from code_files.tokeneconomics import token_economics_analysis
from code_files.sentiment_analysis import sentimental_analysis
from code_files.onchain import onchain_analysis
from code_files.insights import insights


def set_background(image_url):

    response = requests.get(image_url)
    image_bytes = BytesIO(response.content)
    bin_str = base64.b64encode(image_bytes.read()).decode()


    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
    }}
    </style>
    '''


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


selected = option_menu(
    menu_title=None,
    options=['Home', 'Technical Analysis',"Onchain Analysis",'Sentimental Analysis' ,'Fundamental Analysis', 'Tokenomics', "Insights"],
    icons=['house-door-fill', 'upc-scan','upc-scan', 'eye-fill','eye-fill', 'zoom-in', "clipboard-data-fill"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",

)


def change_font_color(element, text, font_color):
    st.markdown(f'<{element} style="color: {font_color};">{text}</{element}>', unsafe_allow_html=True)





def main():

    # local_css("assets/styles.css")


    st.set_option('deprecation.showPyplotGlobalUse', False)
    if selected == "Home":




        change_font_color('h1', 'LIVEPEER :', '#50B8E7')

        st.write("Livepeer is a protocol for developers who want to add live or on-demand video to their project. It aims to increase the reliability of video streaming while reducing costs associated with it by up to 50x.")
        st.write("To achieve this Livepeer is building p2p infrastructure that interacts through a marketplace secured by the Ethereum blockchain")





        change_font_color('h1' ,'Livepeer Overview','#50B8E7')
        livepeer_overview_data = {
            "Key Information": ["What is Livepeer?", "Target Users", "How it Works"],
            "Details": [
                "A protocol for developers to add live or on-demand video to their projects.",
                "Target users include developers, users, and broadcasters, including platforms like Twitch.",
                "Livepeer utilizes a marketplace secured by the Ethereum blockchain, building a decentralized P2P infrastructure.",
            ],
        }


        for key_info, detail in zip(livepeer_overview_data["Key Information"], livepeer_overview_data["Details"]):
            st.header(key_info)
            st.write(detail)

        change_font_color('h1', 'Problem and Solution Analysis', '#50B8E7')
        problem_solution_data = {
            "Problem Statement": ["High cost of video streaming for companies",
                                  "Infrastructure costs leading to financial strain on video startups",
                                  "Aspiring video startups facing funding issues due to high streaming bills"],
            "Solution Offered by Livepeer": [
                "Livepeer aims to reduce costs associated with video streaming by up to 50x.",
                "Livepeer provides a more scalable and cost-effective solution for video infrastructure.",
                "Livepeer helps startups avoid financial strain by offering a cost-effective video streaming solution."]
        }
        st.table(problem_solution_data)



        change_font_color('h1','Actors in the Livepeer Network','#50B8E7')
        actors_data = {
            "Actors": ["Orchestrators", "Livepeer Token (LPT)", "Delegators"],
            "Roles": [
                "Contribute computer resources (CPU, GPU, bandwidth) for transcoding video and earn fees in ETH or stablecoins.",
                "Coordinates, incentivizes participants, and is required for performing transcoding work.",
                "Stake LPT towards orchestrators, ensuring good and honest work, and earning rewards for network security."]
        }
        st.table(actors_data)





        change_font_color("h1","Livepeer Token (LPT) Details",'#50B8E7')

        lpt_details_data = {
            "Key Aspects": ["Purpose of LPT", "Token Utility", "Rewarding Participation"],
            "Details": [
                "Coordinate, bootstrap, and incentivize participants for a cost-effective, secure, and reliable Livepeer network.",
                "Required for transcoding and distributing video on the network. More LPT allows for more work and higher fees.",
                "Orchestrators and Delegators earn a portion of fees and new tokens, growing network ownership.",
            ],
        }


        for aspect, detail in zip(lpt_details_data["Key Aspects"], lpt_details_data["Details"]):
            st.subheader(aspect)
            st.write(detail)



        change_font_color('h1',"Rounds, Inflation, and Growth",'#50B8E7')

        rounds_inflation_data = {
            "Key Metrics": ["Rounds", "Inflation Rate", "Growing Network"],
            "Details": [
                "New tokens minted every round, with one round lasting approximately 22.4 hours.",
                "Adjustable based on the participation rate; currently 0.0375%, aiming for a healthy 50% participation rate.",
                "6,165 delegators securing the network, with increasing participation every day.",
            ],
        }


        st.header("Key Metrics:")
        for metric, detail in zip(rounds_inflation_data["Key Metrics"], rounds_inflation_data["Details"]):
            st.subheader(metric)
            st.write(detail)



        change_font_color('h1',"Additional Notes","#50B8E7")

        additional_notes_data = {
            "Notes": [
                "Livepeer addresses the growing demand for video services with scalable and cost-effective solutions.",
                "Orchestrators contribute resources and earn fees, while Delegators secure the network through token staking.",
                "Livepeer's inflation rate adjusts based on the participation rate, ensuring a healthy balance.",
            ],
        }


        for note in additional_notes_data["Notes"]:
            st.write(note)



    elif selected=='Technical Analysis':
        tech_analysis()


    elif selected=='Onchain Analysis':
        onchain_analysis()

    elif selected=='Fundamental Analysis':
        fundmental_analysis()


    elif selected=='Sentimental Analysis':
        sentimental_analysis()


    elif selected=='Tokenomics':
        token_economics_analysis()


    elif selected=='Insights':
        insights()




if __name__ == "__main__":
    main()