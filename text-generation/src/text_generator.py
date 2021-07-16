import warnings
warnings.filterwarnings("ignore")

from functools import lru_cache

from transformers import (AutoConfig, AutoModelForCausalLM,
                          AutoTokenizer, pipeline, set_seed)

from src import config, utils

logger = utils.create_logger(project_name=config.PREDICTION_TYPE, level="INFO")

class TextGenerator:
    def __init__(self):
        _ = self.get_text_generator(model_name=config.DEFAULT_MODEL_NAME, tokenizer_name=config.DEFAULT_TOKENIZER_NAME) #warm up

    @staticmethod
    @lru_cache(maxsize=config.CACHE_MAXSIZE)
    def get_text_generator(model_name: str, tokenizer_name: str) -> pipeline:
        """text generation pipeline for the given model and tokenizer

        Args:
            model_name (str): Indicating the name of the model
            tokenizer_name (str): Indicating the name of the tokenizer

        Returns:
            pipeline: text generation pipeline
        """
        logger.info(f"Loading model: {model_name}")

        model_config = AutoConfig.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(
            model_name, config=model_config
        )
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
        text_generator = pipeline(
            "text-generation", model=model, tokenizer=tokenizer
        )
        return text_generator

    def get_clean_text(self, text: str) -> str:
        """Clean the text

        Args:
            text (str): text

        Returns:
            str: clean text
        """        
        return text.strip()

    def __call__(self, request: dict)-> dict:
        """ text generation of the given sentences
        
        Args:
            request (dict): request containing the list of snetence for text generation 
        
        Returns:
            dict: classes of the given text
        """
        texts = [self.get_clean_text(text) for text in request["texts"]]

        model_name = request.get("model_name", config.DEFAULT_MODEL_NAME)
        tokenizer_name = request.get("tokenizer_name", config.DEFAULT_TOKENIZER_NAME)
        
        logger.info(f"Generating text for {len(texts)} sentences")

        set_seed(7)
        text_generator = self.get_text_generator(model_name, tokenizer_name)

        max_len = request.get("max_len", config.DEFAULT_MAX_LEN)
        num_seq = request.get("num_return_sequences", config.DEFAULT_NUM_SEQ)
        generated_text = text_generator(texts, max_length=max_len, num_return_sequences=num_seq)

        return {
            "predictions": generated_text
        }

    