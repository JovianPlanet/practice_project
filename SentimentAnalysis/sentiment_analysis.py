""" Invokes the Watson NLP library
    to perform sentiment analysis
"""

import json
import requests

def sentiment_analyzer(text_to_analyse):
    """
    Analyzes sentimente in a text
    returns dictionary wits sentiment label and score
    """
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    injson = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=injson, headers=header)#, timeout=10)
    formatted_response = json.loads(response.text)
    score = None
    label = None
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500:
        label = None
        score = None

    return {'label': label, 'score': score}
