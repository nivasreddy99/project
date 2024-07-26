# diabetes_data_pipeline.py
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions

class ParsePubSubMessage(beam.DoFn):
    def process(self, element):
        import json
        return [json.loads(element.decode('utf-8').replace("'", '"'))]

def run():
    pipeline_options = PipelineOptions([
        '--runner=DataflowRunner',
        '--project=adta5240f238jel',
        '--region=us-central1',
        '--temp_location=gs://diabetes-monitoring-data/temp',
        '--streaming'
    ])
    pipeline_options.view_as(StandardOptions).streaming = True

    p = beam.Pipeline(options=pipeline_options)

    (p
     | 'ReadFromPubSub' >> beam.io.ReadFromPubSub(topic='projects/adta5240f238jel/topics/diabetes-data-stream')
     | 'ParseMessage' >> beam.ParDo(ParsePubSubMessage())
     | 'WriteToBigQuery' >> beam.io.WriteToBigQuery(
         'adta5240f238jel:diabetes_dataset.real_time_data',
         schema='Pregnancies:INTEGER,Glucose:INTEGER,BloodPressure:INTEGER,SkinThickness:INTEGER,Insulin:INTEGER,BMI:FLOAT,DiabetesPedigreeFunction:FLOAT,Age:INTEGER',
         create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
         write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND))

    result = p.run()
    result.wait_until_finish()

if __name__ == '__main__':
    run()