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
        'predictions':  [
            [{'generated_text': 'India is a great country for international investors. It also has the support of'}],
            [{'generated_text': 'AI will rule out that she cannot be allowed to wear a hijab but will'}]
        ]
    }
