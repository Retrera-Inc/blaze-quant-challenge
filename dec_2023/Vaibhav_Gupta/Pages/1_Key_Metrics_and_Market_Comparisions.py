import streamlit as st
from PIL import Image

st.markdown(
    """
## Key Metrics and Market Comparisions : 
"""
)

image_path = "./assets/Revenue_ve_transaction_count.png"
image = Image.open(image_path)
st.image(image, caption=" # Revenue vs transaction_count (from July'23 onwards-)")

st.markdown(
    """ 

"""
)

image_path = "./assets/GN0_trading_Volume_vs_Revenue.png"
image = Image.open(image_path)
st.image(image, caption=" # GNO_Trading_Volume_vs_Revenue (from July'23 onwards-)")

st.markdown(
    """ 

"""
)

image_path = "./assets/Transaction_count_vs_Transaction_per_second.png"
image = Image.open(image_path)
st.image(
    image,
    caption=" # Transaction_count_vs_Transaction_per_second (from July'23 onwards-)",
)

st.markdown(
    """
| Key metrics    | :             |
| -------------  | ------------- |
| Ticket         | GNO           |
| Blockchain     | Ethereum      |
| Token standard | ERC-20        |
| Token type     | governance    |
| Token supply   | 10,000,000 GNO   |

"""
)
