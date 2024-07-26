
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
    '--runner=DirectRunner',  # Use DirectRunner for local execution
])

with beam.Pipeline(options=pipeline_options) as p:
    (p
     | 'ReadData' >> beam.io.ReadFromText('diabetes.csv', skip_header_lines=1)
     | 'Preprocess' >> beam.Map(preprocess_data)
     | 'WriteToJSON' >> beam.io.WriteToText('processed_diabetes_data', file_name_suffix='.json')
    )