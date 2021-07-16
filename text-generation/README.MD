## Token Classification service

Text Generation using Transformers on AWS Lambda. Check root readme for complete setup info.

## Request format

```
{
    "texts": ["India is", "AI will"],
    "model_name": "distilgpt2",  # optional
    "tokenizer_name": "distilgpt2",  # optional
    "max_len": 10, # maximum no. of token(words) to be genrated using the given context optional
    "num_return_sequences": 1 # no. of sequences(sentences) to be genrated using the given context optional
}
```

## Response format

```
{
'predictions': [
                [{'generated_text': 'India is a great help in terms of the security of our species. The'}], 
                [{'generated_text': "AI will rule this week, though we won't know until the end of"}]
            ]
}
```
