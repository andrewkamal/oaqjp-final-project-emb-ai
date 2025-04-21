import requests
import json

def emotion_detector(text_to_analyse ):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, headers=headers, json=input_json)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        dominant_emotion = max(anger, disgust, fear, joy, sadness)
        if dominant_emotion == anger:
            dominant_emotion = 'anger'
        elif dominant_emotion == disgust:
            dominant_emotion = 'disgust'
        elif dominant_emotion == fear:
            dominant_emotion = 'fear'
        elif dominant_emotion == joy:
            dominant_emotion = 'joy'
        else:
            dominant_emotion = 'sadness'
    elif response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None
    return {'anger': anger, 'disgust': disgust,'fear': fear, 'joy': joy,'sadness': sadness, 'dominant_emotion': dominant_emotion}    