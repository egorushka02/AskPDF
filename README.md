# AskPDF - Chat with Your PDF Documents

[English](#english) | [Русский](#russian)

## English

### Description
AskPDF is an interactive web application that allows you to chat with your PDF documents. Using RAG techniques, you can ask questions about the content of your PDFs and get intelligent responses.

### Project Structure
```
AskPDF/
├── backend/
│   ├── pdf_processor.py    # Backend logic for PDF processing and chat
│   └── server.py          # FastAPI server
├── frontend/
│   ├── app.py             # Streamlit frontend application
│   └── htmpTemplates.py   # HTML templates for chat interface
└── requirements.txt       # Project dependencies
```

### Features
- Upload multiple PDF documents
- Interactive chat interface
- AI-powered question answering
- Support for multiple languages
- Real-time document processing
- RESTful API backend
- Modern web interface

### Technical Stack
- Backend:
  - Python
  - FastAPI
  - LangChain
  - OpenAI API
  - FAISS Vector Store
  - HuggingFace Embeddings
- Frontend:
  - Streamlit
  - HTML/CSS
  - Requests for API communication

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

1. Start the backend server:
```bash
cd backend
uvicorn server:app --reload
```

2. In a new terminal, start the frontend:
```bash
cd frontend
streamlit run app.py
```

3. Open your web browser and navigate to the provided local URL (usually http://localhost:8501)

4. Upload your PDF documents using the sidebar

5. Click "Process" to analyze your documents

6. Start asking questions about your documents in the chat interface

## Русский

### Описание
AskPDF - это интерактивное веб-приложение, которое позволяет общаться с вашими PDF-документами. Используя технологии RAG, вы можете задавать вопросы о содержании ваших PDF-файлов и получать интеллектуальные ответы.

### Структура проекта
```
AskPDF/
├── backend/
│   ├── pdf_processor.py    # Бэкенд логика для обработки PDF и чата
│   └── server.py          # FastAPI сервер
├── frontend/
│   ├── app.py             # Streamlit фронтенд приложение
│   └── htmpTemplates.py   # HTML шаблоны для интерфейса чата
└── requirements.txt       # Зависимости проекта
```

### Возможности
- Загрузка нескольких PDF-документов
- Интерактивный интерфейс чата
- Ответы на вопросы с использованием ИИ
- Поддержка нескольких языков
- Обработка документов в реальном времени
- RESTful API бэкенд
- Современный веб-интерфейс

### Технический стек
- Бэкенд:
  - Python
  - FastAPI
  - LangChain
  - OpenAI API
  - FAISS Vector Store
  - HuggingFace Embeddings
- Фронтенд:
  - Streamlit
  - HTML/CSS
  - Requests для API коммуникации

### Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/egorushka02/AskPDF.git
cd AskPDF
```

2. Установите необходимые зависимости:
```bash
pip install -r requirements.txt
```

3. Настройте переменные окружения:
Создайте файл `.env` в корневой директории и добавьте ваш ключ OpenAI API:
```
OPENAI_API_KEY=ваш_ключ_api
OPENAI_API_BASE_URL=ваш_base_url
```

### Использование

1. Запустите бэкенд сервер:
```bash
cd backend
uvicorn server:app --reload
```

2. В новом терминале запустите фронтенд:
```bash
cd frontend
streamlit run app.py
```

3. Откройте веб-браузер и перейдите по предоставленному локальному URL (обычно http://localhost:8501)

4. Загрузите ваши PDF-документы через боковую панель

5. Нажмите "Process" для анализа документов

6. Начните задавать вопросы о ваших документах в интерфейсе чата
