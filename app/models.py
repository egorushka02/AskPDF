from pydantic import BaseModel

class ProcessRequest(BaseModel):
    session_id: str

class QuestionRequest(BaseModel):
    session_id: str
    question: str