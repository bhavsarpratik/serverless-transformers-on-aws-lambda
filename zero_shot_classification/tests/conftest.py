import pytest
from src import config


@pytest.fixture
def requests():
    return {
        "texts": ["food was great", "food was bad", "i am going out for food"],
        "labels": config.DEFAULT_CANDIDATE_LABELS,
        "hypothesis": config.DEFAULT_HYPOTHESIS_TEMPLATE,
        "model_name": config.DEFAULT_MODEL_NAME,
        "tokenizer_name": config.DEFAULT_TOKENIZER_NAME
    }


@pytest.fixture
def response():
    return {'predictions':[
        {'label': 'postive', 'score': 0.81},
        {'label': 'negative', 'score': 0.87},
        {'label': 'postive', 'score': 0.59}
        ]
        }
