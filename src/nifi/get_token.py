import requests


def get_token(url_nifi_api: str, access_payload: dict):
    """
    Retrieves a JWT token by authenticating the user, makes
    use of the REST API `/access/token`.

    :param url_nifi_api: the basic URL to the NiFi API.
    :param access_payload: dictionary with keys 'username' & 'password' and
                           fitting values.
    :return: JWT Token
    """

    header = {
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
    }
    response = requests.post(
        url_nifi_api + "access/token", headers=header, data=access_payload
    )
    return response.content.decode("ascii")
