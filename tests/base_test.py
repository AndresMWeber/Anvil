import unittest
from pprint import pformat, pprint
from deepdiff import DeepDiff
from six import iteritems, string_types

import anvil
from anvil.log import obtainLogger
from collections import Iterable
from collections import OrderedDict
import nomenclate

NOMENCLATE = nomenclate.Nom()


class TestBase(unittest.TestCase):
    LOG = obtainLogger('testing')

    def safe_create(self, dag_path, object_type, name_tokens=None, **flags):
        name_tokens = name_tokens or {}
        if anvil.runtime.dcc.scene.exists(dag_path):
            return object_type(dag_path, **flags)
        else:
            node = object_type.build(**flags)
            node.rename(NOMENCLATE.get(**name_tokens))
            return node

    def setUp(self):
        #anvil.LOG.setLevel(anvil.log.logging.CRITICAL)
        self.fixtures = []

    def tearDown(self):
        pass

    @classmethod
    def delete_objects(cls, objects):
        TestBase.LOG.info('Deleting objects %s' % objects)
        for object in objects:
            if anvil.runtime.dcc.scene.exists(object):
                anvil.runtime.dcc.scene.delete(object, hierarchy=True)

    @classmethod
    def deep_sort(cls, obj):
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

    @staticmethod
    def checkEqual(list_a, list_b):
        return len(list_a) == len(list_b) and sorted(list_a) == sorted(list_b)

    def assertListSame(self, list1, list2):
        print(sorted(list1))
        print(sorted(list2))
        for x, y in zip(sorted(list1), sorted(list2)):
            self.assertEqual(x, y)
        return True

    def assertDictEqual(self, d1, d2, msg=None):  # assertEqual uses for dicts
        for k, v1 in iteritems(d1):
            self.assertIn(k, d2, msg)
            v2 = d2[k]
            if (isinstance(v1, Iterable) and
                    not isinstance(v1, string_types)):
                self.checkEqual(v1, v2)
            else:
                self.assertEqual(v1, v2, msg)
        return True

    @staticmethod
    def delete_created_nodes(func):
        def pre_hook():
            initial_scene_tree = anvil.runtime.dcc.scene.get_scene_tree()
            # TestBase.LOG.info('Scene state before running function %s:' % (func.__name__))
            # TestBase.LOG.info(str(pformat(initial_scene_tree, indent=2)))
            return initial_scene_tree

        def post_hook():
            created_scene_tree = anvil.runtime.dcc.scene.get_scene_tree()
            # TestBase.LOG.info('Scene state after running function %s:' % (func.__name__))
            # TestBase.LOG.info(str(pformat(created_scene_tree, indent=2)))
            return created_scene_tree

        def process(initial_scene_tree, post_scene_tree):
            diff = DeepDiff(initial_scene_tree, post_scene_tree)
            # TestBase.LOG.info('Unprocessed DeepDiff:\n%s' % pformat(diff, indent=2))
            created_nodes = []
            deep_diff_added, deep_diff_removed = 'dictionary_item_added', 'dictionary_item_removed'

            for dict_item in list(diff.get(deep_diff_removed, [])) + list(diff.get(deep_diff_added, [])):
                deep_path = tokenize_deep_diff_string(dict_item)
                created_nodes.append(dict_item_from_path(post_scene_tree, deep_path))
            return created_nodes

        def dict_item_from_path(dict_to_query, query_path):
            """
            item_from_path = dict_to_query
            TestBase.LOG.info('Attempting to get item from path %s in dict %s' % (query_path, dict_to_query))
            for path in query_path:
                try:
                    item_from_path = item_from_path.get(path)
                except AttributeError:
                    pass
            return list(item_from_path)
            """
            return query_path[-1]

        def tokenize_deep_diff_string(deep_diff_path_string):
            full_path = [item.replace(']', '') for item in deep_diff_path_string.split('[')]
            full_path.remove('root')
            deep_path = []
            for item in full_path:
                try:
                    deep_path.append(
                        item.strip('\"').strip("\'") if '\"' in item or '\'' in item or item == 'root' else int(item))
                except ValueError:
                    deep_path.append(str(item))
            return deep_path

        def wrapped(self, *args, **kwargs):
            initial_scene_tree = pre_hook()
            func_return = func(self, *args, **kwargs)
            created_scene_tree = post_hook()
            created_nodes = process(initial_scene_tree, created_scene_tree)
            TestBase.LOG.info('<%s> created nodes: %s' % (self, created_nodes))
            TestBase.LOG.info('Scene state is:\n%s' % pformat(created_scene_tree, indent=2))
            TestBase.delete_objects(created_nodes)
            return func_return

        wrapped.__name__ = func.__name__
        return wrapped
