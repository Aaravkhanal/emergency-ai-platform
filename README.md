# 🚨 AI Emergency Accident Detection System

An end-to-end AI-powered emergency response platform that detects road accidents from images and automatically alerts emergency services via SMS.

---

## 🔍 Problem Statement
Road accidents often go unreported for crucial minutes. This system uses Computer Vision and AI automation to detect severe accidents and trigger emergency alerts instantly.

---

## ⚙️ System Architecture
Frontend → Backend API → AI Model → Severity Engine → SMS Alert System

---

## 🧠 AI Model
- Object Detection Model (YOLO-based)
- Classes:
  - major_accident
  - car_collision
- Confidence-based filtering
- Bounding box annotation

---

## 🚦 Severity Scoring Logic
Severity score is calculated using:
- Number of vehicles involved
- Collision overlap area
- Detection confidence
- Accident type

Severity Levels:
- LOW
- MEDIUM
- HIGH
- CRITICAL

---

## 📲 Emergency Alert System
- Integrated with Fast2SMS API
- Automatically sends alerts to emergency contacts
- Includes severity, timestamp, and response time

---

## 🛠 Tech Stack
- Python (FastAPI/Flask)
- YOLO (Computer Vision)
- React + Vite
- Fast2SMS API
- OpenCV
- NumPy

---

## 🖼 Screenshots
(Add your screenshots here)

---

## 🚀 How to Run

### Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
