import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_vectorstore():
    mock = MagicMock()
    mock.as_retriever.return_value = "retriever"
    return mock