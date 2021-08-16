from datetime import datetime
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow import DAG

# i'm a new release and new branch
default_args = {
    'start_date': datetime(2019, 1, 1),
    'owner': 'Airflow',
}


def process(p1):
    print(p1)
    return 'done'


with DAG(dag_id='new_dag', schedule_interval='0 0 * * *', default_args=default_args, catchup=False) as dag:

    # Tasks dynamically generated
    task_1 = BashOperator(task_id='task_6', bash_command='sleep 60')

    task_1
