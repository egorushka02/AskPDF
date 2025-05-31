from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uuid
from .utils import get_pdf_text, get_text_chunks, get_vectorstore
from .dependencies import get_conversation_chain
from .models import ProcessRequest, QuestionRequest
from io import BytesIO

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],    
)

# session store
sessions = {}

@app.post("/process")
async def process_pdfs(files: list[UploadFile]= File(...)):
    """Process PDF files and create session"""
    try:
        # read pdf file in BytesIO
        pdf_files = [BytesIO(await file.read()) for file in files]

        # processing pdfs
        raw_text = get_pdf_text(pdf_files)
        text_chunks = get_text_chunks(raw_text)
        vectorstore = get_vectorstore(text_chunks)

        # creating session
        session_id = str(uuid.uuid4())
        sessions[session_id] = get_conversation_chain(vectorstore)

        return {"session_id": session_id, "message": "PDFs processed succesfully"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/ask")
async def asK_question(request: QuestionRequest):
    """Process users requests"""
    if request.session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    conversation = sessions[request.session_id]
    response = conversation.invoke({"question": request.question})

    # chat history formatting
    chat_history = []
    for i, message in enumerate(response["chat_history"]):
        chat_history.append({
            "content": message.content,
            "is_user": i % 2 == 0 # True for user, False for bot    
        })

    return {"chat_history": chat_history}