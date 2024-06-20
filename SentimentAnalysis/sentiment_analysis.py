'''
This module defines a function to analyze sentiment using Watson's
sentiment analysis service.
The `sentiment_analyzer` function sends a text to the Watson sentiment 
analysis API and returns the analysis result.
'''
import json
import requests

def sentiment_analyzer(text):
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    url = (
        'https://sn-watson-sentiment-bert.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/SentimentPredict'
    )
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    my_object = { "raw_document": { "text": text } }
    try:
        resp = requests.post(url, json = my_object, headers = header, timeout=10)
        formatted_response = json.loads(resp.text)
        if 200 == resp.status_code:
            label = formatted_response['documentSentiment']['label']
            score = formatted_response['documentSentiment']['score']
            return {'label' : label, 'score' : score}
        return {'label': None, 'score': None}
    except requests.exceptions.Timeout:
        return "The request timed out"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
