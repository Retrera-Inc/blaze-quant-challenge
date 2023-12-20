import streamlit as st
from PIL import Image

def f():
    # with open("style.css") as f:
    #     st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

    st.markdown(
        """
    ## Social Activity :


    """
    )

    image_path = "./assets/Twitter_snap_GNOSIS.png"
    image = Image.open(image_path)
    st.image(image, caption="")

    st.markdown(
        """

    Popularity and Mention Ranking:

    - Gnosis is discussed by 140 unique individuals.
    - It is ranked #314 in terms of mentions and activity from collected posts.

    Sentiment Analysis Across Social Media:

    - In the last 24 hours, Gnosis has an average sentiment score of 0.7 out of 5.
    - On Twitter, 37.95% of tweets express bullish sentiment, while 23.08% express bearish sentiment.
    - The majority (38.97%) of tweets are neutral about Gnosis.

    Sentiment analysis is based on 195 tweets (taken into consideration so far).

    Gnosis is becoming more newsworthy, as evidenced by an increase in mentions and activity.
    """
    )
