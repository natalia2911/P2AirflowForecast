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
    'P2Prediccion_Version1',
    default_args=default_args,
    description='Grafo de tareas para la segunda practica de CC',
    schedule_interval=timedelta(days=1),#None
)

##############################################
## TASKS:
##############################################

ClonarRepoGit = BashOperator(
    task_id='ClonarRepoGit',
    depends_on_past=True,
    bash_command="git clone https://github.com/natalia2911/P2AirflowForecast.git /tmp/P2AirflowForecast/version1/",
    dag=dag,
)

GitVersion1 = BashOperator(
    task_id='GitVersion1',
    depends_on_past=True,
    bash_command="cd /tmp/P2AirflowForecast/version1/ && git checkout version1",
    dag=dag,
)

UnitTest = BashOperator(
    task_id="UnitTest",
    depends_on_past=False,
    bash_command="cd /tmp/P2AirflowForecast/version1/ && python3 tests.py",
    dag=dag
)

BuildVersion1 = BashOperator(
    task_id='BuildVersion1',
    depends_on_past=True,
    bash_command='cd /tmp/P2AirflowForecast/version1/ && docker build -f Dockerfile -t "practica2v1" .',
    dag=dag,
)


EjecutarVersion1 = BashOperator(
    task_id='EjecutarVersion1',
    depends_on_past=True,
    bash_command="docker run -p 5000:5000 -t practica2v1",
    dag=dag,
)


#Dependencias
ClonarRepoGit >> GitVersion1 >> UnitTest >> BuildVersion1 >> EjecutarVersion1
