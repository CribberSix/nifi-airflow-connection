
from src.nifi.get_token import get_token
from src.nifi.update_processor_status import update_processor_status
from src.nifi.get_processor_state import get_processor_state

from src.utils.parse_state import parse_state
from src.utils.pause import pause


def startup_task():          
    # Initialize the following variables according to your setup / needs:
    url_nifi_api = "https://your.cluster.address.com:9443/nifi-api/"
    processor_id = ""  # e.g. hardcoded / pass them via the `provide_context` functionality
    access_payload = "" # e.g. retrieve via Airflow's `BaseHook` functionality

    token = get_token(url_nifi_api, access_payload)
    update_processor_status(processor_id, "RUNNING", token, url_nifi_api)
    pause(60)
    update_processor_status(processor_id, "STOPPED", token, url_nifi_api)


def wait_for_update():
    # Initialize the following variables according to your setup / needs:
    url_nifi_api = ""  
    processor_id = ""  # e.g. pass them via the DAG's `provide_context` functionality
    access_payload = "" # e.g. retrieve the via Airflow's `BaseHook` functionality
    timestamp_property= "last_tms"

    token = get_token(url_nifi_api, access_payload)

    t0 = datetime.now()

    # Get current timestamp
    processor_state = get_processor_state(url_nifi_api, processor_id, token=token)
    value_start = parse_state(processor_state, timestamp_property )

    print("Initial: ", time_start)
    # query and wait until an update happens or we time out. 
    not_yet_updated = True
    while True:
        processor_state = get_processor_state(url_nifi_api, processor_id, token=token)
        value_current = parse_state(processor_state, timestamp_property )

        if time_start == time_current:
            print("Waiting...")
            pause(10)
        else:
            print(f"Update found: {time_current}")
            break

    return None 


def prepare():
    pass

def finalize():
    pass


with DAG(
    dag_id='my_dag_name',
    ) as dag:

    preparation = PythonOperator(
        task_id='preparation',
        python_callable=prepare,
    )
    startup = PythonOperator(
        task_id='startup',
        python_callable=start_nifi,
    )

    waiting_task = PythonOperator(
        task_id='waiting_task',
        python_callable=wait_for_update,
    )

    finalization = PythonOperator(
        task_id='finalization',
        python_callable=finalize,
    )
    preparation >> startup >> waiting_task >> finalization

