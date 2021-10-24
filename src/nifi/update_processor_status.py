import requests
import json 

def update_processor_status(processor_id:str, new_state:str ='STOPPED', token, url_nifi_api)
  """Starts or stops a processor by retrieving the processor to get 
  the current revision and finally putting a JSON with the desired 
  state towards the API. 

  :param processor_id: Id of the processor to receive the new state.
  :param new_state: String representing the new state, acceptable
                    values are: STOPPED or RUNNING. 
  :param token: a JWT access token for NiFi.
  :param url_nifi_api: URL to the NiFi API
  :return: None
  """  
  # Create header with access token
  header =  {
              'Content-Type':'application/json'
            , 'Authorization': 'Bearer {}'.format(token)
            }

  # GET processor and parse to JSON
  response = requests.get(url_nifi_api + f'/processors/{processor_id}', headers=header)
  processor = json.loads(response.content)
  # You could potentially check here if the current state is already 
  # the desired one and return early.

  # Create a JSON with the new state
  put_dict = {"revision": processor['revision'], "state": new_state, "disconnectedNodeAcknowledged": True}

  # Dump JSON and POST processor
  payload = json.dumps(put_dict).encode('utf8')
  response = requests.put(url_nifi_api + f'/processors/{processor_id}/run-status', headers=header, data=payload)
