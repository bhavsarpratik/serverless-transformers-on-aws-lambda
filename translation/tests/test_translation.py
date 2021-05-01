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
     {
      "id": "13",
      "text": "Je ne téléchargerai jamais votre application volera"
    }
],
    "target_lang": "en",
    "source_lang": "ROMANCE"
}

expected_response = {'target_lang': 'en', 
                     'records': [
                         {'id': '11', 'translated': "I'll never download your app again, steal your bank information and authorize a subscription that you never ask for.", 'source_lang': 'es'}, 
                         {'id': '12', 'translated': '', 'source_lang': 'en'}, 
                         {'id': '13', 'translated': 'I will never download your app will fly', 'source_lang': 'fr'}]
                    }



def test_response():
    global expected_response
    response = translate_records(**requests)
    del response["translation_time"]
    assert expected_response == response


