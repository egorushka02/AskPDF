from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch, MagicMock

client = TestClient(app)

def test_ask_question_invalid_session():
    response = client.post(
        "/ask",
        json={"session_id": "invalid", "question": "test"}
    )
    assert response.status_code == 404