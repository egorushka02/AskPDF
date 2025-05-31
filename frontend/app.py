import streamlit as st
import requests
from htmpTemplates import css, bot_template, user_template
import json

class PDFChatFrontend:
    def __init__(self):
        self.api_url = "http://localhost:8000"
        self.setup_streamlit()

    def setup_streamlit(self):
        st.set_page_config(page_title="Chat with your PDF", page_icon=":books:")
        st.write(css, unsafe_allow_html=True)

    def handle_user_input(self, user_question):
        try:
            response = requests.post(
                f"{self.api_url}/chat",
                json={"question": user_question}
            )
            if response.status_code == 200:
                st.write(response.json())
            else:
                st.error("Error getting response from server")
        except Exception as e:
            st.error(f"Error: {str(e)}")

    def process_documents(self, pdf_docs):
        try:
            files = [("files", (pdf.name, pdf.getvalue())) for pdf in pdf_docs]
            response = requests.post(
                f"{self.api_url}/process-documents",
                files=files
            )
            if response.status_code == 200:
                return True
            else:
                st.error("Error processing documents")
                return False
        except Exception as e:
            st.error(f"Error: {str(e)}")
            return False

    def run(self):
        st.header("Chat with your PDF :books:")
        
        # Chat interface
        user_question = st.text_input("Ask a question about your documents:")
        if user_question:
            self.handle_user_input(user_question)

        # Display initial messages
        st.write(user_template.replace("{{MSG}}", "Hello, Robot!"), unsafe_allow_html=True)
        st.write(bot_template.replace("{{MSG}}", "Hello, Human!"), unsafe_allow_html=True)

        # Sidebar for document upload
        with st.sidebar:
            st.subheader("Your documents")
            pdf_docs = st.file_uploader(
                "Upload your PDFs here and click on 'Process'",
                accept_multiple_files=True
            )
            if st.button("Process"):
                with st.spinner("Processing"):
                    self.process_documents(pdf_docs)


def main():
    app = PDFChatFrontend()
    app.run()


if __name__ == "__main__":
    main() 