import pytest
from io import BytesIO
from app.utils import get_pdf_text, get_text_chunks, get_vectorstore

def test_get_text_chunks():
    text = "This is a sample text. " * 50
    chunks = get_text_chunks(text)
    assert isinstance(chunks, list)
    assert all(isinstance(chunk, str) for chunk in chunks)
    assert len(chunks) > 0

def test_get_vectorstore():
    chunks = ["sample chunk 1", "sample chunk 2"]
    vectorstore = get_vectorstore(chunks)
    assert vectorstore is not None
    