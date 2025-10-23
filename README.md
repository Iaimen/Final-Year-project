# IoT-Based Sustainable Living Guide Application 🌿

## 📘 Project Overview
The **IoT-Based Sustainable Living Guide Application** is a full-stack web and mobile system that promotes environmental sustainability by monitoring, analyzing, and predicting air quality and carbon footprint levels using IoT sensors and Machine Learning. This project integrates **Django (Backend)**, **React (Frontend)**, **Android Studio (Mobile App)**, and **IoT sensors (MQ135, MQ7, DHT22)** to provide real-time environmental insights, actionable recommendations, and sustainability forecasts.

---

## ⚙️ Key Components
- **IoT Integration:** Sensors (MQ135, MQ7, DHT22) collect air pollutant data using an ESP32 microcontroller.
- **Database Management:** Sensor data stored in MySQL via Django backend.
- **Machine Learning (Random Forest):** Predicts future carbon footprint levels based on current and historical pollutant data.
- **Notifications:** Alerts users when the environment becomes unsustainable.
- **Frontend (React):** Displays dashboards, analytics, and forecasted environmental values.
- **Mobile App (Android Studio):** Provides real-time alerts and sustainable recommendations.
- **AI Chatbot:** Provides sustainability guidance and suggestions based on air quality analysis.

---

## 🚀 Features
### 🌍 IoT Data Collection
- Real-time monitoring of environmental parameters such as:
  - Carbon Dioxide (CO₂)
  - Carbon Monoxide (CO)
  - Ammonia (NH₃)
  - Benzene (C₆H₆)
  - Temperature and Humidity

### 📈 Data Analytics & Visualization
- Live sensor data charts (bar and line graphs)
- 7-day forecast using **XGBoost Machine Learning Model**
- Comparison of forecasted vs current pollution levels

### 🤖 Machine Learning Integration (XGBoost)
- Trained on `sensor_data.csv` (20,000+ readings)
- Predicts future carbon footprint
- Generates sustainability insights

### 🔔 Notifications System
- Alerts users when carbon footprint exceeds sustainable thresholds
- Shows forecasted environmental insights on dashboard

### 💬 Smart Chatbot
- Green-themed AI assistant for sustainability queries
- Provides actionable eco-friendly recommendations
- Integrated with Django backend (data stored in local DB)

### 🔐 Authentication
- Custom Signup and Login (Django + React)
- Secure user data storage in MySQL

---

## 🧩 Folder Structure

```
backend/
├── myapp/
│   ├── models/
│   ├── views.py
│   ├── urls.py
│   ├── utils/
│   ├── xgboost_model/
│   │   ├── train_xgboost.py
│   │   ├── predict_xgboost.py
│   │   ├── xgboost_model.json
│   ├── sensor_data.csv
│   ├── read_serial_and_save_csv.py
│   └── templates/
│
└── manage.py

frontend/
├── src/
│   ├── components/
│   ├── pages/
│   ├── App.js
│   └── index.js
└── package.json
```

---

## 🛠️ Installation & Setup Guide

### 1. Clone the Repository
```bash
git clone https://github.com/aiman-mumtaz/sustainable-living-guide.git
cd sustainable-living-guide
```

### 2. Backend Setup (Django)
```bash
cd backend
python -m venv venv
venv\Scripts\activate      # For Windows
source venv/bin/activate     # For Mac/Linux

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 3. Frontend Setup (React)
```bash
cd frontend
npm install
npm start
```

### 4. IoT Setup (Arduino + ESP32)
- Connect MQ135, MQ7, DHT22 sensors to ESP32
- Flash Arduino code to send serial data
- Run `read_serial_and_save_csv.py` in backend to store sensor values in `sensor_data.csv`

```bash
python myapp/read_serial_and_save_csv.py
```

---

## 🧠 Machine Learning Setup (Random Forest)

### 1. Train Model
Run the training script to generate `random_forest.ipynb

### 2. Predict Future Values
Predict carbon footprint based on new sensor readings:
```bash
python myapp/xgboost_model/random_forest.py
```

### 3. API Endpoint for Predictions
Backend API to fetch forecasted values:
```
GET /get_forecast/?temperature=30.5&humidity=45&co2=0.22&nh3=0.14&co=0.38
```

Sample Response:
```json
{
  "forecast": 12.56
}
```

---

## 🔔 Notifications Integration
Notifications are triggered when forecasted carbon footprint exceeds sustainable thresholds (e.g., >15).  
These notifications appear on the frontend dashboard and mobile app.

---

## 📱 Mobile App Integration
- Built using **Android Studio**
- Fetches API data from Django backend
- Displays sustainability tips, real-time sensor data, and forecasts

---

## 🧩 Technologies Used
| Category | Technologies |
|-----------|--------------|
| **Frontend** | React.js, Chart.js, HTML, CSS, JavaScript |
| **Backend** | Django, MySQL, REST API |
| **IoT** | ESP32, Arduino IDE, MQ135, MQ7, DHT22 |
| **Machine Learning** | Python, XGBoost, scikit-learn, Pandas |
| **Mobile App** | Android Studio, Java/Kotlin |
| **Notifications** | Django channels / custom push system |

---

## 📊 Future Enhancements
- Integrate more sensors for water and noise pollution
- Add deep learning models for more accurate forecasts
- Expand chatbot with NLP for sustainability education
- Deploy app on AWS / Render for public access

---

## 👩‍💻 Author  

### 🎓 Final Year Project – *IoT-Based Sustainable Living Guide Application*  

**Supervisor:**  
**Syed Ali Haider Naqvi**  
📧 [alihaider@lgu.edu.pk](mailto:alihaider@lgu.edu.pk)  
🌐 [LinkedIn](https://www.linkedin.com/in/syed-ali-haider-n-32a132124/)  

---

**Group Member 1:**  
**Shahzada Rizwan Ali**  
📧 [shahzadarizwanali01@gmail.com](mailto:shahzadarizwanali01@gmail.com)  
🌐 [LinkedIn](https://www.linkedin.com/in/shahzadarizwanali)  

**Group Member 2:**  
**Aiman Mumtaz**  
📧 [aimanmumtaz@example.com](mailto:aimanmumtaz@example.com)  
🌐 [LinkedIn](https://www.linkedin.com/in/aimanmumtaz-se)  

  
