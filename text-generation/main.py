from sklearn import pipeline
from src.text_generator import TextGenerator

pipeline = TextGenerator()


def lambda_handler(event, context):
    try:
        return pipeline(event)
    except Exception as e:
        raise
