import streamlit as st
import base64
def embed_pdf(pdf_path):
    with open(pdf_path, "rb") as f:
        data = f.read()
    base64_pdf = base64.b64encode(data).decode('utf-8')
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="500" type="application/pdf">'
    styled_container = f"""
    <div style="
        height: 150%;
        display: flex;
        flex-direction: column;
        align-items: center;
    ">
        <div style="margin-top: 20px;">{pdf_display}</div>
    </div>
    """
    
    st.markdown(styled_container, unsafe_allow_html=True)

# Example usage
pdf_path = "assets/whitepaper.pdf"
st.set_page_config(page_title="White Paper", page_icon="📚")
st.title("White Paper")
embed_pdf(pdf_path)
