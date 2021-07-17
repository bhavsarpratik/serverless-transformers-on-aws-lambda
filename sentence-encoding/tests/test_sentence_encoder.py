from src.sentence_encoder import SentenceEncoder
import numpy as np

pipeline = SentenceEncoder()

def test_response(requests, response):
    assert np.allclose(response['predictions'], pipeline(requests)['predictions'], atol=1e-3)
