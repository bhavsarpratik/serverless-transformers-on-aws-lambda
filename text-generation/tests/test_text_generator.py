from src.text_generator import TextGenerator

pipeline = TextGenerator()

def test_response(requests, response):
    assert response == pipeline(requests)
