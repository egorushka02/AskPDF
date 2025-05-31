import pytest
from app.utils import get_pdf_text, get_text_chunks

# MOK for pdf files
@pytest.fixture
def mock_pdf_file():
    class MockPDF:
        def pages(sels):
            return [MockPage()]
    class MockPage:
        def extract_text(self):
            return "Sample text\n"
    return MockPDF

def get_test_pdf_text(mock_pdf_file):
    text = get_pdf_text([mock_pdf_file])
    assert text == "Sample text\n"

def test_get_text_chunks():
    text = "a\n" * 500 # 1000 symbols
    chunks = get_text_chunks(text)
    assert len(chunks) > 1 
    assert 900  < len(chunks[0]) < 1100