from src.classifier import Classifier

pipeline = Classifier()


def lambda_handler(event, context):
    try:
        return pipeline(event)
    except Exception as e:
        raise
