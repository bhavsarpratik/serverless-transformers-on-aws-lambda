PREDICTION_TYPE = 'classification'

DEFAULT_MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment"
DEFAULT_TOKENIZER_NAME = "roberta-base"
ID_SENTIMENT_MAPPING = { # add for all models to be supported
    "cardiffnlp/twitter-roberta-base-sentiment": {
        0: "NEGATIVE",
        1: "NEUTRAL",
        2: "POSITIVE"
    },
    "cardiffnlp/twitter-roberta-base-emotion": {
        0: "ANGER",
        1: "JOY",
        2: "OPTIMISM",
        3: "SADNESS"
    }
}
