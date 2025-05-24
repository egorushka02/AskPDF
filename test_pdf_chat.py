import unittest
from io import BytesIO
from PyPDF2 import PdfWriter
from app import get_pdf_text, get_text_chunks

class SimplePDFChatTests(unittest.TestCase):
    def test_get_pdf_text_simple(self):
        """Test basic text extraction from PDF"""
        pdf_writer = PdfWriter()
        pdf_writer.add_blank_page(width=72, height=72)
        
        pdf_file = BytesIO()
        pdf_writer.write(pdf_file)
        pdf_file.seek(0)
        pdf_file.name = "test.pdf"
        
        text = get_pdf_text([pdf_file])
        self.assertIsInstance(text, str)


    def test_empty_text_chunks(self):
        """Test with empty input"""
        chunks = get_text_chunks("")
        self.assertEqual(chunks, [])

    def test_edge_cases(self):
        """Test edge cases in text chunking"""
        # Только пустые строки
        self.assertEqual(get_text_chunks("\n\n\n"), [])
        
        # Очень длинная строка без разделителей
        long_line = "a" * 1500
        chunks = get_text_chunks(long_line)
        self.assertEqual(len(chunks), 1)
        self.assertTrue(1000 <= len(chunks[0]) <= 1500)
        
        # Смешанный контент
        mixed_text = "\n".join(["Short", "", "Long " * 500, "", "Medium " * 100])
        chunks = get_text_chunks(mixed_text)
        self.assertTrue(2 <= len(chunks) <= 3)

if __name__ == '__main__':
    unittest.main()