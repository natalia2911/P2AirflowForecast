from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import pandas
from pandas import DataFrame
import csv

default_args = {
    'owner': 'Natalia Maria Martir Moreno',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['nataliamartir@correo.ugr.es'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    #'retry_delay': timedelta(minutes=5),
}


#Inicialización del grafo DAG de tareas para el flujo de trabajo
dag = DAG(
    'P2Prediccion_Version2',
    default_args=default_args,
    description='Grafo de tareas para la segunda practica de CC - Version 2',
    schedule_interval=timedelta(days=1),#None
)

##############################################
## TASKS:
##############################################

ClonarRepoGit = BashOperator(
    task_id='ClonarRepoGit',
    depends_on_past=True,
    bash_command="git clone https://github.com/natalia2911/P2AirflowForecast.git /tmp/P2AirflowForecast/version2/",
    dag=dag,
)

GitVersion2 = BashOperator(
    task_id='GitVersion2',
    depends_on_past=True,
    bash_command="cd /tmp/P2AirflowForecast/version2/ && git checkout version2",
    dag=dag,
)

UnitTest = BashOperator(
    task_id="UnitTest",
    depends_on_past=False,
    bash_command="cd /tmp/P2AirflowForecast/version2/ && python3 tests.py",
    dag=dag
)

BuildVersion2 = BashOperator(
    task_id='BuildVersion2',
    depends_on_past=True,
    bash_command='cd /tmp/P2AirflowForecast/version2/ && docker build -f Dockerfile -t "practica2v2" .',
    dag=dag,
)


EjecutarVersion2 = BashOperator(
    task_id='EjecutarVersion2',
    depends_on_past=True,
    bash_command="docker run -p 8000:8000 -t practica2v2",
    dag=dag,
)


#Dependencias
ClonarRepoGit >> GitVersion2 >> UnitTest >> BuildVersion2 >> EjecutarVersion2
