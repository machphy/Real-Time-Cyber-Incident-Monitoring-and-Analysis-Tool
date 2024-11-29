from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from data_pipeline.jobs.ingest_data import ingest_data

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG('data_ingestion_dag', default_args=default_args, schedule_interval='@hourly', start_date=datetime(2024, 1, 1)) as dag:
    ingest_task = PythonOperator(
        task_id='ingest_data',
        python_callable=ingest_data
    )
