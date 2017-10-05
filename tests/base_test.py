import unittest
import maya.cmds as mc
import anvil
from collections import Iterable
from six import iteritems, string_types
from pprint import pformat
from collections import OrderedDict


setUp_count = 0
tearDown_count = 0


class TestBase(unittest.TestCase):
    def setUp(self):
        anvil.LOG.info('Initializing maya_utils standalone...')

        global setUp_count
        anvil.LOG.info('setup has run %d times.' % setUp_count)
        anvil.LOG.info('setUp-Start state of scene: ')
        anvil.LOG.info(pformat(anvil.plugins.maya.scene.get_scene_tree()))

        self.fixtures = []
        test_parent_grp = 'test_parent'
        test_grp = '%s|test_GRP' % test_parent_grp

        self.test_group = test_grp if mc.objExists(test_grp) else anvil.core.objects.transform.Transform.build(n='test', em=True)
        self.test_group_parent = test_parent_grp if mc.objExists(
            test_parent_grp) else anvil.core.objects.transform.Transform.build(n='test_parent')

        self.fixtures.append(self.test_group)
        self.fixtures.append(self.test_group_parent)
        anvil.LOG.info('state of scene after initial node creation: ')
        anvil.LOG.info(pformat(anvil.plugins.maya.scene.get_scene_tree()))
        anvil.LOG.info('Registered nodes %s' % self.fixtures)
        setUp_count += 1

    def tearDown(self):
        global tearDown_count
        anvil.LOG.info('Tearing down!! Deleting all nodes...')
        if self.fixtures:
            self.fixtures = [fixture for fixture in self.fixtures if mc.objExists(fixture)]
            for fixture in self.fixtures:
                if mc.objExists(fixture):
                    for fix in mc.ls(fixture):
                        mc.delete(fix)
        tearDown_count += 1

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