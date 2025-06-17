import base64
import json
from google.cloud import firestore

def send_alert(event, context):
    db = firestore.Client()
    message = json.loads(base64.b64decode(event['data']).decode('utf-8'))

    db.collection("weather_alerts").add({
        "city": message["city"],
        "temperature": message["temp"],
        "condition": message["condition"],
        "message": message["message"],
        "timestamp": firestore.SERVER_TIMESTAMP
    })
    print("Alert logged to Firestore")
