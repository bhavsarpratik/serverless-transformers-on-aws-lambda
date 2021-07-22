## Text Generation service

Text Generation using Transformers on AWS Lambda. Check root readme for complete setup info.

## Request format

```
{
    "texts": ["India is", "AI will"],
    "model_name": "distilgpt2",  (optional argument)
    "tokenizer_name": "distilgpt2",  (optional argument)
    "max_len": 10, # maximum no. of token(words) to be genrated using the given context (optional argument)
    "num_return_sequences": 1 # no. of sequences(sentences) to be genrated using the given context (optional argument)
}
```

## Response format

```
{
'predictions': [
                [{'generated_text': 'India is a great country for international investors. It also has the support of'}],
                [{'generated_text': 'AI will rule out that she cannot be allowed to wear a hijab but will'}]
            ]
}
```