import unittest
from pprint import pformat, pprint
from deepdiff import DeepDiff
from six import iteritems, string_types

import anvil
from anvil import node_types as nt
from collections import Iterable
from collections import OrderedDict
import nomenclate

NOMENCLATE = nomenclate.Nom()


class TestBase(unittest.TestCase):
    def safe_create(self, dag_path, object_type, name_tokens=None, **flags):
        name_tokens = name_tokens or {}
        if anvil.runtime.dcc.scene.exists(dag_path):
            return object_type(dag_path, **flags)
        else:
            node = object_type.build(**flags)
            node.rename(NOMENCLATE.get(**name_tokens))
            return node

    def setUp(self):
        anvil.LOG.info('Test(%s).setUp-Start state of scene: ' % self.__class__)
        anvil.LOG.info(pformat(anvil.runtime.dcc.scene.get_scene_tree()))
        self.fixtures = []

    def tearDown(self):
        pass

    @classmethod
    def delete_objects(cls, objects):
        for object in objects:
            if anvil.runtime.dcc.scene.exists(object):
                anvil.runtime.dcc.scene.delete(object)

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
        def wrapped(*args, **kwargs):
            initial_scene_tree = anvil.runtime.dcc.scene.get_scene_tree()
            anvil.LOG.info('Scene state before running function %s:' % func)
            anvil.LOG.info(str(pformat(initial_scene_tree, indent=2)))
            func_return = func(*args, **kwargs)

            created_scene_tree = anvil.runtime.dcc.scene.get_scene_tree()
            anvil.LOG.info('Scene state after running function %s:' % func)
            anvil.LOG.info(str(pformat(created_scene_tree, indent=2)))

            diff = DeepDiff(initial_scene_tree, created_scene_tree)
            anvil.LOG.info('New or deleted nodes: %s' % pformat(diff))
            # TestBase.delete_objects(diff)

            return func_return
        wrapped.__name__ = func.__name__
        return wrapped
