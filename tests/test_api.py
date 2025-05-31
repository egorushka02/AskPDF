from fastapi.testclient import TestClient
from app.main import app
import os 

client = TestClient(app)

def test_process_pdfs():
    # MOK for pdf file
    files = [("files", ("test.pdf", b"%PDF-1.5 test content", "application/pdf"))]

    response = client.post("/process", files=files)
    assert response.status_code == 200
    assert "session_id" in response.json()


def test_ask_question():
    # first create session
    files = [("files", ("test.pdf", b"%PDF-1.5", "application/pdf"))]

    session_id = client.post("/proccess", files=files).json()["session_id"]

    # test of question
    response = client.post("/ask", json={
        "session_id": session_id,
        "question": "Test question"
    })

    assert response.status_code == 200
    assert "chat_history" in response.json()
