from src.sentence_encoder import SentenceEncoder

pipeline = SentenceEncoder()

def test_response(requests, response):
    assert response['predictions'] - pipeline(requests)['predictions'][0][0] < 0.001
