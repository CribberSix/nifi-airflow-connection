def parse_state(json_obj, state_key: str):
    """
    Retrieves the value of a state by the key of the state out of the JSON.

    :param json_obj: the processor's general state.
    :param state_key: the key for the specific state.
    :raises ValueError: if the passed key cannot be found in the processor state.
    :return: value of the matching key.
    """
    states = json_obj["componentState"]["localState"]["state"]
    for state in states:
        if state["key"] == state_key:
            value = state["value"]
            return value
    raise ValueError(f"Could not find {state_key} ")
