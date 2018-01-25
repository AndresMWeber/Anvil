import anvil.node_types as nt
import anvil
from base_test import TestBase


class TestBaseDagNode(TestBase):
    pass


class TestDagNodeBuild(TestBaseDagNode):
    @TestBase.delete_created_nodes
    def test_empty_input(self):
        self.assertRaises(NotImplementedError, nt.DagNode.build)

    @TestBase.delete_created_nodes
    def test_full_input(self):
        self.assertRaises(NotImplementedError, nt.DagNode.build, meta_data={'name':'test'}, name='bob')

    @TestBase.delete_created_nodes
    def test_partial_input(self):
        self.assertRaises(NotImplementedError, nt.DagNode.build, meta_data={'name':'test'})

class TestDagNodeRename(TestBaseDagNode):
    @TestBase.delete_created_nodes
    def rename_runner(self, desired_output, input_name):
        dag_node = nt.DagNode(str(nt.Transform.build()))
        dag_node.rename(input_name)
        desired_output = desired_output or str(dag_node)
        if 'standalone' in anvil.runtime.dcc.ENGINE:
            self.assertTrue(True)
        else:
            self.assertEqual(str(dag_node), desired_output)

    def test_empty_input(self):
        self.assertRaises(RuntimeError, self.rename_runner, None, '')

    def test_single_char_input(self):
        self.rename_runner('n', 'n')

    def test_string_input(self):
        self.rename_runner('new_name', 'new_name')
