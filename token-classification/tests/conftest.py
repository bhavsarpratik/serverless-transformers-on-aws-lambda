import pytest
from src import config


@pytest.fixture
def requests():
    return {
        "texts": ["Mark is going back to Germany from South Africa", "John Adams is performing live in Venezuela"],
        "model_name": config.DEFAULT_MODEL_NAME,
        "tokenizer_name": config.DEFAULT_TOKENIZER_NAME
    }

@pytest.fixture
def requests_default():
    return {
        "texts": ["Mark is going back to Germany from South Africa", "John Adams is performing live in Venezuela"],
    }


@pytest.fixture
def response():
    return {
        'predictions': [
            [
                {'word': 'Mark', 'score': 1.0, 'entity': 'B-PER', 'index': 1, 'start': 0, 'end': 4
                 },
                {'word': 'Germany', 'score': 1.0, 'entity': 'B-LOC', 'index': 6, 'start': 22, 'end': 29
                 },
                {'word': 'South', 'score': 1.0, 'entity': 'B-LOC', 'index': 8, 'start': 35, 'end': 40
                 },
                {'word': 'Africa', 'score': 1.0, 'entity': 'I-LOC', 'index': 9, 'start': 41, 'end': 47
                 }
            ],
            [
                {'word': 'John', 'score': 1.0, 'entity': 'B-PER', 'index': 1, 'start': 0, 'end': 4
                 },
                {'word': 'Adams', 'score': 1.0, 'entity': 'I-PER', 'index': 2, 'start': 5, 'end': 10
                 },
                {'word': 'Venezuela', 'score': 1.0, 'entity': 'B-LOC', 'index': 7, 'start': 33, 'end': 42
                 }
            ]
        ]
    }
