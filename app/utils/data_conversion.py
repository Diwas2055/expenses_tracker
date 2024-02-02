from collections import namedtuple


def exclude_keys_from_dict(dictionary, keys: list):
    """
    Exclude keys from a dictionary
    :param dictionary: dictionary
    :param keys: list of keys to exclude
    :return: dictionary
    """
    return {k: v for k, v in dictionary.items() if k not in keys}


def convert_into_dict(data, exclude_keys: list = []):
    # Convert the record to a namedtuple
    myrecord = namedtuple("DictRecord", data.keys())

    dict_values = tuple(data.values())
    dict_namedtuple = myrecord(*dict_values)

    # Convert the namedtuple to a dictionary
    dict_data = dict_namedtuple._asdict()
    return exclude_keys_from_dict(dict_data, exclude_keys)
