from src.classifier import Classifier

pipeline = Classifier()

def test_complete_response(requests, response):
    assert response[0] == pipeline(requests[0])

def test_default_response(requests, response):
    assert response[1] == pipeline(requests[1])

def test_multi_label_response(requests, response):
    assert response[2] == pipeline(requests[2])
