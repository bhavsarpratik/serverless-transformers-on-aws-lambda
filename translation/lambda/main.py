from src.easy_nmt import translate_records


def lambda_handler(event, context):
    try:
        return translate_records(event)
    except Exception as e:
        raise
