import os
import unittest2
from deepdiff import DeepDiff
from six import iteritems, string_types
from functools import wraps

os.environ['ANVIL_MODE'] = 'TEST'
import anvil
from anvil.log import obtainLogger
import logging
from collections import Iterable
from collections import OrderedDict

from contextlib import contextmanager
import nomenclate

NOMENCLATE = nomenclate.Nom()


class TestBase(unittest2.TestCase):
    LOG = obtainLogger('testing')
    logging.getLogger('pymel.core.nodetypes').setLevel(logging.CRITICAL)
    LOG.setLevel(logging.CRITICAL)

    APOSE = 'APOSE'
    TPOSE = 'TPOSE'
    FOOT = 'FOOT'
    EXTERNALA = 'EXTERNALA'
    HAND_MERC = "HAND_MERC"
    TEMPLATE_FILES = {APOSE: 'test_skeleton_a_pose.ma',
                      TPOSE: 'test_skeleton_t_pose.ma',
                      EXTERNALA: 'test_skeleton_externalA.ma',
                      FOOT: 'test_skeleton_biped_foot.ma',
                      HAND_MERC: "test_skeleton_hand.ma"
                      }

    @classmethod
    def import_template_files(cls, template_file):
        import pymel.core as pm
        import os
        file_path = os.path.join(os.path.dirname(__file__), 'acceptance', cls.TEMPLATE_FILES[template_file])
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

    @classmethod
    def delete_objects(cls, objects):
        cls.LOG.info('Deleting objects %s' % objects)
        for object in objects:
            if anvil.runtime.dcc.scene.exists(object):
                try:
                    anvil.runtime.dcc.scene.delete(object, hierarchy=True)
                except ValueError:
                    anvil.runtime.dcc.scene.delete(anvil.runtime.dcc.scene.list_scene(object + '*'), hierarchy=True)

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

    @classmethod
    def sanitize_scene(cls):
        preexisting_nodes = anvil.runtime.dcc.scene.list_scene_nodes()
        TestBase.LOG.info('Sanitizing Scene of preexisting nodes %s' % preexisting_nodes)
        cls.delete_objects(preexisting_nodes)

    def post_hook(self):
        created_scene_tree = anvil.runtime.dcc.scene.get_scene_tree()
        return created_scene_tree

    def pre_hook(self):
        initial_scene_tree = anvil.runtime.dcc.scene.get_scene_tree()
        return initial_scene_tree

    def process_scene_tree_diff(self, initial_scene_tree, post_scene_tree):
        diff = DeepDiff(initial_scene_tree, post_scene_tree)
        created_nodes = []
        deep_diff_added, deep_diff_removed = 'dictionary_item_added', 'dictionary_item_removed'
        for dict_item in list(diff.get(deep_diff_removed, [])) + list(diff.get(deep_diff_added, [])):
            deep_path = self.tokenize_deep_diff_string(dict_item)
            created_nodes.append(self.dict_item_from_path(post_scene_tree, deep_path))
        return created_nodes

    def dict_item_from_path(self, dict_to_query, query_path):
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

    def tokenize_deep_diff_string(self, deep_diff_path_string):
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

    @classmethod
    def delete_created_nodes(cls, func):
        @wraps(func)
        def wrapped(self, *args, **kwargs):
            self.LOG.info('RUNNING UNITTEST ----------- %s(%s, %s)' % (func.__name__, args, kwargs))
            with cleanup_nodes():
                if hasattr(self, 'build_dependencies'):
                    self.build_dependencies()
                    initial_scene_tree = self.pre_hook()
                    self.LOG.info('Pre-scene: %s' % initial_scene_tree)
                func_return = func(self, *args, **kwargs)
                created_scene_tree = self.post_hook()
                self.LOG.info('Post-scene: %s' % created_scene_tree)
            return func_return

        return wrapped


@contextmanager
def cleanup_nodes():
    TestBase.sanitize_scene()
    yield
    TestBase.sanitize_scene()


def pre_and_post_sanitize_scene(f):
    @wraps(f)
    def wrapper(instance, *args, **kwargs):
        with cleanup_nodes():
            return f(instance, *args, **kwargs)

    return wrapper
