import dag_node
import anvil.runtime as rt
import anvil.config as cfg
import anvil.core.utils as ut


class Transform(dag_node.DagNode):
    dcc_type = 'transform'

    @staticmethod
    def create_engine_instance(**flags):
        return rt.dcc.create.create_transform(**flags)

    def get_parent(self):
        parents = rt.dcc.scene.list_relatives(self.name(), parent=True)
        try:
            return parents[0]
        except IndexError:
            return parents

    def parent(self, new_parent):
        self.LOG.debug('Parenting %s to %s' % (self, new_parent))
        top_node, new_parent = self, new_parent
        nodes_exist = [rt.dcc.scene.exists(node) for node in [top_node, new_parent] if node != None]
        if all(nodes_exist or [False]):
            rt.dcc.scene.parent(top_node, new_parent)
            return True
        elif new_parent is None:
            rt.dcc.scene.parent(top_node, world=True)
        else:
            raise KeyError('Node %s or %s does not exist.' % (self, new_parent))

    @classmethod
    def build(cls, reference_object=None, meta_data=None, parent=None, **kwargs):
        node = super(Transform, cls).build(meta_data=meta_data, **kwargs)
        node.parent(parent)
        node.match_position(reference_object)
        return node

    def match(self, reference_objects, mode=cfg.TRANSLATE, keep_constraint=False, **kwargs):
        if mode == cfg.TRANSLATE:
            return self.match_position(reference_objects, keep_constraint=keep_constraint, **kwargs)
        elif mode == cfg.ROTATE:
            return self.match_rotation(reference_objects, keep_constraint=keep_constraint, **kwargs)
        elif mode == cfg.AIM:
            return self.aim_at(reference_objects, keep_constraint=keep_constraint, **kwargs)
        elif mode == cfg.TRANSFORM:
            return self.match_transform(reference_objects, keep_constraint=keep_constraint, **kwargs)
        else:
            raise ValueError('%s.match - mode %s not supported.' % self.__class__.__name__)

    def aim_at(self, reference_objects, up_vector=None, aim_vector=None, up_object=None, keep_constraint=False,
               **kwargs):
        reference_objects = ut.validate_and_cast_to_str_list(reference_objects)
        self.LOG.info('Aiming %s at %s' % (self, reference_objects))
        if reference_objects:
            kwargs.update(
                {k: v for k, v in [['upObject', up_object], ['upVector', up_vector], ['aimVector', aim_vector]] if v})

            constraint = rt.dcc.connections.aim(reference_objects, self, maintainOffset=False, **kwargs)
            if not keep_constraint:
                rt.dcc.scene.delete(constraint)
                constraint = None
            return constraint

    def match_rotation(self, reference_objects, keep_constraint=False, **kwargs):
        reference_objects = ut.validate_and_cast_to_str_list(reference_objects)
        self.LOG.info('Matching position of %s to %s' % (self, reference_objects))
        if reference_objects:
            constraint = rt.dcc.connections.rotate(reference_objects, self, maintainOffset=False, **kwargs)
            if not keep_constraint:
                rt.dcc.scene.delete(constraint)
                constraint = None
            return constraint

    def match_position(self, reference_objects, keep_constraint=False, **kwargs):
        reference_objects = ut.validate_and_cast_to_str_list(reference_objects)
        self.LOG.info('Matching position of %s to %s' % (self, reference_objects))
        if reference_objects:
            constraint = rt.dcc.connections.translate(reference_objects, self, maintainOffset=False, **kwargs)
            if not keep_constraint:
                rt.dcc.scene.delete(constraint)
                constraint = None
            return constraint

    def match_transform(self, reference_objects, keep_constraint=False, **kwargs):
        reference_objects = ut.validate_and_cast_to_str_list(reference_objects)
        self.LOG.info('Matching position of %s to %s' % (self, reference_objects))
        if reference_objects:
            constraint = rt.dcc.connections.parent(reference_objects, self, maintainOffset=False, **kwargs)
            if not keep_constraint:
                rt.dcc.scene.delete(constraint)
                constraint = None
            return constraint

    def move(self, value, mode=cfg.TRANSLATE, **kwargs):
        if mode in [cfg.SCALE, cfg.SCALE[0], cfg.SCALE[0].upper()]:
            self.scale_node(value, **kwargs)

        elif mode in [cfg.TRANSLATE, cfg.TRANSFORMATION, cfg.TRANSFORM, cfg.TRANSLATE[0], cfg.TRANSLATE[0].upper()]:
            self.translate_node(value, **kwargs)

        elif mode in [cfg.ROTATE, cfg.ROTATION, cfg.ROTATE[0], cfg.ROTATE[0].upper()]:
            self.rotate_node(value, **kwargs)

    def scale_node(self, value, **kwargs):
        rt.dcc.scene.position(self, scale=value, **kwargs)

    def translate_node(self, value, **kwargs):
        rt.dcc.scene.position(self, translation=value, **kwargs)

    def rotate_node(self, value, **kwargs):
        rt.dcc.scene.position(self, rotation=value, **kwargs)
