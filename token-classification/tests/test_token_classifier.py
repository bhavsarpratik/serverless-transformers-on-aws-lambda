from src.token_classifier import TokenClassifier

pipeline = TokenClassifier()

def test_response(requests, response):
    assert response == pipeline(requests)

def test_response_default(requests_default, response):
    assert response == pipeline(requests_default)
