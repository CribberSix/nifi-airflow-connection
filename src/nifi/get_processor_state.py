import requests
import json 

def get_processor_state(url_nifi_api:str, processor_id:str, token=None):
    """
    Gets and returns a single processor state.

    Makes use of the REST API 'processors/{processor_id}/state'.

    :param url_nifi_api: String 
    :param processor_id: String
    :param token: JWT access token
    :returns: JSON object processor's state  
    """

    # Authorization header
    if token is None: 
        header =  {'Content-Type':'application/json'}
    else:
        header =  {'Content-Type':'application/json', 'Authorization': 'Bearer {}'.format(token)}

    # GET processor and parse to JSON
    response = requests.get(url_nifi_api + f'processors/{processor_id}/state'
                            , headers=header)
    return json.loads(response.content)
