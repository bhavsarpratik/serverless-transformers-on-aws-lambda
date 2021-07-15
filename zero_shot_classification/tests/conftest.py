import pytest
from src import config


@pytest.fixture
def requests():
    request_complete = {
        "texts": ["food was great", "food was bad", "i am going out for food"],
        "labels": config.DEFAULT_CANDIDATE_LABELS,
        "hypothesis": config.DEFAULT_HYPOTHESIS_TEMPLATE,
        "model_name": config.DEFAULT_MODEL_NAME,
        "tokenizer_name": config.DEFAULT_TOKENIZER_NAME,
        "multi_label": config.DEFAULT_MULTI_LABEL
    }
    request_default = {
            "texts": ["food was great", "food was bad", "i am going out for food"],
            }
    
    request_multi_label = {
                            "texts": ["food was great", "food was bad", "i am going out for food"],
                            "multi_label": True,
                            }

    return (request_complete, request_default, request_multi_label)


@pytest.fixture
def response():
    response_complete =  {'predictions':[
                                        {'label': 'postive', 'score': 0.8},
                                        {'label': 'negative', 'score': 0.87},
                                        {'label': 'postive', 'score': 0.58}
                                        ]
                        }

    response_default = {'predictions':[
                                        {'label': 'postive', 'score': 0.8},
                                        {'label': 'negative', 'score': 0.87},
                                        {'label': 'postive', 'score': 0.58}
                                        ]
                            }
    
    response_multi_label = {'predictions': [
                                            {'label': ['postive', 'neutral', 'negative'], 'score': [0.87, 0.33, 0.0]},
                                            {'label': ['negative', 'neutral', 'postive'], 'score': [1.0, 0.85, 0.83]},
                                            {'label': ['postive', 'negative', 'neutral'], 'score': [0.67, 0.34, 0.14]}
                                            ]
                            }

    return (response_complete, response_default, response_multi_label)
