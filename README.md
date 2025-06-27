# ⛅ Weather Alert App – GCP Powered

A **cloud-native weather alert system** using **Google Cloud Platform** that:
- Fetches weather data every hour via **Cloud Scheduler + Cloud Functions**
- Sends critical weather alerts via **Pub/Sub**
- Logs alerts to **Firestore** for permanent record

---

## 🚀 Features

- 🌦️ Fetches live weather using OpenWeatherMap API
- 🔔 Sends alerts for extreme heat, rain, or storm
- ☁️ Cloud Functions used as compute logic
- 🔄 Triggered hourly by Cloud Scheduler
- 📬 Pub/Sub message pipeline
- 🗃️ Firestore alert logs
- 🔐 Safe environment variable handling

---

## 🧩 Tech Stack

| Layer        | Tool/Service              |
|--------------|---------------------------|
| API          | OpenWeatherMap API        |
| Backend      | Python (Cloud Functions)  |
| Messaging    | Pub/Sub                   |
| Database     | Firestore (NoSQL)         |
| Scheduler    | Cloud Scheduler           |
---
