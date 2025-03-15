import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        response_json = response.json()
        return parse_the_response_json(response_json)
    else:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")

def parse_the_response_json(response_dict):
    prediction = response_dict.get("emotionPredictions", [])
    if not prediction:
        raise Exception("No emotion prediction found in the response.")
    # Expected only one prediction
    emotion_scores = prediction[-1].get("emotion", {})
    anger_score = emotion_scores.get("anger", 0)
    disgust_score = emotion_scores.get("disgust", 0)
    fear_score = emotion_scores.get("fear", 0)
    joy_score = emotion_scores.get("joy", 0)
    sadness_score = emotion_scores.get("sadness", 0)
    emotions = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = dominant_emotion
    return emotions

'''
# For testing purposes 
if __name__=='__main__':
    #result = emotion_detector("I love this new technology.")
    result = emotion_detector("I am so happy I am doing this.")
    
    print(result)
    print(type(result))
'''