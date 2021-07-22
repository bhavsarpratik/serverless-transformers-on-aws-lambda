## Sentence Encoding service

Sentence Encoding using Sentence Transformers on AWS Lambda. Check root readme for complete setup info.

## Request format

```
{
    "texts": ['This framework generates embeddings for each input sentence',
             'Sentences are passed as a list of string.',
             'The quick brown fox jumps over the lazy dog.'],
    "model_name":'paraphrase-MiniLM-L6-v2' (optional)    
}
```

## Response format

```
# returns a list of the shape (348,) for each sentence

{
"vectors": [[-1.76214233e-01  1.20601095e-01 -2.93623984e-01 -2.29858086e-01 ... -0.3186724   0.41656044 -0.05431654  0.14036156  1.0559164   0.53018135]]
}
```
