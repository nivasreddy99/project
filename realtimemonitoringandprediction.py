# diabetes_prediction.py
from google.cloud import bigquery
from google.cloud import aiplatform

client = bigquery.Client()
ai_client = aiplatform.gapic.PredictionServiceClient(client_options={"api_endpoint": "us-central1-aiplatform.googleapis.com"})

def predict_diabetes(event, context):
    query = """
    SELECT *
    FROM `adta5240f238jel.diabetes_dataset.real_time_data`
    ORDER BY timestamp DESC
    LIMIT 1
    """
    query_job = client.query(query)
    results = query_job.result()

    for row in results:
        instances = [{
            "Pregnancies": row['Pregnancies'],
            "Glucose": row['Glucose'],
            "BloodPressure": row['BloodPressure'],
            "SkinThickness": row['SkinThickness'],
            "Insulin": row['Insulin'],
            "BMI": row['BMI'],
            "DiabetesPedigreeFunction": row['DiabetesPedigreeFunction'],
            "Age": row['Age']
        }]

        response = ai_client.predict(
            endpoint="projects/adta5240f238jel/locations/us-central1/endpoints/diabetes_model",
            instances=instances
        )

        prediction_data = {
            "timestamp": row['timestamp'],
            "diabetes_risk": response.predictions[0]
        }
        client.insert_rows_json('adta5240f238jel.diabetes_dataset.predictions', [prediction_data])