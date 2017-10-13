import unittest
from pprint import pformat

from six import iteritems, string_types

import anvil
from anvil import node_types
from collections import Iterable
from collections import OrderedDict


class TestBase(unittest.TestCase):
    def safe_create(self, dag_path, object_type, name_tokens=None, **flags):
        if anvil.runtime.dcc.scene.exists(dag_path):
            return dag_path
        else:
            return node_types.Transform.build(name_tokens=name_tokens, **flags)

    def setUp(self):
        anvil.LOG.info('Initializing maya_utils standalone...')

        global setUp_count
        anvil.LOG.info('setUp-Start state of scene: ')
        anvil.LOG.info(pformat(anvil.runtime.dcc.scene.get_scene_tree()))

        self.fixtures = []
        test_parent_grp = 'test_parent'
        test_grp = '%s|test_GRP' % test_parent_grp

        try:
            self.test_group = self.safe_create(test_grp,
                                               node_types.Transform,
                                               name_tokens={'name': 'test'})

            self.test_group_parent = self.safe_create(test_parent_grp,
                                                      node_types.Transform,
                                                      name_tokens={'name': 'test_parent'})

            self.fixtures.append(self.test_group)
            self.fixtures.append(self.test_group_parent)
        except ImportError:
            pass

        anvil.LOG.info('State of scene after initial node creation: ')
        anvil.LOG.info(pformat(anvil.runtime.dcc.scene.get_scene_tree()))

    def tearDown(self):
        global tearDown_count
        try:
            import maya.cmds as mc
            if self.fixtures:
                self.fixtures = [fixture for fixture in self.fixtures if mc.objExists(fixture)]
                for fixture in self.fixtures:
                    if mc.objExists(fixture):
                        for fix in mc.ls(fixture):
                            mc.delete(fix)
        except ImportError:
            pass

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
