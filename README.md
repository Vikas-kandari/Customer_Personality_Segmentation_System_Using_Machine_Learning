# Customer Personality Segmentation
[![Live Demo](https://img.shields.io/badge/Live-Demo-green)](https://huggingface.co/spaces/VikasKandari1502/Customer-personality-segmentation-system)
## Problem Statement
This project predicts customer personality segments using machine learning techniques. 
Businesses can use this system to categorize customers and target marketing campaigns effectively.

## Solution
We use clustering and classification models to dynamically assign customers to segments.

## Tech Stack
- Python
- FastAPI
- Scikit-learn
- Pandas

## Models Used
- K-Means (Clustering)
- XGBoostClassifier (Classification)

## Project Pipeline
1. Data Ingestion
2. Data Validation
3. Feature Engineering
4. Clustering
5. Classification
6. Model Evaluation
7. Deployment with FastAPI

## 🌐 Deployment
The application is deployed on Hugging Face Spaces using Docker.
Platform: Hugging Face Spaces  
Framework: FastAPI  
Frontend: Jinja2 Template  
Containerization: Docker

## Model Performance
Accuracy : 96%
## How to Run

### Clone the repository
1. use the link "gh repo clone Vikas-kandari/Customer_Personality_Segmentation_System_Using_Machine_Learning"
2.cd project
pip install -r requirements.txt
3.Run this in terminal uvicorn app:app --reload 

## 🚀 Live Demo
Try the deployed application here:
https://huggingface.co/spaces/VikasKandari1502/Customer-personality-segmentation-system
