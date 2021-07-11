from src.classifier import Classifier

pipeline = Classifier()

def test_response(requests, response):
    assert response == pipeline(requests)
