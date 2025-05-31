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
