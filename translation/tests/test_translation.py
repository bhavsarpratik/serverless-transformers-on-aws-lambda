from src.easy_nmt import translate_records

requests = {
    "records": [
    {
        "id": "11",
        "text": "Nunca volveré a bajar su app se roba tu información bancaria y se autoriza una suscripción que nunca solicitas",
    },
    {
        "id": "12",
        "text": "I will never download your app will steal your bank information and authorizes a subscription you never request",
    },
],
    "target_lang": "en"
}

expected_response = {
    
    "records": [
        {
            "id": "11",
            "translated": "I'll never download your app again. It steals your bank information and authorizes a subscription that you never request.",
            "source_lang": "es",
        },
        {
            "id": "12",
            "translated": "",
            "source_lang": "en",
        },
    ]
}



def test_response():
    global expected_response
    response = translate_records(**requests)
    assert expected_response == response


