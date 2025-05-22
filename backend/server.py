from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import uvicorn
from pdf_processor import PDFChatBackend
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене заменить на конкретные домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Создаем экземпляр бэкенда
backend = PDFChatBackend()

@app.post("/process-documents")
async def process_documents(files: List[UploadFile] = File(...)):
    try:
        # Сохраняем файлы временно
        pdf_docs = []
        for file in files:
            content = await file.read()
            pdf_docs.append(content)
        
        # Обрабатываем документы
        success = backend.process_documents(pdf_docs)
        return {"status": "success" if success else "error"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/chat")
async def chat(question: str):
    try:
        response = backend.get_response(question)
        if response:
            return response
        raise HTTPException(status_code=400, detail="No conversation initialized")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 