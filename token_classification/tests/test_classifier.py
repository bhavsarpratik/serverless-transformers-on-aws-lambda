from src.token_classifier import TokenClassifier

pipeline = TokenClassifier()

def test_response(requests, response):
    assert response == pipeline(requests)
