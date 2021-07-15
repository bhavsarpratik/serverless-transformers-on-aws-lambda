## Token Classification service

Token Classification using Transformers on AWS Lambda. Check root readme for complete setup info.

## Request format

```
{
        "texts": ["Mark is going back to Germany from South Africa"],
        "model_name": "dslim/bert-base-NER",
        "tokenizer_name": "dslim/bert-base-NER"
    }
```

## Response format

```
{
        'predictions': [{
            "entity_group": "PER",
            "score": 0.9996247887611389,
            "word": "Mark",
            "start": 0,
            "end": 4
        },
            {
            "entity_group": "LOC",
            "score": 0.9998000264167786,
            "word": "Germany",
            "start": 22,
            "end": 29
        },
            {
            "entity_group": "LOC",
            "score": 0.9994221925735474,
            "word": "South Africa",
            "start": 35,
            "end": 47
        }]
    }
```
