from sklearn import pipeline
from src.token_classifier import TokenClassifier

pipeline = TokenClassifier()


def lambda_handler(event, context):
    try:
        return pipeline(event)
    except Exception as e:
        raise
