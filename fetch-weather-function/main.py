import os
import requests
import json
from google.cloud import pubsub_v1

PROJECT_ID = os.getenv("GCP_PROJECT")
PUBSUB_TOPIC = "weather-alerts"
CITY = os.getenv("CITY")
API_KEY = os.getenv("WEATHER_API_KEY")

def fetch_weather(event, context):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    temp = data['main']['temp']
    condition = data['weather'][0]['main']

    if temp >= 40 or condition.lower() in ['rain', 'storm', 'thunderstorm']:
        alert = {
            "city": CITY,
            "temp": temp,
            "condition": condition,
            "message": f"Alert! Weather condition: {condition}, Temp: {temp}°C"
        }

        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path(PROJECT_ID, PUBSUB_TOPIC)
        publisher.publish(topic_path, json.dumps(alert).encode("utf-8"))
        print("Alert published")
    else:
        print("Weather normal")
