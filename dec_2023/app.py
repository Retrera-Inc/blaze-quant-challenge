
import streamlit as st
from analysis import analyze_token
def main():
    st.title("Token Analysis App")

    token_symbol = st.text_input("Enter Token Symbol:")

    if st.button("Analyze"):
        if not token_symbol:
            st.warning("Please enter a valid token symbol.")
        else:
            try:
                analysis_results = analyze_token(token_symbol)
                st.subheader(f"Analysis for {token_symbol}")
                st.write(analysis_results)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

if _name_ == "_main_":
    main()
