import streamlit as st

def draw():
    st.subheader("TokenInsight Rating")

    # Get the TokenInsight widget script URL
    widget_script_url = "https://s2.tokeninsight.com/widgets/tokeninsight-rating-widget/index.js?343243434"
    
    # TokenInsight rating widget configuration
    subject = "black"
    language = "en"
    token = "ocean-protocol"

    # Embed the TokenInsight rating widget using an HTML script
    st.components.v1.html(
        f"""
        <script src="{widget_script_url}"></script>
        <tokeninsight-rating-widget subject="{subject}" language="{language}" token="{token}"></tokeninsight-rating-widget>
        """,
        height=635,
        width = 1025
    )


# st.markdown(
#     f"""<script src="https://s2.tokeninsight.com/widgets/tokeninsight-rating-widget/index.js?343243434"></script><tokeninsight-rating-widget subject="black" language="en" token="{symbol}"></tokeninsight-rating-widget>""",
#     unsafe_allow_html=True
# )
