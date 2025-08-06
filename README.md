# 🧬 Hope Hub – AI Cancer Detection Platform

An AI-powered Flask-based web app to detect Skin, Brain, and Lung cancer using trained ML models.  
Generates PDF reports and logs patient metadata for dataset analysis.

## 🚀 Features
- Upload medical images (Skin, Brain, Lung)
- Predicts cancer type using TensorFlow models
- PDF report generation
- Dataset log with metadata
- User authentication (signup/login)

## 🛠️ Tech Stack
Flask, TensorFlow, Keras, OpenCV, Bootstrap

## 📁 Folder Structure
- `app.py` – Main Flask app
- `/templates` – HTML pages
- `/static` – CSS, images, uploads
- `/models` – Pretrained `.h5` ML models
- `/reports` – Generated PDFs

## 🔗 Download Pretrained Models

The following models are required to run this project. Please download them manually and place them in the `models/` directory:

- [Brain Tumor Classifier (.h5)](https://drive.google.com/file/d/1fhJZ2DEcYpkTGnLEc0tNJikpdZJvoctW/view?usp=drive_link)
- [Skin Cancer Binary Model (.h5)](https://drive.google.com/file/d/15pN-khXm_NDXSsqMW4ZNkZha2gzcOAWZ/view?usp=drive_link)

> ⚠️ Note: These files are not included in the repository due to size limits.
