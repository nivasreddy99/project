# diabetes_preprocessing.py
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

def preprocess_data(element):
    values = element.split(',')
    return {
        'Pregnancies': int(values[0]),
        'Glucose': int(values[1]),
        'BloodPressure': int(values[2]),
        'SkinThickness': int(values[3]),
        'Insulin': int(values[4]),
        'BMI': float(values[5]),
        'DiabetesPedigreeFunction': float(values[6]),
        'Age': int(values[7]),
        'Outcome': int(values[8])
    }

pipeline_options = PipelineOptions([
    '--runner=DataflowRunner',
    '--project=adta5240f238jel',
    '--region=us-central1',
    '--temp_location=gs://diabetes-monitoring-data/temp',
])

with beam.Pipeline(options=pipeline_options) as p:
    (p
     | 'ReadData' >> beam.io.ReadFromText('gs://diabetes-monitoring-data/raw/diabetes.csv', skip_header_lines=1)
     | 'Preprocess' >> beam.Map(preprocess_data)
     | 'WriteToBigQuery' >> beam.io.WriteToBigQuery(
         'adta5240f238jel.diabetes_dataset.processed_data',
         schema='Pregnancies:INTEGER,Glucose:INTEGER,BloodPressure:INTEGER,SkinThickness:INTEGER,Insulin:INTEGER,BMI:FLOAT,DiabetesPedigreeFunction:FLOAT,Age:INTEGER,Outcome:INTEGER',
         create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
         write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE))