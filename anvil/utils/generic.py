from six import iteritems, itervalues
from collections import OrderedDict, MutableMapping, Iterable
from functools import wraps
import anvil.config as cfg


def to_list(query):
    if isinstance(query, list):
        return query
    elif isinstance(query, str):
        return [query]
    elif isinstance(query, dict):
        return [query]
    elif not query:
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
    """Taken from:

    https://stackoverflow.com/questions/3835192/flatten-a-dictionary-of-dictionaries-2-levels-deep-of-lists-in-python
    Given the d_inner, return an iterator that provides all the nodes from within.

    """
    for d_inner in itervalues(d):
        if isinstance(d_inner, dict):
            for nodes in itervalues(d_inner):
                print('nodes ', nodes)
                for node in to_list(nodes):
                    print(node)
                    yield node
        else:
            for node in to_list(d_inner):
                print('node ', node)
                yield node


def get_dict_depth(d=None, level=0):
    """Returns maximum depth of the hierarchy"""
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
    """Recursively sort list or dict nested lists

    Taken from: http://goo.gl/tQfDP6
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
    """Outputs a merged dictionary from inputs. Overwrites data if there are conflicts from left to right.

    :param args: (dict), tuple of input dictionaries
    :param kwargs: dict, input kwargs to merge
    :return: dict, combined data.
    """
    data = {}
    for input_dict in [arg for arg in args if isinstance(arg, dict)] + [kwargs]:
        data.update(input_dict)
    return data


def dict_compare(d1, d2):
    """Taken from: https://stackoverflow.com/questions/4527942/comparing-two-dictionaries-in-python"""
    d1_keys = set(list(d1))
    d2_keys = set(list(d2))
    intersect_keys = d1_keys.intersection(d2_keys)
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys
    modified = {o: (d1[o], d2[o]) for o in intersect_keys if d1[o] != d2[o]}
    same = set(o for o in intersect_keys if d1[o] == d2[o])
    return added, removed, modified, same


def dict_to_flat_dict(d, full_path=True, parent_key='', sep='_'):
    """Got from https://stackoverflow.com/questions/6027558/flatten-nested-python-dictionaries-compressing-keys

    :param d: dict, input dictionary
    :param full_path: bool, whether to store the full path as the key or the final key for that dictionary item.
    :param parent_key: str, keeps track of the dictionary path taken, do not set.
    :param sep: str, arbitary separator to delineate path separation in the parent_key string.
    :return: dict, flat dictionary with all keys as full path keys.
    """
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key and full_path else k
        if isinstance(v, MutableMapping):
            items.extend(dict_to_flat_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


merge_value_LUT = {
    dict: lambda d1, d2: merge_dicts(d2),
    list: lambda l1, l2: l1 + to_list(l2),
    str: lambda s1, s2: s1 + str(s2),
    'replace': lambda e1, e2: e2,
}


class Map(dict):
    """A dot notation accessible dictionary class extension.

    Taken from: https://stackoverflow.com/questions/2352181/how-to-use-a-dot-to-access-members-of-dictionary
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

    def deep_update(self, d, path=None):
        if path is None:
            path = []
        for k, v in iteritems(d):
            if isinstance(v, dict):
                self.deep_update(v, path=path + [k])
            else:
                self._merge_value(path + [k], v)

    def flatten(self):
        return gen_flatten_dict_depth_two(self)

    def to_flat_dict(self, full_path=False):
        return dict_to_flat_dict(self, full_path=full_path)

    def to_value_list(self):
        result = []
        map(result.extend, [n if isinstance(n, Iterable) else to_list(n) for n in itervalues(self.to_flat_dict())])
        return result

    def _merge_value(self, path, v):
        """Stably merge values without overwriting or messing up Map object.

        This is used since we have a slightly customized way of adding entries and do not want the base Map object
        to start getting stale data.  If a path does not exist, we will add a default Map object in that place
        unless it is the final path, in which case we merge with the existing (or not) value.

        :param path: list, list of keys we will traverse down.
        :param v: object, any type of object we are adding to that nested/base dict.
        """
        current_map = self
        for p in path[:-1]:
            current_map = current_map.setdefault(p, self.__class__())
        current_v = current_map.setdefault(path[-1], None)
        current_map[path[-1]] = merge_value_LUT.get(type(current_v), merge_value_LUT['replace'])(current_v, v)

    def __getattr__(self, attr):
        """Passthrough function for dictionary.get"""
        return self.get(attr)

    def __setattr__(self, key, value):
        """Passthrough function for dictionary item setter"""
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        """Updates both setitem and instance dictionary key value"""
        super(Map, self).__setitem__(key, value)
        self.__dict__[key] = value

    def __delattr__(self, item):
        """Passthrough for dictionary delete item."""
        self.__delitem__(item)

    def __delitem__(self, key):
        """Deletes both the attribute and the instance dictionary"""
        super(Map, self).__delitem__(key)
        del self.__dict__[key]

    def __eq__(self, other):
        """Determines if the dictionary is equivalent to the other dictionary."""
        return dict_compare(self.__dict__, other)


def extend_parent_kwarg(number_of_parents):
    def inner(f):
        @wraps(f)
        def wrapper(abstract_grouping, *args, **kwargs):
            kwargs[cfg.PARENT] = iter(to_size_list(kwargs.get(cfg.PARENT), number_of_parents))
            return f(abstract_grouping, *args, **kwargs)

        return wrapper

    return inner
