## Zero-Shot Classification service   
Zero-Shot using Transformers on AWS Lambda. Check root readme for complete setup info.

## Request format
```
{
        "texts": ["food was great", "food was bad", "i am going out for food"],
        "labels": ["negative", "postive", "neutral"],
        "hypothesis": "The sentiment of the review is {}.",
        "model_name": "typeform/mobilebert-uncased-mnli",
        "tokenizer_name": "typeform/mobilebert-uncased-mnli"
    }
```

## Response format
```
{'predictions':[
        {'label': 'postive', 'score': 0.81},
        {'label': 'negative', 'score': 0.87},
        {'label': 'postive', 'score': 0.59}
        ]
        
}
```