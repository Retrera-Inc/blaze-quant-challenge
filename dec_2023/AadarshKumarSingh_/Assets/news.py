import requests
import streamlit as st

url = "https://api.tokeninsight.com/api/v1/news/list?lang=en"

headers = {
    "accept": "application/json",
    "TI_API_KEY": "27b2a3d576f54c72bb339b9641ee042a"
}

response = requests.get(url, headers=headers)
data = response.json()

# Check if the request was successful
if response.status_code == 200 and data["status"]["code"] == 0:
    news_items = data["data"]["items"]

    # Create a Streamlit app
    st.title("Token News")

    for item in news_items:
        # Check if any tag name contains "Ocean Protocol"
        if any(tag["name"] == "ocean" for tag in item["tags"]):
            st.subheader(item["title"])
            st.markdown(item["content"], unsafe_allow_html=True)
            st.write("URL:", item["url"])
            st.image(item["image_url"], caption="Image")
            st.write("Source URL:", item["source_url"])
            st.write("Timestamp:", item["timestamp"])
            st.write("Tags:", ", ".join([tag["name"] for tag in item["tags"]]))
            st.markdown("-" * 50)
else:
    st.error("Error: {}".format(data["status"]["message"]))
