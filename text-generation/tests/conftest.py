import pytest
from src import config


@pytest.fixture
def requests():
    return {
        "texts": ["India is a great", "AI will rule"],
        "model_name": "distilgpt2",  # optional
        "tokenizer_name": "distilgpt2",  # optional
        # maximum no. of token(words) to be genrated using the given context optional
        "max_len": 15,
        # no. of sequences(sentences) to be genrated using the given context optional
        "num_return_sequences": 1
    }


@pytest.fixture
def response():
    return {
        'predictions': [
            [{'generated_text': 'India is a great help in terms of the security of our species. The'}], 
            [{'generated_text': "AI will rule this week, though we won't know until the end of"}]
        ]
    }
