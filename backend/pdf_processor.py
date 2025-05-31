from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI


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


class PDFChatBackend:
    def __init__(self):
        self.pdf_processor = PDFProcessor()
        self.vector_store_manager = VectorStoreManager()
        self.conversation_manager = ConversationManager()
        self.conversation = None

    def process_documents(self, pdf_docs):
        # Extract text from PDFs
        raw_text = self.pdf_processor.extract_text(pdf_docs)
        
        # Create text chunks
        text_chunks = self.pdf_processor.create_chunks(raw_text)
        
        # Create vector store
        vectorstore = self.vector_store_manager.create_vectorstore(text_chunks)

        # Create conversation chain
        self.conversation = self.conversation_manager.create_conversation_chain(vectorstore)
        return True

    def get_response(self, user_question):
        if self.conversation:
            return self.conversation({'question': user_question})
        return None 