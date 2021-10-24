import requests
import json


def get_processor(url_nifi_api: str, processor_id: str, token=None):
    """
    Gets and returns a single processor.

    Makes use of the REST API `/processors/{processor_id}`.

    :param url_nifi_api: String
    :param processor_id: String
    :param token: JWT access token
    :returns: JSON object processor
    """

    # Authorization header
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(token),
    }

    # GET processor and parse to JSON
    response = requests.get(url_nifi_api + f"processors/{processor_id}", headers=header)
    return json.loads(response.content)
