# AskPDF - Chat with Your PDF Documents


### Description
AskPDF is an interactive web application that allows you to chat with your PDF documents. Using RAG techniques, you can ask questions about the content of your PDFs and get intelligent responses.

### Features
- Upload multiple PDF documents
- Interactive chat interface
- AI-powered question answering
- Support for multiple languages
- Real-time document processing

### Technical Stack
- Python
- Streamlit
- LangChain
- OpenAI API
- FAISS Vector Store
- HuggingFace Embeddings

### Installation

1. Clone the repository:
```bash
git clone https://github.com/egorushka02/AskPDF.git
cd AskPDF
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
OPENAI_API_BASE_URL=your_base_url
```

### Usage
1. Run the application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided local URL (usually http://localhost:8501)

3. Upload your PDF documents using the sidebar

4. Click "Process" to analyze your documents

5. Start asking questions about your documents in the chat interface
