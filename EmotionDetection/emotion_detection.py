import requests
import json

def emotion_detector(text_to_analyze):
    if text_to_analyze.strip() == '':
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
            "status_code": 400
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    payload = {
         "raw_document": {
             "text": text_to_analyze 
            }
        }
    try:
        response = requests.post(url, json = payload, headers = headers)
        json_response = json.loads(response.text)
        emotions = json_response['emotionPredictions'][0]['emotion']
        dominante = max(emotions, key=emotions.get)
        emotions['dominant_emotion'] = dominante


        return emotions
    except Exception as e:
        return {"error": str(e)}

