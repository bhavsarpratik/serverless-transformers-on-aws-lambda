## Zero-Shot Classification service   
Zero-Shot using Transformers on AWS Lambda. Check root readme for complete setup info.

## Request format for Multi-Class
```
{
        "texts": ["food was great", "food was bad", "i am going out for food"],
        "labels": ["negative", "postive", "neutral"],
        "hypothesis": "The sentiment of the review is {}.",
        "model_name": "typeform/mobilebert-uncased-mnli",
        "tokenizer_name": "typeform/mobilebert-uncased-mnli",
        "multi_label": False
    }
```

## Response format for Multi-Class
```
{'predictions':[
        {'label': 'postive', 'score': 0.8},
        {'label': 'negative', 'score': 0.87},
        {'label': 'postive', 'score': 0.58}
        ]
        
}
```

## Request format for Multi-Label
```
{
        "texts": ["food was great", "food was bad", "i am going out for food"],
        "multi_label": True,
}
```

## Response format for Multi-Label
```
{'predictions': [
                {'label': ['postive', 'neutral', 'negative'], 'score': [0.87, 0.33, 0.0]},
                {'label': ['negative', 'neutral', 'postive'], 'score': [1.0, 0.85, 0.83]},
                {'label': ['postive', 'negative', 'neutral'], 'score': [0.67, 0.34, 0.14]}
                ]
}
```
