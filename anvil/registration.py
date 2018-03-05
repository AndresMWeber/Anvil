from six import iteritems
from functools import wraps
import config as cfg
from anvil.utils.generic import Map
from anvil.utils.generic import to_list, to_size_list


def register_built_nodes(f):
    """ This function automatically digests a dictionary formatted build report of all nodes created and returned
        during function 'f'.  They will be added to the existing dict object self.hierarchy which is a dot notation
        searchable dictionary subclass.  Any additional dictionary objects that are nested will be converted
        to bunch objects.

        Depends on all build node functions being comprised of a dictionary with str keys with the structure:

        {'controls': ..., 'joints': ..., 'nodes': ...}

        Operations based on input/existing types:
            (existing entry, new entry)
            - list, list: it will extend the list with the new list
            - list, object: adds the object to the list
            - dict, dict: it will update the existing dict with new dict
            - object, object: converts the entry to a list

        If there is no existing entry then we will just assign it.

    """

    @wraps(f)
    def wrapper(abstract_grouping, *args, **kwargs):
        skip_register = kwargs.pop('skip_register', False)

        results = f(abstract_grouping, *args, **kwargs)
        if skip_register:
            return results

        for result_id, node in iteritems(results):
            if isinstance(node, tuple):
                node = Map([(node[0], node[1])])
            elif isinstance(node, dict):
                node = Map(node)

            try:
                hierarchy_entry = abstract_grouping.hierarchy[result_id]

                if issubclass(type(hierarchy_entry), dict) and issubclass(type(node), dict):
                    hierarchy_entry.update(node)

                elif isinstance(hierarchy_entry, list):
                    if isinstance(node, list):
                        hierarchy_entry.extend(node)
                    else:
                        hierarchy_entry.append(node)
                else:
                    abstract_grouping.hierarchy[result_id] = [hierarchy_entry, node]

            except KeyError:
                abstract_grouping.hierarchy[result_id] = node
        return results

    return wrapper


def generate_build_report(f):
    @wraps(f)
    def wrapper(abstract_grouping, *args, **kwargs):
        """ Creates a dictionary of created nodes that will be digested later by the node registration function.

        :param args: object, node to sort into the hierarchy, SHOULD be an Anvil node.
        :param kwargs: dict, use kwargs if you want to override the types.
                             By default accepts any key from abstract_grouping.BUILD_REPORT_KEYS
        :return:

        A build report looks like this:

        {'control': {'default': [anvil_controls_or_set_of_controls, ...]},
         'node': {'default': [anvil_nodes_or_set_of_nodes, ...],
                  'user custom hierarchy id': node}},
         'set': {'default': None},
         'joint': {'default': None},

        A top level key will not be present if the result nodes from the wrapped function are not of that type.
        The top level key possibilities are: ['control', 'joint', 'node', 'set']
        """
        skip_report = kwargs.pop('skip_report', False)
        custom_hierarchy_ids = kwargs.pop('hierarchy_id', None)
        nodes_built = f(abstract_grouping, *args, **kwargs)

        if skip_report:
            return nodes_built

        result = {}
        nodes_built = to_list(nodes_built)
        for node, hierarchy_id in zip(nodes_built, to_size_list(custom_hierarchy_ids, len(nodes_built))):
            tag = getattr(node, cfg.ANVIL_TYPE, cfg.NODE_TYPE)
            if hierarchy_id:
                # We are assuming the extra tag is unique and we can just do a plain update instead of checking.
                result.update({tag: {hierarchy_id: node}})
            else:
                result[tag] = result.get(tag, {cfg.DEFAULT: []})
                result[tag][cfg.DEFAULT].append(node)
        return result

    return wrapper
