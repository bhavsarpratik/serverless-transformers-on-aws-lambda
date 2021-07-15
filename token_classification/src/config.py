PREDICTION_TYPE = 'token_classification'

DEFAULT_MODEL_NAME = "dslim/bert-base-NER"
DEFAULT_TOKENIZER_NAME = "dslim/bert-base-NER"
ID_TAG_MAPPING = { # add for all models to be supported
    "dslim/bert-base-NER": {
        0: "O",
        1: "B-MISC",
        2: "I-MISC",
        3: "B-PER",
        4: "I-PER",
        5: "B-ORG",
        6: "I-ORG",
        7: "B-LOC",
        8: "I-LOC"
    },
    
}

# cache
CACHE_MAXSIZE = 4
