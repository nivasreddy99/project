# Diabetes Monitoring System

## Project Overview

The Diabetes Monitoring System is a cutting-edge, real-time health analytics platform designed to improve diabetes risk assessment and patient care. Leveraging Google Cloud Platform (GCP) services, this system ingests, processes, and analyzes large volumes of health data in real-time, providing valuable insights for healthcare professionals.

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [System Architecture](#system-architecture)
4. [Setup and Installation](#setup-and-installation)
5. [Usage](#usage)
6. [Data Flow](#data-flow)
7. [Machine Learning Model](#machine-learning-model)
8. [API Documentation](#api-documentation)

## Features

- Real-time data ingestion and processing
- Advanced data preprocessing and feature engineering
- Machine learning model for diabetes risk prediction
- Scalable data storage using Google Cloud Storage and BigQuery
- Real-time alerting system for high-risk patients
- RESTful API for data access and integration
- Comprehensive data visualization dashboard

## Technologies Used

- Google Cloud Platform (GCP)
  - Cloud Storage
  - Pub/Sub
  - Dataflow
  - BigQuery
  - AI Platform
  - Cloud Functions
  - Cloud Monitoring
- Apache Beam
- Python
- SQL
- GitHub Actions (CI/CD)

## System Architecture

[Include a high-level system architecture diagram here]

The system consists of the following main components:
1. Data Ingestion: Pub/Sub topics for real-time data streaming
2. Data Processing: Dataflow pipelines for data transformation and feature engineering
3. Data Storage: Cloud Storage for raw data and BigQuery for processed data
4. Machine Learning: BigQuery ML for model training and AI Platform for deployment
5. API Layer: Cloud Functions for data access and predictions
6. Monitoring: Cloud Monitoring for system health and alerting

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nivasreddy99/project.git
   cd project
   ```

2. Set up Google Cloud Project:
   - Create a new GCP project
   - Enable required APIs (refer to `scripts/enable_apis.sh`)
   - Set up service account with necessary permissions

3. Configure environment variables:
   ```bash
   export PROJECT_ID=your-project-id
   export BUCKET_NAME=your-bucket-name
   ```

4. Run the setup script:
   ```bash
   ./scripts/setup.sh
   ```

5. Deploy Dataflow pipelines:
   ```bash
   python src/dataflow/preprocessing_pipeline.py
   python src/dataflow/realtime_processing_pipeline.py
   ```

6. Train the machine learning model:
   ```bash
   bq query < src/ml/train_model.sql
   ```

7. Deploy the API:
   ```bash
   gcloud functions deploy predict_diabetes --runtime python39 --trigger-http
   ```

## Usage

1. Data Ingestion:
   - Upload historical data to Cloud Storage
   - Use the Pub/Sub simulator for real-time data ingestion

2. Data Processing:
   - Monitor Dataflow jobs in the GCP console

3. Accessing Predictions:
   - Use the deployed Cloud Function API for real-time predictions

4. Visualization:
   - Access the Data Studio dashboard (link provided separately)

## Data Flow

1. Raw data is ingested via Cloud Storage (batch) or Pub/Sub (streaming)
2. Dataflow pipelines process and transform the data
3. Processed data is stored in BigQuery
4. The machine learning model is periodically retrained on updated data
5. Real-time predictions are made using the deployed model
6. Results are stored in BigQuery and made available via the API

## Machine Learning Model

The current implementation uses a logistic regression model trained on the Pima Indians Diabetes Database. The model is trained using BigQuery ML and deployed to AI Platform for real-time predictions.

Model performance metrics:
- AUC-ROC: 0.83
- Precision: 0.75
- Recall: 0.68

## API Documentation

API endpoints:
- `GET /patient/{id}`: Retrieve patient data and risk score
- `POST /predict`: Submit patient data for a prediction

For detailed API documentation, refer to `docs/api_spec.yaml`.


