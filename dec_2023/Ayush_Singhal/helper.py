import pandas as pd
import warnings 
import requests
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import base64
import streamlit as st

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

def download_nltk_resources():
    nltk.download("punkt")
    nltk.download('stopwords')

def remove_emojis(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F700-\U0001F77F"  # alchemical symbols
                               u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                               u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                               u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                               u"\U0001FA00-\U0001FA6F"  # Chess Symbols
                               u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                               u"\U00002702-\U000027B0"  # Dingbats
                               u"\U000024C2-\U0001F251" 
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def remove_stopwords(text):
    download_nltk_resources()
    stopwords_list = set(stopwords.words("english"))
    custom_stopwords = ["e.g.", "i.e.", "etc."]
    stopwords_list.update(custom_stopwords)
    tokens = nltk.word_tokenize(text)
    filtered_tokens = [token for token in tokens if token.lower() not in stopwords_list]
    return " ".join(filtered_tokens)

def stem_text(text):
    porter_stemmer = PorterStemmer()
    tokens = nltk.word_tokenize(text)
    stemmed_tokens = [porter_stemmer.stem(token) for token in tokens]
    return " ".join(stemmed_tokens)

def filter_words(text):
    filtered_words = [word for word in text.split() if 'illuv' not in word and 'ilv' not in word]
    return " ".join(filtered_words)

# def extract(token) :

#     data = requests.get(f'https://api.coingecko.com/api/v3/coins/{token}/market_chart?vs_currency=USD&days=max').json()
#     open_close = requests.get(f'https://api.coingecko.com/api/v3/coins/{token}/ohlc?vs_currency=usd&days=max').json()

#     if 'error' in data.keys() : warnings.warn('Token Not available')
#     else :

#         prices = pd.DataFrame(data['prices'] , columns = ['Time' , 'prices'])
#         mcap = pd.DataFrame(data['market_caps'] , columns = ['Time' , 'MCap'])
#         volume = pd.DataFrame(data['total_volumes'] , columns = ['Time' , 'Volume'])

#         open_close = pd.DataFrame(open_close , columns = ['Time' , 'Open' , 'High' , 'Low' , 'Close'])

#         prices = prices.merge(mcap)
#         prices = prices.merge(volume)
#         prices = prices.merge(open_close , how = 'outer')

#         return prices

#     return None 

pd.options.mode.chained_assignment = None

def download_data(url, destination):
    response = requests.get(url)
    if response.status_code == 200:
        with open(destination, "wb") as file:
            file.write(response.content)
        print(f"File downloaded successfully to {destination}")
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")

def help(path):
    # Download data if not already present
    download_data("https://api.llama.fi/dataset/illuvium.csv", path)

    data = pd.read_csv(path)

    cols = []
    for col in data.columns:
        value = list(data[col][:4])
        stri = col
        for val in value:
            try:
                stri += '_' + val
            except Exception as e:
                pass
        cols.append(stri)

    sample_data = pd.DataFrame(data, columns=cols)

    for col_data, col_s_data in zip(data.columns, sample_data.columns):
        sample_data[col_s_data] = data[col_data]

    sample_data = sample_data[4:]

    sample_data['Date'] = pd.to_datetime(sample_data['Date'], format='%d/%m/%Y')
    for col in sample_data.columns[2:]:
        sample_data[col] = sample_data[col].astype(float)

    return sample_data