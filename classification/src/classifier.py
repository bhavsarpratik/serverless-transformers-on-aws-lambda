import warnings
from functools import lru_cache

warnings.filterwarnings("ignore")

from tqdm import tqdm
from transformers import (AutoConfig, AutoModelForSequenceClassification,
                          AutoTokenizer, pipeline)

from src import config, utils

logger = utils.create_logger(project_name=config.PREDICTION_TYPE, level="INFO")

class Classifier:
    def __init__(self):
        _ = self.get_sentiment_pipeline(model_name=config.DEFAULT_MODEL_NAME, tokenizer_name=config.DEFAULT_TOKENIZER_NAME) #warm up

    @staticmethod
    @lru_cache(maxsize=config.CACHE_MAXSIZE)
    def get_sentiment_pipeline(model_name: str, tokenizer_name: str) -> pipeline:
        """Sentiment pipeline for the given model and tokenizer

        Args:
            model_name (str): Indicating the name of the model
            tokenizer_name (str): Indicating the name of the tokenizer

        Returns:
            pipeline: sentiment pipeline
        """
        logger.info(f"Loading model: {model_name}")
        id2label = config.ID_SENTIMENT_MAPPING[model_name]
        label2id = {label: idx for idx, label in id2label.items()}

        model_config = AutoConfig.from_pretrained(model_name)
        model_config.label2id = label2id
        model_config.id2label = id2label
        model = AutoModelForSequenceClassification.from_pretrained(
            model_name, config=model_config
        )
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
        classification_pipeline = pipeline(
            "sentiment-analysis", model=model, tokenizer=tokenizer
        )
        return classification_pipeline

    def get_clean_text(self, text: str) -> str:
        """Clean the text

        Args:
            text (str): text

        Returns:
            str: clean text
        """        
        return text.strip().lower()

    def __call__(self, request: dict)-> dict:
        """Predict the sentiment of the given texts
        
        Args:
            request (dict): request containing the list of text to predict the sentiment 
        
        Returns:
            dict: classes of the given text
        """
        texts = [self.get_clean_text(text) for text in request["texts"]]
        model_name = request["model_name"]
        tokenizer_name = request["tokenizer_name"]
        
        logger.info(f"Predicting sentiment for {len(texts)} texts")
        classification_pipeline = self.get_sentiment_pipeline(model_name, tokenizer_name)

        predictions = classification_pipeline(texts)
        for i, pred in enumerate(predictions):
            predictions[i]["score"] = round(pred["score"], 2)

        return {
            "predictions": predictions
        }

    