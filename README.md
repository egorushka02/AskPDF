# AskPDF - AI-Powered PDF Chat Application


### Overview
AskPDF is an intelligent application that allows you to chat with your PDF documents using advanced AI technology. It uses RAG (Retrieval-Augmented Generation) to provide accurate and context-aware responses to your questions about PDF content.

### Features
- 📄 **Multiple PDF Support**: Upload and process multiple PDF documents simultaneously
- 💬 **Interactive Chat**: Natural language interface for asking questions about your documents
- 🤖 **AI-Powered**: Utilizes OpenAI's language models for intelligent responses
- 🔍 **Smart Search**: Advanced document retrieval using FAISS vector store
- 🌐 **Web Interface**: User-friendly Streamlit-based web application
- 🔒 **Secure**: Local processing of documents with secure API communication

### Technical Architecture
```
AskPDF/
├── backend/
│   ├── pdf_processor.py    # PDF processing and AI logic
│   └── server.py          # FastAPI server implementation
├── frontend/
│   ├── app.py             # Streamlit frontend application
│   └── htmpTemplates.py   # HTML/CSS templates
├── tests/
│   └── test_app.py        # Unit tests
└── requirements.txt       # Project dependencies
```

### Technology Stack
- **Backend**:
  - Python 3.8+
  - FastAPI
  - LangChain
  - OpenAI API
  - FAISS Vector Store
  - HuggingFace Embeddings
