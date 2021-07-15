import warnings
from functools import lru_cache

warnings.filterwarnings("ignore")

from tqdm import tqdm
from transformers import pipeline

from src import config, utils

logger = utils.create_logger(project_name=config.PREDICTION_TYPE, level="INFO")

class Classifier:
    def __init__(self):
        _ = self.get_zero_shot_classification_pipeline(model_name=config.DEFAULT_MODEL_NAME, tokenizer_name=config.DEFAULT_TOKENIZER_NAME) #warm up

    @staticmethod
    @lru_cache(maxsize=config.CACHE_MAXSIZE)
    def get_zero_shot_classification_pipeline(model_name: str, tokenizer_name: str) -> pipeline:
        """Zero Shot pipeline for the given model and tokenizer

        Args:
            model_name (str): Indicating the name of the model
            tokenizer_name (str): Indicating the name of the tokenizer

        Returns:
            pipeline: Zero-Shot Classification Pipeline
        """
        logger.info(f"Loading model: {model_name}")
        classification_pipeline = pipeline("zero-shot-classification", model=model_name, tokenizer=tokenizer_name)
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

        labels = request["labels"] if "labels" in request.keys() else config.DEFAULT_CANDIDATE_LABELS
            
        hypothesis = request["hypothesis"] if "hypothesis" in request.keys() else config.DEFAULT_HYPOTHESIS_TEMPLATE

        model_name = request["model_name"] if "model_name" in request.keys() else config.DEFAULT_MODEL_NAME
        
        tokenizer_name = request["tokenizer_name"] if "tokenizer_name" in request.keys() else config.DEFAULT_TOKENIZER_NAME
        
        multi_label = request["multi_label"] if "multi_label" in request.keys() else config.DEFAULT_MULTI_LABEL
        
        logger.info(f"Classifying {len(texts)} texts")
        classification_pipeline = self.get_zero_shot_classification_pipeline(model_name, tokenizer_name)

        predictions = classification_pipeline(texts, labels, hypothesis, multi_label=multi_label)
        
        if not multi_label:
            output = []
            for i, pred in enumerate(predictions):
                output.append({"label": pred["labels"][0], "score": round(pred["scores"][0], 2)})
    
            return {"predictions": output}
            
        else:
            output = []
            for i, pred in enumerate(predictions):
                output.append({"label": pred["labels"], "score": [round(score, 2) for score in pred["scores"]]})
                
            return {"predictions": output}
