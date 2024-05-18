import requests
import json

def emotion_detector(text_to_analyze):
     url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
     myobj = { "raw_document": { "text": text_to_analyze } }
     headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
     response = requests.post(url, json = myobj, headers=headers)
     formatted_response = json.loads(response.text)
     if response.status_code == 400:
         label = None
         score = None
     elif response.status_code == 200:
 #  here we find the dominat score and return it in the response
          dominant_score = max(formatted_response, key=lambda k: formatted_response[k])
          return formatted_response['dominant_emotion': f'${dominant_score}']
     else:
          return {'label': label, 'score': score}
   
   
               


