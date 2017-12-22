import anvil
import anvil.config as cfg
import anvil.runtime as rt
from six import iteritems


def to_list(query):
    if isinstance(query, list):
        return query
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


def get_node_hierarchy_as_dict(node_or_nodes, tree=None, node_filter=None):
    nodes = to_list(node_or_nodes)

    if tree is None:
        tree = dict()

    for tree_child in nodes:
        anvil_node = anvil.factory(tree_child)
        try:
            relative_tree = tree[anvil_node]
        except KeyError:
            tree[anvil_node] = dict()
            relative_tree = tree[anvil_node]

        node_filter_kwargs = {cfg.TYPE: node_filter} if node_filter else {}
        children = rt.dcc.scene.list_relatives(tree_child, fullPath=True, children=True, **node_filter_kwargs) or []
        if children:
            get_node_hierarchy_as_dict(children, relative_tree, node_filter=node_filter)
    return tree


def dict_to_keys_list(d, keys=None):
    keys = keys if keys is not None else []
    if isinstance(d, dict):
        for k, v in iteritems(d):
            keys.append(k)
            dict_to_keys_list(v, keys)
    else:
        keys.append(d)
    return keys


def validate_and_cast_to_list_of_type(reference_objects, cast_type=str):
    reference_objects = to_list(reference_objects)
    return [cast_type(reference_object) for reference_object in reference_objects if
            reference_object is not None and rt.dcc.scene.exists(reference_object)]
