# simulate_diabetes_data.py
import random
import time
from google.cloud import pubsub_v1

project_id = "adta5240f238jel"
topic_id = "diabetes-data-stream"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

def generate_diabetes_data():
    return {
        "Pregnancies": random.randint(0, 17),
        "Glucose": random.randint(0, 199),
        "BloodPressure": random.randint(0, 122),
        "SkinThickness": random.randint(0, 99),
        "Insulin": random.randint(0, 846),
        "BMI": round(random.uniform(0, 67.1), 1),
        "DiabetesPedigreeFunction": round(random.uniform(0.078, 2.42), 3),
        "Age": random.randint(21, 81)
    }

while True:
    data = generate_diabetes_data()
    future = publisher.publish(topic_path, str(data).encode("utf-8"))
    print(f"Published message: {future.result()}")
    time.sleep(5)  # Publish every 5 seconds