import warnings
warnings.filterwarnings("ignore")

from functools import lru_cache

from sentence_transformers import SentenceTransformer


from src import config, utils

logger = utils.create_logger(project_name=config.PREDICTION_TYPE, level="INFO")

class SentenceEncoder:
    def __init__(self):
        _ = self.get_sent_encoder(model_name=config.DEFAULT_MODEL_NAME) #warm up

    @staticmethod
    @lru_cache(maxsize=config.CACHE_MAXSIZE)
    def get_sent_encoder(model_name: str) -> SentenceTransformer:
        """loads and returns a SentenceTransformer model specified by model_name argument
        Args:
            model_name (str): Indicating the name of the model

        Returns:
            SentenceTransformer model
        """
        logger.info(f"Loading model: {model_name}")

        model = SentenceTransformer(model_name)
        return model

    def get_clean_text(self, text: str) -> str:
        """Clean the text

        Args:
            text (str): text

        Returns:
            str: clean text
        """        
        return text.strip().lower()

    def __call__(self, request: dict)-> dict:
        """ embeddings of the given list of sentences
        
        Args:
            request (dict): request containing the list of snetences for encoding
        
        Returns:
            dict: list of embeddings for each sentence embedding dimension = (384,)
        """
        texts = [self.get_clean_text(text) for text in request["texts"]]
        
        logger.info(f"Generating embeddings for {len(texts)} sentences")

        model_name = request.get('model_name', config.DEFAULT_MODEL_NAME)

        sentence_encoder = self.get_sent_encoder(model_name)

        embeddings = sentence_encoder.encode(texts)
        
        return {
            "predictions": embeddings
        }

    