from sklearn import pipeline
from src.sentence_encoder import SentenceEncoder

pipeline = SentenceEncoder()


def lambda_handler(event, context):
    try:
        return pipeline(event)
    except Exception as e:
        raise
