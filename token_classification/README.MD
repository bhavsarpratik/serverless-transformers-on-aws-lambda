## Classification service   
Classification using Transformers on AWS Lambda. Check root readme for complete setup info.

## Request format
```
{
        "texts": ["food was great", "food was bad", "i am going out for food"],
        "model_name": "cardiffnlp/twitter-roberta-base-sentiment",
        "tokenizer_name": "roberta-base"
    }
```

## Response format
```
{
        'predictions': [{
            'label': 'POSITIVE',
            'score': 0.97
        }, {
            'label': 'NEGATIVE',
            'score': 0.95
        }, {
            'label': 'NEUTRAL',
            'score': 0.69
        }]
    }
```