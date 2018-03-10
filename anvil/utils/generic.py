from six import iteritems, itervalues
from collections import OrderedDict


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


def to_size_list(query, desired_length):
    query_list = to_list(query) if query else [None]
    if len(query_list) > desired_length:
        return query_list[:desired_length]
    else:
        return query_list + [query_list[-1]] * (desired_length - len(query_list))


def to_camel_case(input_string):
    tokens = input_string.split('_')
    return tokens[0] + ''.join([token.capitalize() for token in tokens[1:]])


def gen_flatten_dict_depth_two(d):
    """ Taken from:
        https://stackoverflow.com/questions/3835192/flatten-a-dictionary-of-dictionaries-2-levels-deep-of-lists-in-python
        Given the d_inner, return an iterator that provides all the sessions, one by one, converted to tuples.
    """
    for d_inner in itervalues(d):
        for nodes in itervalues(d_inner):
            for node in to_list(nodes):
                yield node


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


def dict_deep_sort(cls, obj):
    """
    https://stackoverflow.com/questions/18464095/how-to-achieve-assertdictequal-with-assertsequenceequal-applied-to-values
    Recursively sort list or dict nested lists
    """
    if isinstance(obj, dict):
        _sorted = OrderedDict()
        for key in sorted(list(obj)):
            _sorted[key] = cls.deep_sort(obj[key])

    elif isinstance(obj, list):
        new_list = []
        for val in obj:
            new_list.append(cls.deep_sort(val))
        _sorted = sorted(new_list)

    else:
        _sorted = obj

    return _sorted


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


class Map(dict):
    """ Taken from:
        https://stackoverflow.com/questions/2352181/how-to-use-a-dot-to-access-members-of-dictionary
    Example:
    m = Map({'first_name': 'Eduardo'}, last_name='Pool', age=24, sports=['Soccer'])
    """

    def __init__(self, *args, **kwargs):
        super(Map, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in iteritems(arg):
                    self[k] = v

        if kwargs:
            for k, v in iteritems(kwargs):
                self[k] = v

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Map, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Map, self).__delitem__(key)
        del self.__dict__[key]
