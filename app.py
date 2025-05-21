import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI
from htmpTemplates import css, bot_template, user_template
import os


class PDFProcessor:
    def __init__(self):
        self.text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )

    def extract_text(self, pdf_docs):
        text = ""
        for pdf in pdf_docs:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                text += page.extract_text()
        return text

    def create_chunks(self, text):
        return self.text_splitter.split_text(text)


class VectorStoreManager:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-mpnet-base-v2",
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': False}
        )

    def create_vectorstore(self, text_chunks):
        return FAISS.from_texts(texts=text_chunks, embedding=self.embeddings)


class ConversationManager:
    def __init__(self):
        self.llm = ChatOpenAI(
            base_url="https://proxy.merkulov.ai",
            api_key="sk-06emc8NHjoFndfxgIYH7tw"
        )
        self.memory = ConversationBufferMemory(
            memory_key='chat_history',
            return_messages=True
        )

    def create_conversation_chain(self, vectorstore):
        return ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=vectorstore.as_retriever(),
            memory=self.memory
        )


class PDFChatApp:
    def __init__(self):
        self.pdf_processor = PDFProcessor()
        self.vector_store_manager = VectorStoreManager()
        self.conversation_manager = ConversationManager()
        self.setup_streamlit()

    def setup_streamlit(self):
        st.set_page_config(page_title="Chat with your PDF", page_icon=":books:")
        st.write(css, unsafe_allow_html=True)

        if "conversation" not in st.session_state:
            st.session_state.conversation = None

    def handle_user_input(self, user_question):
        if st.session_state.conversation:
            response = st.session_state.conversation({'question': user_question})
            st.write(response)

    def process_documents(self, pdf_docs):
        with st.spinner("Processing"):
            # Extract text from PDFs
            raw_text = self.pdf_processor.extract_text(pdf_docs)
            
            # Create text chunks
            text_chunks = self.pdf_processor.create_chunks(raw_text)
            
            # Create vector store
            vectorstore = self.vector_store_manager.create_vectorstore(text_chunks)

            # Create conversation chain
            st.session_state.conversation = self.conversation_manager.create_conversation_chain(vectorstore)

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
                self.process_documents(pdf_docs)


def main():
    app = PDFChatApp()
    app.run()


if __name__ == "__main__":
    main()