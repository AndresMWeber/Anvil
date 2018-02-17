from six import iteritems


def to_list(query):
    if isinstance(query, list):
        return query
    elif isinstance(query, str):
        return [query]
    elif query is None:
        return list()
    try:
        return list(query)
    except TypeError:
        return [query]


def to_camel_case(input_string):
    tokens = input_string.split('_')
    return tokens[0] + ''.join([token.capitalize() for token in tokens[1:]])


def get_dict_depth(d=None, level=0):
    """ Returns maximum depth of the hierarchy
    """
    if not isinstance(d, dict) or not d:
        return level
    return max(get_dict_depth(d[k], level=level + 1) for k in d)


def get_dict_key_matches(key, dictionary):
    for k, v in iteritems(dictionary):
        if k == key:
            return {k: v}
        elif isinstance(v, dict):
            return get_dict_key_matches(key, v)


def dict_to_keys_list(d, keys=None):
    keys = keys if keys is not None else []
    if isinstance(d, dict):
        for k, v in iteritems(d):
            keys.append(k)
            dict_to_keys_list(v, keys)
    else:
        keys.append(d)
    return keys


def to_str_dict(d):
    data = {}
    for k, v in iteritems(d):
        try:
            data.update({str(k): str(v)})
        except TypeError:
            pass
    return data


def pop_dict_keys(d, keys):
    popped = []
    for key in keys:
        try:
            popped.append(d.pop(key))
        except KeyError:
            pass
    return popped


def merge_dicts(*args, **kwargs):
    """ Outputs a merged dictionary from inputs. Overwrites data if there are conflicts from left to right.

    :param args: (dict), tuple of input dictionaries
    :param kwargs: dict, input kwargs to merge
    :return: dict, combined data.
    """
    data = {}
    for input_dict in [arg for arg in args if isinstance(arg, dict)] + [kwargs]:
        data.update(input_dict)
    return data


def dict_compare(d1, d2):
    """ Taken from: https://stackoverflow.com/questions/4527942/comparing-two-dictionaries-in-python
    """
    d1_keys = set(list(d1))
    d2_keys = set(list(d2))
    intersect_keys = d1_keys.intersection(d2_keys)
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys
    modified = {o: (d1[o], d2[o]) for o in intersect_keys if d1[o] != d2[o]}
    same = set(o for o in intersect_keys if d1[o] == d2[o])
    return added, removed, modified, same
