import streamlit as st
import pandas as pd
from textblob import TextBlob
import json
import plotly.express as px

def categorize_sentiment(score):
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

def perform_sentiment_analysis(tweets):
    polarities = [TextBlob(tweet["text"]).sentiment.polarity for tweet in tweets]
    overall_sentiment = sum(polarities) / len(polarities)
    return {"Overall Sentiment": overall_sentiment, "Sentiment Scores": polarities}

def sentimental_analysis():
    # Load Twitter data from JSON file
    json_file_path = "code_files/Data/twitter.json"  # Replace with the actual path to your JSON file
    with open(json_file_path, "r", encoding="utf-8") as file:
        twitter_data = json.load(file)

    sentiment_result = perform_sentiment_analysis(twitter_data)
    sentiment_categories = [categorize_sentiment(score) for score in sentiment_result["Sentiment Scores"]]
    sentiment_counts = pd.Series(sentiment_categories).value_counts()

    st.title("Twitter Sentiment Analysis")
    st.write(f"Overall Sentiment: {categorize_sentiment(sentiment_result['Overall Sentiment'])}")
    st.write("Sentiment Distribution:")
    st.write(sentiment_counts)
    st.title("Sentiment Pie Chart")
    fig = px.pie(sentiment_counts, values=sentiment_counts.values, names=sentiment_counts.index,
                 title="Sentiment Distribution")
    st.plotly_chart(fig)
