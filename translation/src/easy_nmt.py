import json
import os
import time
from typing import List, Optional

from easynmt import EasyNMT

model_name = os.getenv('EASYNMT_MODEL', 'opus-mt')
model_args = json.loads(os.getenv('EASYNMT_MODEL_ARGS', '{}'))
print("Load model: "+ model_name)
model = EasyNMT(model_name, load_translator=True, **model_args)


def translate_records(target_lang: str, records: List[dict], source_lang: Optional[str] = '', beam_size: Optional[int] = 5, perform_sentence_splitting: Optional[bool] = True):
    """
    Translates the records to the given target language.
    :param records: Record that should be translated
    :param target_lang: Target language
    :param source_lang: Language of text. Optional, if empty: Automatic language detection
    :param beam_size: Beam size. Optional
    :param perform_sentence_splitting: Split longer documents into individual sentences for translation. Optional
    :return:  Returns a json with the translated records
    """


    # if 'EASYNMT_MAX_TEXT_LEN' in os.environ and len(text) > int(os.getenv('EASYNMT_MAX_TEXT_LEN')):
    #     raise ValueError("Text was too long. Only texts up to {} characters are allowed".format(os.getenv('EASYNMT_MAX_TEXT_LEN')))

    # if beam_size < 1 or ('EASYNMT_MAX_BEAM_SIZE' in os.environ and beam_size > int(os.getenv('EASYNMT_MAX_BEAM_SIZE'))):
    #     raise ValueError("Illegal beam size")

    if len(source_lang.strip()) == 0:
        source_lang = None


    start_time = time.time()
    output = {"target_lang": target_lang}

    texts = [record["text"] for record in records]

    detected_langs = model.language_detection(texts)
    
    translations = model.translate(texts, target_lang=target_lang, source_lang=source_lang, beam_size=beam_size, perform_sentence_splitting=perform_sentence_splitting, batch_size=int(os.getenv('EASYNMT_BATCH_SIZE', 16)))
    for translation, detected_lang, record in zip(translations, detected_langs, records):
        record["translated"] = translation
        if translation == record["text"]:
            record["source_lang"] = target_lang
            record["translated"] = ""
        else:
            record["source_lang"] = detected_lang
        del record["text"]

    output["records"] = records
    output['translation_time'] = time.time()-start_time
    return output
