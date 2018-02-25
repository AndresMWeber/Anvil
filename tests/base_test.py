import os
import unittest2
from six import iteritems, string_types
from functools import wraps

os.environ['ANVIL_MODE'] = 'TEST'
import logging
from collections import Iterable
from anvil.utils.scene import sanitize_scene
from contextlib import contextmanager
import nomenclate
import anvil
from anvil.log import obtain_logger

NOMENCLATE = nomenclate.Nom()


class TestBase(unittest2.TestCase):
    LOG = obtain_logger('testing')
    logging.getLogger('pymel.core.nodetypes').setLevel(logging.CRITICAL)
    LOG.setLevel(logging.CRITICAL)

    APOSE = 'APOSE'
    TPOSE = 'TPOSE'
    FOOT = 'FOOT'
    EXTERNALA = 'EXTERNALA'
    HAND_MERC = "HAND_MERC"
    FOOT_WITH_LEG = 'FOOT_WITH_LEG'
    FOOT_WITH_LEG_AND_SOLES = 'FOOT_WITH_LEG_AND_SOLES'
    TEMPLATE_FILES = {APOSE: 'test_skeleton_a_pose.ma',
                      TPOSE: 'test_skeleton_t_pose.ma',
                      EXTERNALA: 'test_skeleton_externalA.ma',
                      FOOT: 'test_skeleton_biped_foot.ma',
                      FOOT_WITH_LEG: 'test_skeleton_biped_foot_with_leg.ma',
                      FOOT_WITH_LEG_AND_SOLES: 'test_skeleton_biped_foot_with_leg_and_soles.ma',
                      HAND_MERC: "test_skeleton_hand.ma"
                      }

    @classmethod
    def import_template_files(cls, template_file):
        import pymel.core as pm
        import os
        file_path = os.path.join(os.path.dirname(__file__), 'resources', cls.TEMPLATE_FILES[template_file])
        cls.LOG.info('Importing file %s from anvil/tests dir' % file_path)
        pm.importFile(file_path, ignoreVersion=True)
        cls.LOG.info('Successfully imported file.')

    @classmethod
    def build_dependencies(cls):
        cls.LOG.info('Building Dependencies...')

    def tearDown(self):
        super(TestBase, self).tearDown()

    def setUp(self):
        super(TestBase, self).setUp()

    def safe_create(self, dag_path, object_type, name_tokens=None, **flags):
        name_tokens = name_tokens or {}
        if anvil.runtime.dcc.scene.exists(dag_path):
            return object_type(dag_path, **flags)
        else:
            node = object_type.build(**flags)
            node.rename(NOMENCLATE.get(**name_tokens))
            return node

    @staticmethod
    def checkEqual(list_a, list_b):
        return len(list_a) == len(list_b) and sorted(list_a) == sorted(list_b)

    def assertListSame(self, list1, list2):
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


@contextmanager
def sanitize():
    sanitize_scene()
    yield
    sanitize_scene()


def clean_up_scene(func):
    @wraps(func)
    def wrapped(self, *args, **kwargs):
        with sanitize():
            if hasattr(self, 'build_dependencies'):
                self.build_dependencies()
            func_return = func(self, *args, **kwargs)
        return func_return

    return wrapped
