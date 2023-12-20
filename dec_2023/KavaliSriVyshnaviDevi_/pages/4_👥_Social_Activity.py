import streamlit as st
st.set_page_config(page_title="Social Activity", page_icon="👥")

# Navigation Bar
st.sidebar.title("Navigation")
section = st.sidebar.selectbox("Go to", ["Community Engagement", "Online Forums Evaluation","Social Media Assessment"])

# Content
st.title("Social Activity")

if section == "Community Engagement":
    st.header("Community Engagement")

    st.markdown(
        "MakerDAO actively fosters community engagement through various channels, ensuring transparency and collaboration. "
        "One prominent avenue is its GitHub repository, where the development and progress of the Maker Protocol are shared with the community."
    )

    st.subheader("GitHub Repository")
    st.markdown(
        "The MakerDAO GitHub repository serves as a central hub for the open-source development of the Maker Protocol. "
        "It includes a comprehensive collection of code, documentation, and project management resources. "
        "Users, developers, and contributors can access, review, and contribute to the ongoing development of the protocol."
    )
    st.image("assets/git.png")

elif section == "Online Forums Evaluation":
    st.header("Online Forums Evaluation")

    st.subheader("MakerDAO Forum")
    st.markdown(
        "[forum.makerdao.com/tags](http://forum.makerdao.com/tags)\n"
        "- **Engagement:** High. Serving as the official forum for MakerDAO, this platform facilitates discussions on protocol updates, governance proposals, and technical matters. It stands as a valuable resource for staying abreast of the latest developments within the Maker ecosystem.\n"
        "- **Assessment:** A trustworthy source directly affiliated with the MakerDAO team. However, discussions can be highly technical, potentially posing challenges for beginners."
    )

    st.subheader("Reddit")
    st.markdown(
        "[reddit.com/subreddits/create](https://www.reddit.com/subreddits/create)\n"
        "- **Engagement:** Moderate. The Maker subreddit serves as a community hub for discussions covering various facets of the Maker ecosystem, spanning trading, price predictions, and technical analysis.\n"
        "- **Assessment:** While community activity is noticeable, shared information may carry an element of speculation. Caution and fact-checking are advised before relying on this source for investment decisions."
    )

    st.subheader("Bitcointalk")
    st.markdown(
        "[start.makerdao.com](https://start.makerdao.com/)\n"
        "- **Engagement:** Low. The Maker thread on Bitcointalk has experienced limited recent activity.\n"
        "- **Assessment:** Once a prominent platform for cryptocurrency discussions, Bitcointalk's waning activity raises concerns about the timeliness and relevance of information found here. Verification of information from alternative sources is recommended."
    )
elif section == "Social Media Assessment":
    st.header("Social Media Assessment")
    st.subheader("Twitter")
    st.markdown(
        "Twitter: [@PlaymakerDAO](https://twitter.com/PlaymakerDAO)\n"
        "- **Activity:** High. Boasting a substantial following of over 500,000 users, the MakerDAO Twitter account is a prolific source for official announcements, news updates, and community engagement.\n"
        "- **Evaluation:** A dependable channel for official MakerDAO and Maker ecosystem information. Nevertheless, users should exercise caution due to the potential for misinformation and manipulation on social media platforms."
    )
    st.subheader("Discord")
    st.markdown(
        "Discord: [@DiscordMarkerDAO](https://discord.com/invite/AY7yq3gyHq)\n"
        "- **Activity:** Moderate. With over 10,000 members, the MakerDAO Discord server provides a space for more casual discussions and community interaction.\n"
        "- **Evaluation:** A valuable platform for connecting with fellow Maker enthusiasts and receiving real-time updates. However, the unfiltered nature of information shared on Discord may not always ensure reliability."
    )
    st.subheader("Telegram")
    st.markdown(
        "Telegram: [@daomaker](https://t.me/daomaker)\n"
        "- **Activity:** Moderate. The MakerDAO Telegram group, boasting over 16,000 members, serves as another avenue for community discussions and announcements.\n"
        "- **Evaluation:** Similar to Discord, Telegram can facilitate community engagement. Yet, users should be mindful that information shared may lack filtration and reliability."
    )
