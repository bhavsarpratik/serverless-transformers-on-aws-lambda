import warnings

warnings.filterwarnings("ignore")

from functools import lru_cache

from transformers import (AutoConfig, AutoModelForTokenClassification,
                          AutoTokenizer, pipeline)

from src import config, utils

logger = utils.create_logger(project_name=config.PREDICTION_TYPE, level="INFO")


class TokenClassifier:
    def __init__(self):
        _ = self.get_ner_pipeline(model_name=config.DEFAULT_MODEL_NAME,
                                  tokenizer_name=config.DEFAULT_TOKENIZER_NAME)  # warm up

    @staticmethod
    @lru_cache(maxsize=config.CACHE_MAXSIZE)
    def get_ner_pipeline(model_name: str, tokenizer_name: str) -> pipeline:
        """NER pipeline for the given model and tokenizer

        Args:
            model_name (str): Indicating the name of the model
            tokenizer_name (str): Indicating the name of the tokenizer

        Returns:
            pipeline: ner pipeline
        """
        logger.info(f"Loading model: {model_name}")
        id2label = config.ID_TAG_MAPPING[model_name]
        label2id = {label: idx for idx, label in id2label.items()}

        model_config = AutoConfig.from_pretrained(model_name)
        model_config.label2id = label2id
        model_config.id2label = id2label
        model = AutoModelForTokenClassification.from_pretrained(
            model_name, config=model_config
        )
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
        ner_pipeline = pipeline(
            "ner", model=model, tokenizer=tokenizer
        )
        return ner_pipeline

    def get_clean_text(self, text: str) -> str:
        """Clean the text

        Args:
            text (str): text

        Returns:
            str: clean text
        """
        return text.strip()

    def __call__(self, request: dict) -> dict:
        """Predict tags of the given tokens

        Args:
            request (dict): request containing the list of text to predict entities

        Returns:
            dict: classes of the given text
        """
        texts = [self.get_clean_text(text) for text in request["texts"]]
        model_name = request.get("model_name", config.DEFAULT_MODEL_NAME)
        tokenizer_name = request.get("tokenizer_name", config.DEFAULT_TOKENIZER_NAME)

        logger.info(f"Predicting tags for {len(texts)} texts")
        ner_pipeline = self.get_ner_pipeline(model_name, tokenizer_name)

        predictions = ner_pipeline(texts)
        
        for i, pred in enumerate(predictions):
            for dct in pred:
                dct["score"] = round(dct["score"], 2)
            predictions[i] = pred

        return {
            "predictions": predictions
        }
