import requests
import json

from .get_processor import get_processor


def update_processor_status(processor_id: str, new_state: str, token, url_nifi_api):
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

    # Retrieve processor from `/processors/{processor_id}`
    processor = get_processor(url_nifi_api, processor_id, token)

    # Create a JSON with the new state and the processor's revision
    put_dict = {
        "revision": processor["revision"],
        "state": new_state,
        "disconnectedNodeAcknowledged": True,
    }

    # Dump JSON and POST processor
    payload = json.dumps(put_dict).encode("utf8")
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(token),
    }
    response = requests.put(
        url_nifi_api + f"/processors/{processor_id}/run-status",
        headers=header,
        data=payload,
    )
    return response
