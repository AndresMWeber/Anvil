import anvil
import anvil.runtime as rt
import anvil.node_types as nt
import anvil.templates.sub_rig.spine as spine
from base_test import TestBase


class TestBaseTemplates(TestBase):
    name_tokens = {'name': 'eye', 'purpose': 'mvp'}
    test_rig = None


class TestSpineBuild(TestBaseTemplates):
    @TestBase.delete_created_nodes
    def test_build(self):
        joints = []
        for i in range(6):
            joint =nt.Joint.build()
            rt.dcc.scene.position(joint, translate=True, translation=[0,i,0])
            joints.append(joint)

        sub_rig_instance = spine.Spine()
        sub_rig_instance.build(joints, {})

    @TestBase.delete_created_nodes
    def test_build_with_parent(self):
        top = nt.Transform.build()
        joints = []
        for i in range(6):
            joint = nt.Joint.build()
            rt.dcc.scene.position(joint, translate=True, translation=[0, i, 0])
            joints.append(joint)

        sub_rig_instance = spine.Spine()
        sub_rig_instance.build(joints, {}, parent=top)
