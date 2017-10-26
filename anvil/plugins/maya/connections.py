import anvil.plugins.base.connections as connections
from anvil.plugins.maya.dependencies import *
from jsonschema import validate

m_api = pm


class Attribute(connections.Attribute):
    def get(self, object, attr, **flags):
        return m_api.getAttr(object, attr)

    def set(self, object, attr, value, **flags):
        return m_api.setAttr(object, attr, value, **flags)


class Constraint(connections.Constraint):
    default_schema = {
        "type": ["object", "null"],
        "properties": {
            "layer": {"type": "string"},
            "name": {"type": "string"},
            "remove": {"type": "boolean"},
            "targetList": {"type": "boolean"},
            "weight": {"type": "number"},
            "weightAliasList": {"type": "boolean"},
        },
    }
    cacheable_schema = {
        "createCache": {"type": "array", "items": {"type": "number"}, "minItems": 2, "maxItems": 2},
        "deleteCache": {"type": "boolean"},
    }

    offset_schema = {
        "maintainOffset": {"type": "boolean"},
        "offset": {"type": "array", "items": {"type": "number"}, "minItems": 3, "maxItems": 3},
        "skip": {"type": "string"},
    }

    aim_schema = {
        "aimVector": {"type": "array", "items": {"type": "number"}, "minItems": 3, "maxItems": 3},
        "upVector": {"type": "array", "items": {"type": "number"}, "minItems": 3, "maxItems": 3},
        "worldUpObject": {"type": "string"},
        "worldUpType": {"type": "string"},
        "worldUpVector": {"type": "array", "items": {"type": "number"}, "minItems": 3, "maxItems": 3},
    }

    def translate(self, source, targets, **flags):
        schema = {}
        schema.update(self.default_schema)
        schema.update(self.offset_schema)
        validate(flags, schema)
        flags = self._initialize_and_filter_flags(flags, schema)
        return m_api.pointConstraint(targets, source, **flags)

    def rotate(self, source, targets, **flags):
        schema = {}
        schema.update(self.default_schema)
        schema.update(self.offset_schema)
        schema.update(self.cacheable_schema)
        validate(flags, schema)
        flags = self._initialize_and_filter_flags(flags, schema)
        return m_api.orientConstraint(targets, source, **flags)

    def aim(self, source, targets, **flags):
        schema = {}
        schema.update(self.default_schema)
        schema.update(self.offset_schema)
        schema.update(self.aim_schema)
        validate(flags, schema)
        flags = self._initialize_and_filter_flags(flags, schema)
        return m_api.aimConstraint(targets, source, **flags)

    def scale(self, source, targets, **flags):
        schema = {
            "properties": {
                "scaleCompensate": {"type": "boolean"},
                "targetList": {"type": "boolean"},
            },
        }
        schema.update(self.default_schema)
        schema.update(self.offset_schema)
        validate(flags, schema)
        flags = self._initialize_and_filter_flags(flags, schema)
        return m_api.scaleConstraint(targets, source, **flags)

    def parent(self, source, targets, **flags):
        schema = {
            "properties": {
                "decompRotationToChild": {"type": "boolean"},
                "skipRotate": {"type": "string"},
                "skipTranslate": {"type": "string"},
            },
        }
        schema.update(self.default_schema)
        schema.update(self.offset_schema)
        schema.update(self.cacheable_schema)
        if schema['properties'].get('skip'):
            schema['properties'].pop('skip')
        validate(flags, schema)
        flags = self._initialize_and_filter_flags(flags, schema)
        return m_api.parentConstraint(targets, source, **flags)

    def tangent(self, source, targets, **flags):
        schema = {}
        schema.update(self.default_schema)
        schema.update(self.aim_schema)
        validate(flags, schema)
        flags = self._initialize_and_filter_flags(flags, schema)
        return m_api.tangentConstraint(targets, source, **flags)

    def geometry_point(self, source, targets, **flags):
        schema = {}
        schema.update(self.default_schema)
        validate(flags, schema)
        flags = self._initialize_and_filter_flags(flags, schema)
        return m_api.geometryConstraint(targets, source, **flags)

    def geometry_normal(self, source, targets, **flags):
        schema = {}
        schema.update(self.default_schema)
        schema.update(self.aim_schema)
        validate(flags, schema)
        flags = self._initialize_and_filter_flags(flags, schema)
        return m_api.normalConstraint(targets, source, **flags)

    def pole_vector(self, source, targets, **flags):
        schema = {}
        schema.update(self.default_schema)
        validate(flags, schema)
        flags = self._initialize_and_filter_flags(flags, schema)
        return m_api.poleVectorConstraint(targets, source, **flags)
