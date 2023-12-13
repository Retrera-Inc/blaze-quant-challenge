import streamlit as st
import base64

def wp():
    def embed_pdf_viewer(pdf_path):
        # Read the PDF file and encode it to base64
        with open(pdf_path, "rb") as file:
            pdf_content = file.read()
            pdf_base64 = base64.b64encode(pdf_content).decode("utf-8")

        # Generate HTML code with an iframe for the PDF viewer
        pdf_viewer_html = f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="700" height="980" type="application/pdf"></iframe>'

        # Display the PDF viewer in Streamlit
        st.markdown(pdf_viewer_html, unsafe_allow_html=True)

    # Specify the path to your PDF file
    pdf_path = "Assets/white_paper.pdf"

    # Display the PDF viewer
    st.title("Ocean WhitePaper")
    embed_pdf_viewer(pdf_path)

