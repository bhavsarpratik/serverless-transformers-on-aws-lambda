PREDICTION_TYPE = 'zero-shot-classification'

DEFAULT_MODEL_NAME = "typeform/mobilebert-uncased-mnli"
DEFAULT_TOKENIZER_NAME = "typeform/mobilebert-uncased-mnli"
DEFAULT_HYPOTHESIS_TEMPLATE = "The sentiment of the review is {}."
DEFAULT_CANDIDATE_LABELS = ["negative", "postive", "neutral"]
DEFAULT_MULTI_LABEL = False

# cache
CACHE_MAXSIZE = 4
