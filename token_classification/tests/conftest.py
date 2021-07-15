import pytest
from src import config


@pytest.fixture
def requests():
    return {
        "texts": ["Mark is going back to Germany from South Africa"],
        "model_name": config.DEFAULT_MODEL_NAME,
        "tokenizer_name": config.DEFAULT_TOKENIZER_NAME
    }


@pytest.fixture
def response():
    return {
        'predictions': [{
            "entity_group": "PER",
            "score": 0.9996247887611389,
            "word": "Mark",
            "start": 0,
            "end": 4
        },
            {
            "entity_group": "LOC",
            "score": 0.9998000264167786,
            "word": "Germany",
            "start": 22,
            "end": 29
        },
            {
            "entity_group": "LOC",
            "score": 0.9994221925735474,
            "word": "South Africa",
            "start": 35,
            "end": 47
        }]
    }
