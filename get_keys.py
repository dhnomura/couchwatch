def get_keys(input_dict):
    """ Creates a array of key from a dictionary, input(dict) """
    for key, value in input_dict.items():
        if isinstance(value, dict):
            for subkey in get_keys(value):
                yield key + '.' + subkey
        else:
            yield key