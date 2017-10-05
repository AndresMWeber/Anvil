"""Kraken Maya - Maya Builder module.
Classes:
Builder -- Component representation.
"""

import json
import logging

from kraken.log import getLogger

from kraken.core.kraken_system import ks
from kraken.core.configs.config import Config

from kraken.core.maths import Vec2, Vec3, Xfo, Mat44, Math_radToDeg, RotationOrder

from kraken.core.builder import Builder
from kraken.core.objects.object_3d import Object3D
from kraken.core.objects.attributes.attribute import Attribute
from kraken.plugins.maya_plugin.utils import *

from kraken.helpers.utility_methods import prepareToSave, prepareToLoad

import maya.cmds as cmds

logger = getLogger('kraken')
logger.setLevel(logging.INFO)

# Rotation order remapping
# Maya's enums don't map directly to the Fabric rotation orders
#
# Fabric | Maya
# ---------------
# 0 ZYX  | 5 ZYX
# 1 XZY  | 3 XZY
# 2 YXZ  | 4 YXZ
# 3 YZX  | 1 YZX
# 4 XYZ  | 0 XYZ
# 5 ZXY  | 2 ZXY

ROT_ORDER_REMAP = {
    0: 5,
    1: 3,
    2: 4,
    3: 1,
    4: 0,
    5: 2
}

MAYA_2015_COLORS = {
    "black": [1, [0.00, 0.00, 0.0]],
    "lightGrey": [2, [0.75, 0.75, 0.75]],
    "darkGrey": [3, [0.50, 0.50, 0.50]],
    "fusia": [4, [0.80, 0.00, 0.20]],
    "blueDark": [5, [0.00, 0.00, 0.40]],
    "blue": [6, [0.00, 0.00, 1.00]],
    "green": [7, [0.00, 0.30, 0.00]],
    "purpleDark": [8, [0.20, 0.00, 0.30]],
    "magenta": [9, [0.80, 0.00, 0.80]],
    "brownLight": [10, [0.60, 0.30, 0.20]],
    "brownDark": [11, [0.25, 0.13, 0.13]],
    "orange": [12, [0.70, 0.20, 0.00]],
    "red": [13, [1.00, 0.00, 0.00]],
    "greenBright": [14, [0.00, 1.00, 0.00]],
    "blueMedium": [15, [0.00, 0.30, 0.60]],
    "white": [16, [1.00, 1.00, 1.00]],
    "yellow": [17, [1.00, 1.00, 0.00]],
    "greenBlue": [18, [0.00, 1.00, 1.00]],
    "turqoise": [19, [0.00, 1.00, 0.80]],
    "pink": [20, [1.00, 0.70, 0.70]],
    "peach": [21, [0.90, 0.70, 0.50]],
    "yellowLight": [22, [1.00, 1.00, 0.40]],
    "turqoiseDark": [23, [0.00, 0.70, 0.40]],
    "brownMuted": [24, [0.60, 0.40, 0.20]],
    "yellowMuted": [25, [0.63, 0.63, 0.17]],
    "greenMuted": [26, [0.40, 0.60, 0.20]],
    "turqoiseMuted": [27, [0.20, 0.63, 0.35]],
    "blueLightMuted": [28, [0.18, 0.63, 0.63]],
    "blueDarkMuted": [29, [0.18, 0.40, 0.63]],
    "purpleLight": [30, [0.43, 0.18, 0.63]]
}


class Builder(Builder):
    """Builder object for building Kraken objects in Maya."""

    def __init__(self):
        super(Builder, self).__init__()

    def deleteBuildElements(self):
        """Clear out all dcc built elements from the scene if exist."""

        for builtElement in self._buildElements:
            if builtElement['src'].isTypeOf('Attribute'):
                continue

            node = builtElement['tgt']
            if node.exists():
                pm.delete(node)

        self._buildElements = []

        return

    # ========================
    # Object3D Build Methods
    # ========================
    def buildContainer(self, kSceneItem, buildName):
        """Builds a container / namespace object.
        Args:
            kSceneItem (Object): kSceneItem that represents a container to
                be built.
            buildName (str): The name to use on the built object.
        Returns:
            object: Node that is created.
        """

        parentNode = self.getDCCSceneItem(kSceneItem.getParent())

        dccSceneItem = pm.group(name="group", em=True)
        pm.parent(dccSceneItem, parentNode)
        pm.rename(dccSceneItem, buildName)

        if kSceneItem.isTypeOf('Rig'):
            krakenRigAttr = dccSceneItem.addAttr('krakenRig',
                                                 niceName='krakenRig',
                                                 attributeType="bool",
                                                 defaultValue=True,
                                                 keyable=False)

            dccSceneItem.attr('krakenRig').setLocked(True)

            # Put Rig Data on DCC Item
            metaData = kSceneItem.getMetaData()
            if 'guideData' in metaData:
                pureJSON = metaData['guideData']

                krakenRigDataAttr = dccSceneItem.addAttr('krakenRigData',
                                                         niceName='krakenRigData',
                                                         dataType="string",
                                                         keyable=False)

                dccSceneItem.attr('krakenRigData').set(json.dumps(pureJSON, indent=2))
                dccSceneItem.attr('krakenRigData').setLocked(True)

        self._registerSceneItemPair(kSceneItem, dccSceneItem)

        return dccSceneItem

    def buildLayer(self, kSceneItem, buildName):
        """Builds a layer object.
        Args:
            kSceneItem (Object): kSceneItem that represents a layer to
                be built.
            buildName (str): The name to use on the built object.
        Returns:
            object: Node that is created.
        """

        parentNode = self.getDCCSceneItem(kSceneItem.getParent())

        dccSceneItem = pm.group(name="group", em=True)
        pm.parent(dccSceneItem, parentNode)
        pm.rename(dccSceneItem, buildName)

        self._registerSceneItemPair(kSceneItem, dccSceneItem)

        return dccSceneItem

    def buildHierarchyGroup(self, kSceneItem, buildName):
        """Builds a hierarchy group object.
        Args:
            kSceneItem (Object): kSceneItem that represents a group to
                be built.
            buildName (str): The name to use on the built object.
        Return:
            object: DCC Scene Item that is created.
        """

        parentNode = self.getDCCSceneItem(kSceneItem.getParent())

        dccSceneItem = pm.group(name="group", em=True)
        pm.parent(dccSceneItem, parentNode)
        pm.rename(dccSceneItem, buildName)

        self._registerSceneItemPair(kSceneItem, dccSceneItem)

        return dccSceneItem

    def buildGroup(self, kSceneItem, buildName):
        """Builds a group object.
        Args:
            kSceneItem (Object): kSceneItem that represents a group to
                be built.
            buildName (str): The name to use on the built object.
        Returns:
            object: Node that is created.
        """

        parentNode = self.getDCCSceneItem(kSceneItem.getParent())

        dccSceneItem = pm.group(name="group", em=True)
        pm.parent(dccSceneItem, parentNode)
        pm.rename(dccSceneItem, buildName)

        self._registerSceneItemPair(kSceneItem, dccSceneItem)

        return dccSceneItem

    def buildJoint(self, kSceneItem, buildName):
        """Builds a joint object.
        Args:
            kSceneItem (Object): kSceneItem that represents a joint to
                be built.
            buildName (str): The name to use on the built object.
        Return:
            object: DCC Scene Item that is created.
        """

        parentNode = self.getDCCSceneItem(kSceneItem.getParent())

        pm.select(parentNode)
        dccSceneItem = pm.joint(name="joint")
        pm.rename(dccSceneItem, buildName)

        radius = dccSceneItem.attr('radius').set(kSceneItem.getRadius())

        self._registerSceneItemPair(kSceneItem, dccSceneItem)

        return dccSceneItem

    def buildLocator(self, kSceneItem, buildName):
        """Builds a locator / null object.
        Args:
            kSceneItem (Object): locator / null object to be built.
            buildName (str): The name to use on the built object.
        Returns:
            object: Node that is created.
        """

        parentNode = self.getDCCSceneItem(kSceneItem.getParent())

        dccSceneItem = pm.spaceLocator(name="locator")
        pm.parent(dccSceneItem, parentNode)
        pm.rename(dccSceneItem, buildName)

        self._registerSceneItemPair(kSceneItem, dccSceneItem)

        return dccSceneItem

    def buildCurve(self, kSceneItem, buildName):
        """Builds a Curve object.
        Args:
            kSceneItem (Object): kSceneItem that represents a curve to
                be built.
            buildName (str): The name to use on the built object.
        Returns:
            object: Node that is created.
        """

        parentNode = self.getDCCSceneItem(kSceneItem.getParent())

        # Format points for Maya
        curveData = kSceneItem.getCurveData()

        # Scale, rotate, translation shape
        curvePoints = []
        for eachSubCurve in curveData:
            formattedPoints = eachSubCurve["points"]
            curvePoints.append(formattedPoints)

        mainCurve = None
        for i, eachSubCurve in enumerate(curvePoints):
            closedSubCurve = curveData[i]["closed"]
            degreeSubCurve = curveData[i]["degree"]

            currentSubCurve = pm.curve(per=False,
                                       point=curvePoints[i],
                                       degree=degreeSubCurve)

            if closedSubCurve:
                pm.closeCurve(currentSubCurve,
                              preserveShape=True,
                              replaceOriginal=True)

            if mainCurve is None:
                mainCurve = currentSubCurve

            if i > 0:
                pm.parent(currentSubCurve.getShape(),
                          mainCurve,
                          relative=True,
                          shape=True)

                pm.delete(currentSubCurve)

        dccSceneItem = mainCurve
        pm.parent(dccSceneItem, parentNode)
        pm.rename(dccSceneItem, buildName)

        self._registerSceneItemPair(kSceneItem, dccSceneItem)

        return dccSceneItem

    def buildControl(self, kSceneItem, buildName):
        """Builds a Control object.
        Args:
            kSceneItem (Object): kSceneItem that represents a control to
                be built.
            buildName (str): The name to use on the built object.
        Returns:
            object: Node that is created.
        """

        parentNode = self.getDCCSceneItem(kSceneItem.getParent())

        # Format points for Maya
        curveData = kSceneItem.getCurveData()

        # Scale, rotate, translation shape
        curvePoints = []
        for eachSubCurve in curveData:
            formattedPoints = eachSubCurve["points"]
            curvePoints.append(formattedPoints)

        mainCurve = None
        for i, eachSubCurve in enumerate(curvePoints):
            closedSubCurve = curveData[i]["closed"]
            degreeSubCurve = curveData[i]["degree"]

            currentSubCurve = pm.curve(per=False,
                                       point=curvePoints[i],
                                       degree=degreeSubCurve)

            if closedSubCurve:
                pm.closeCurve(currentSubCurve,
                              preserveShape=True,
                              replaceOriginal=True)

            if mainCurve is None:
                mainCurve = currentSubCurve

            if i > 0:
                pm.parent(currentSubCurve.getShape(),
                          mainCurve,
                          relative=True,
                          shape=True)

                pm.delete(currentSubCurve)

        dccSceneItem = mainCurve
        pm.parent(dccSceneItem, parentNode)
        pm.rename(dccSceneItem, buildName)

        self._registerSceneItemPair(kSceneItem, dccSceneItem)

        return dccSceneItem

    # ========================
    # Attribute Build Methods
    # ========================
    def buildBoolAttribute(self, kAttribute):
        """Builds a Bool attribute.
        Args:
            kAttribute (Object): kAttribute that represents a boolean
                attribute to be built.
        Return:
            bool: True if successful.
        """

        if kAttribute.getParent().getName() == 'implicitAttrGrp':
            return False

        parentDCCSceneItem = self.getDCCSceneItem(kAttribute.getParent().getParent())
        parentDCCSceneItem.addAttr(kAttribute.getName(),
                                   niceName=kAttribute.getName(),
                                   attributeType="bool",
                                   defaultValue=kAttribute.getValue(),
                                   keyable=True)

        dccSceneItem = parentDCCSceneItem.attr(kAttribute.getName())
        self._registerSceneItemPair(kAttribute, dccSceneItem)

        return True

    def buildScalarAttribute(self, kAttribute):
        """Builds a Float attribute.
        Args:
            kAttribute (Object): kAttribute that represents a float attribute
                to be built.
        Return:
            bool: True if successful.
        """

        if kAttribute.getParent().getName() == 'implicitAttrGrp':
            return False

        parentDCCSceneItem = self.getDCCSceneItem(kAttribute.getParent().getParent())
        parentDCCSceneItem.addAttr(kAttribute.getName(),
                                   niceName=kAttribute.getName(),
                                   attributeType="float",
                                   defaultValue=kAttribute.getValue(),
                                   keyable=True)

        dccSceneItem = parentDCCSceneItem.attr(kAttribute.getName())

        if kAttribute.getMin() is not None:
            dccSceneItem.setMin(kAttribute.getMin())

        if kAttribute.getMax() is not None:
            dccSceneItem.setMax(kAttribute.getMax())

        if kAttribute.getUIMin() is not None:
            dccSceneItem.setSoftMin(kAttribute.getUIMin())

        if kAttribute.getUIMax() is not None:
            dccSceneItem.setSoftMax(kAttribute.getUIMax())

        self._registerSceneItemPair(kAttribute, dccSceneItem)

        return True

    def buildIntegerAttribute(self, kAttribute):
        """Builds a Integer attribute.
        Args:
            kAttribute (Object): kAttribute that represents a integer attribute to be built.
        Return:
            bool: True if successful.
        """

        if kAttribute.getParent().getName() == 'implicitAttrGrp':
            return False

        mininum = kAttribute.getMin()
        if mininum == None:
            mininum = 0

        maximum = kAttribute.getMax()
        if maximum == None:
            maximum = kAttribute.getValue() * 2

        parentDCCSceneItem = self.getDCCSceneItem(kAttribute.getParent().getParent())
        parentDCCSceneItem.addAttr(kAttribute.getName(), niceName=kAttribute.getName(), attributeType="long",
                                   defaultValue=kAttribute.getValue(), minValue=mininum, maxValue=maximum, keyable=True)
        parentDCCSceneItem.attr(kAttribute.getName())
        dccSceneItem = parentDCCSceneItem.attr(kAttribute.getName())

        if kAttribute.getMin() is not None:
            dccSceneItem.setMin(kAttribute.getMin())

        if kAttribute.getMax() is not None:
            dccSceneItem.setMax(kAttribute.getMax())

        if kAttribute.getUIMin() is not None:
            dccSceneItem.setSoftMin(kAttribute.getUIMin())

        if kAttribute.getUIMax() is not None:
            dccSceneItem.setSoftMax(kAttribute.getUIMax())

        self._registerSceneItemPair(kAttribute, dccSceneItem)

        return True

    def buildStringAttribute(self, kAttribute):
        """Builds a String attribute.
        Args:
            kAttribute (Object): kAttribute that represents a string attribute
                to be built.
        Return:
            bool: True if successful.
        """

        if kAttribute.getParent().getName() == 'implicitAttrGrp':
            return False

        parentDCCSceneItem = self.getDCCSceneItem(kAttribute.getParent().getParent())
        parentDCCSceneItem.addAttr(kAttribute.getName(),
                                   niceName=kAttribute.getName(),
                                   dataType="string")

        dccSceneItem = parentDCCSceneItem.attr(kAttribute.getName())
        dccSceneItem.set(kAttribute.getValue())
        self._registerSceneItemPair(kAttribute, dccSceneItem)

        return True

    def buildAttributeGroup(self, kAttributeGroup):
        """Builds attribute groups on the DCC object.
        Args:
            kAttributeGroup (object): Kraken object to build the attribute
                group on.
        Return:
            bool: True if successful.
        """

        parentDCCSceneItem = self.getDCCSceneItem(kAttributeGroup.getParent())

        groupName = kAttributeGroup.getName()
        if groupName == "implicitAttrGrp":
            return False

        parentDCCSceneItem.addAttr(groupName,
                                   niceName=groupName,
                                   attributeType="enum",
                                   enumName="-----",
                                   keyable=True)

        dccSceneItem = parentDCCSceneItem.attr(groupName)
        pm.setAttr(parentDCCSceneItem + "." + groupName, lock=True)

        self._registerSceneItemPair(kAttributeGroup, dccSceneItem)

        return True

    def connectAttribute(self, kAttribute):
        """Connects the driver attribute to this one.
        Args:
            kAttribute (Object): Attribute to connect.
        Return:
            bool: True if successful.
        """

        if kAttribute.isConnected() is True:

            # Detect if driver is visibility attribute and map to correct DCC
            # attribute
            driverAttr = kAttribute.getConnection()
            if driverAttr.getName() == 'visibility' and driverAttr.getParent().getName() == 'implicitAttrGrp':
                dccItem = self.getDCCSceneItem(driverAttr.getParent().getParent())
                driver = dccItem.attr('visibility')

            elif driverAttr.getName() == 'shapeVisibility' and driverAttr.getParent().getName() == 'implicitAttrGrp':
                dccItem = self.getDCCSceneItem(driverAttr.getParent().getParent())
                shape = dccItem.getShape()
                driver = shape.attr('visibility')

            else:
                driver = self.getDCCSceneItem(kAttribute.getConnection())

            # Detect if the driven attribute is a visibility attribute and map
            # to correct DCC attribute
            if kAttribute.getName() == 'visibility' and kAttribute.getParent().getName() == 'implicitAttrGrp':
                dccItem = self.getDCCSceneItem(kAttribute.getParent().getParent())
                driven = dccItem.attr('visibility')

            elif kAttribute.getName() == 'shapeVisibility' and kAttribute.getParent().getName() == 'implicitAttrGrp':
                dccItem = self.getDCCSceneItem(kAttribute.getParent().getParent())
                shape = dccItem.getShape()
                driven = shape.attr('visibility')
            else:
                driven = self.getDCCSceneItem(kAttribute)

            pm.connectAttr(driver, driven, force=True)

        return True

    # =========================
    # Constraint Build Methods
    # =========================
    def buildOrientationConstraint(self, kConstraint, buildName):
        """Builds an orientation constraint represented by the kConstraint.
        Args:
            kConstraint (Object): Kraken constraint object to build.
        Return:
            object: dccSceneItem that was created.
        """

        dccSceneItem = None
        constraineeDCCSceneItem = self.getDCCSceneItem(kConstraint.getConstrainee())

        if self.getConfig().getMetaData('UseMayaNativeConstraints', False):

            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'tx', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'ty', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'tz', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'rx', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'ry', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'rz', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'sx', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'sy', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'sz', lock=False)

            dccSceneItem = pm.orientConstraint(
                [self.getDCCSceneItem(x) for x in kConstraint.getConstrainers()],
                constraineeDCCSceneItem,
                name=kConstraint.getName() + "_ori_cns",
                maintainOffset=kConstraint.getMaintainOffset())

            if kConstraint.getMaintainOffset() is True:
                order = ROT_ORDER_REMAP[kConstraint.getConstrainee().ro.order]

                offsetXfo = kConstraint.computeOffset()
                offsetAngles = offsetXfo.ori.toEulerAnglesWithRotOrder(
                    RotationOrder(order))

                dccSceneItem.attr('offset').set([offsetAngles.x,
                                                 offsetAngles.y,
                                                 offsetAngles.z])

            pm.rename(dccSceneItem, buildName)

        else:

            constrainerDCCSceneItem = self.getDCCSceneItem(kConstraint.getConstrainers()[0])
            dccSceneItem = pm.PyNode(pm.createNode('fabricConstraint'))
            pm.connectAttr('%s.worldMatrix' % constrainerDCCSceneItem, '%s.input' % dccSceneItem)
            pm.connectAttr('%s.rotate' % dccSceneItem, '%s.rotate' % constraineeDCCSceneItem)
            pm.setAttr('%s.rotateOrder' % dccSceneItem, pm.getAttr('%s.rotateOrder' % constraineeDCCSceneItem))

            if kConstraint.getConstrainee().isTypeOf('Joint'):
                parentDCCSceneItem = self.getDCCSceneItem(kConstraint.getConstrainee().getParent())
                pm.connectAttr("%s.worldMatrix" % parentDCCSceneItem, "%s.parent" % dccSceneItem)
            else:
                pm.setAttr("%s.inheritsTransform" % constraineeDCCSceneItem, 0)

            if kConstraint.getMaintainOffset() is True:
                offsetXfo = kConstraint.computeOffset()
                self.setMat44Attr('%s' % dccSceneItem, 'offset', offsetXfo.toMat44())

            pm.rename(dccSceneItem, buildName)

        self._registerSceneItemPair(kConstraint, dccSceneItem)

        return dccSceneItem

    def buildPoseConstraint(self, kConstraint, buildName):
        """Builds an pose constraint represented by the kConstraint.
        Args:
            kConstraint (Object): kraken constraint object to build.
        Return:
            bool: True if successful.
        """

        dccSceneItem = None
        constraineeDCCSceneItem = self.getDCCSceneItem(kConstraint.getConstrainee())

        if self.getConfig().getMetaData('UseMayaNativeConstraints', False):

            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'tx', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'ty', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'tz', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'rx', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'ry', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'rz', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'sx', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'sy', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'sz', lock=False)

            dccSceneItem = pm.parentConstraint(
                [self.getDCCSceneItem(x) for x in kConstraint.getConstrainers()],
                constraineeDCCSceneItem,
                name=buildName,
                maintainOffset=kConstraint.getMaintainOffset())

            # We need this block of code to replace the pose constraint name with
            # the scale constraint name since we don't have a single pos, rot, scl,
            # constraint in Maya.
            config = Config.getInstance()
            nameTemplate = config.getNameTemplate()
            poseCnsName = nameTemplate['types']['PoseConstraint']
            sclCnsName = nameTemplate['types']['ScaleConstraint']

            scaleConstraint = pm.scaleConstraint(
                [self.getDCCSceneItem(x) for x in kConstraint.getConstrainers()],
                constraineeDCCSceneItem,
                name=buildName.replace(poseCnsName, sclCnsName),
                maintainOffset=kConstraint.getMaintainOffset())

            if kConstraint.getMaintainOffset() is True:
                order = ROT_ORDER_REMAP[kConstraint.getConstrainee().ro.order]

                offsetXfo = kConstraint.computeOffset()
                offsetAngles = offsetXfo.ori.toEulerAnglesWithRotOrder(
                    RotationOrder(order))

                # Set offsets on parent constraint
                dccSceneItem.target[0].targetOffsetTranslate.set([offsetXfo.tr.x,
                                                                  offsetXfo.tr.y,
                                                                  offsetXfo.tr.z])

                dccSceneItem.target[0].targetOffsetRotate.set(
                    [Math_radToDeg(offsetAngles.x),
                     Math_radToDeg(offsetAngles.y),
                     Math_radToDeg(offsetAngles.z)])

                # Set offsets on the scale constraint
                scaleConstraint.offset.set([offsetXfo.sc.x,
                                            offsetXfo.sc.y,
                                            offsetXfo.sc.z])

        else:

            constrainerDCCSceneItem = self.getDCCSceneItem(kConstraint.getConstrainers()[0])
            dccSceneItem = pm.PyNode(pm.createNode('fabricConstraint'))
            pm.connectAttr('%s.worldMatrix' % constrainerDCCSceneItem, '%s.input' % dccSceneItem)
            pm.connectAttr('%s.translate' % dccSceneItem, '%s.translate' % constraineeDCCSceneItem)
            pm.connectAttr('%s.rotate' % dccSceneItem, '%s.rotate' % constraineeDCCSceneItem)
            pm.connectAttr('%s.scale' % dccSceneItem, '%s.scale' % constraineeDCCSceneItem)
            pm.setAttr('%s.rotateOrder' % dccSceneItem, pm.getAttr('%s.rotateOrder' % constraineeDCCSceneItem))
            if kConstraint.getConstrainee().isTypeOf('Joint'):
                parentDCCSceneItem = self.getDCCSceneItem(kConstraint.getConstrainee().getParent())
                pm.connectAttr("%s.worldMatrix" % parentDCCSceneItem, "%s.parent" % dccSceneItem)
            else:
                pm.setAttr("%s.inheritsTransform" % constraineeDCCSceneItem, 0)

            if kConstraint.getMaintainOffset() is True:
                offsetXfo = kConstraint.computeOffset()
                self.setMat44Attr('%s' % dccSceneItem, 'offset', offsetXfo.toMat44())

            pm.rename(dccSceneItem, buildName)

        self._registerSceneItemPair(kConstraint, dccSceneItem)

        return dccSceneItem

    def buildPositionConstraint(self, kConstraint, buildName):
        """Builds an position constraint represented by the kConstraint.
        Args:
            kConstraint (Object): Kraken constraint object to build.
        Return:
            bool: True if successful.
        """

        dccSceneItem = None
        constraineeDCCSceneItem = self.getDCCSceneItem(kConstraint.getConstrainee())

        if self.getConfig().getMetaData('UseMayaNativeConstraints', False):

            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'tx', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'ty', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'tz', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'rx', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'ry', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'rz', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'sx', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'sy', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'sz', lock=False)

            dccSceneItem = pm.pointConstraint(
                [self.getDCCSceneItem(x) for x in kConstraint.getConstrainers()],
                constraineeDCCSceneItem,
                name=buildName,
                maintainOffset=kConstraint.getMaintainOffset())

            if kConstraint.getMaintainOffset() is True:
                offsetXfo = kConstraint.computeOffset()

                # Set offsets on the scale constraint
                dccSceneItem.offset.set([offsetXfo.tr.x,
                                         offsetXfo.tr.y,
                                         offsetXfo.tr.z])

        else:

            constrainerDCCSceneItem = self.getDCCSceneItem(kConstraint.getConstrainers()[0])
            dccSceneItem = pm.PyNode(pm.createNode('fabricConstraint'))
            pm.connectAttr('%s.worldMatrix' % constrainerDCCSceneItem, '%s.input' % dccSceneItem)
            pm.connectAttr('%s.translate' % dccSceneItem, '%s.translate' % constraineeDCCSceneItem)
            pm.setAttr('%s.rotateOrder' % dccSceneItem, pm.getAttr('%s.rotateOrder' % constraineeDCCSceneItem))
            if kConstraint.getConstrainee().isTypeOf('Joint'):
                parentDCCSceneItem = self.getDCCSceneItem(kConstraint.getConstrainee().getParent())
                pm.connectAttr("%s.worldMatrix" % parentDCCSceneItem, "%s.parent" % dccSceneItem)
            else:
                pm.setAttr("%s.inheritsTransform" % constraineeDCCSceneItem, 0)

            if kConstraint.getMaintainOffset() is True:
                offsetXfo = kConstraint.computeOffset()
                self.setMat44Attr('%s' % dccSceneItem, 'offset', offsetXfo.toMat44())

            pm.rename(dccSceneItem, buildName)

        self._registerSceneItemPair(kConstraint, dccSceneItem)

        return dccSceneItem

    def buildScaleConstraint(self, kConstraint, buildName):
        """Builds an scale constraint represented by the kConstraint.
        Args:
            kConstraint (Object): Kraken constraint object to build.
        Return:
            bool: True if successful.
        """

        dccSceneItem = None
        constraineeDCCSceneItem = self.getDCCSceneItem(kConstraint.getConstrainee())

        if self.getConfig().getMetaData('UseMayaNativeConstraints', False):

            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'tx', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'ty', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'tz', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'rx', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'ry', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'rz', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'sx', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'sy', lock=False)
            pm.setAttr(constraineeDCCSceneItem.longName() + "." + 'sz', lock=False)

            dccSceneItem = pm.scaleConstraint(
                [self.getDCCSceneItem(x) for x in kConstraint.getConstrainers()],
                constraineeDCCSceneItem,
                name=buildName,
                maintainOffset=kConstraint.getMaintainOffset())

            if kConstraint.getMaintainOffset() is True:
                offsetXfo = kConstraint.computeOffset()

                # Set offsets on the scale constraint
                dccSceneItem.offset.set([offsetXfo.sc.x,
                                         offsetXfo.sc.y,
                                         offsetXfo.sc.z])

        else:

            constrainerDCCSceneItem = self.getDCCSceneItem(kConstraint.getConstrainers()[0])
            dccSceneItem = pm.PyNode(pm.createNode('fabricConstraint'))
            pm.connectAttr('%s.worldMatrix' % constrainerDCCSceneItem, '%s.input' % dccSceneItem)
            pm.connectAttr('%s.scale' % dccSceneItem, '%s.scale' % constraineeDCCSceneItem)
            pm.setAttr('%s.rotateOrder' % dccSceneItem, pm.getAttr('%s.rotateOrder' % constraineeDCCSceneItem))
            if kConstraint.getConstrainee().isTypeOf('Joint'):
                parentDCCSceneItem = self.getDCCSceneItem(kConstraint.getConstrainee().getParent())
                pm.connectAttr("%s.worldMatrix" % parentDCCSceneItem, "%s.parent" % dccSceneItem)
            else:
                pm.setAttr("%s.inheritsTransform" % constraineeDCCSceneItem, 0)

            if kConstraint.getMaintainOffset() is True:
                offsetXfo = kConstraint.computeOffset()
                self.setMat44Attr('%s' % dccSceneItem, 'offset', offsetXfo.toMat44())

            pm.rename(dccSceneItem, buildName)

        self._registerSceneItemPair(kConstraint, dccSceneItem)

        return dccSceneItem

    # =========================
    # Operator Builder Methods
    # =========================
    def buildKLOperator(self, kOperator, buildName):
        """Builds KL Operators on the components.
        Args:
            kOperator (Object): Kraken operator that represents a KL
                operator.
            buildName (str): The name to use on the built object.
        Return:
            bool: True if successful.
        """

        # Code to build KL and Canvas based Operators has been merged.
        # It's important to note here that the 'isKLBased' argument is set
        # to true.
        self.buildCanvasOperator(kOperator, buildName, isKLBased=True)

        return True

    def buildCanvasOperator(self, kOperator, buildName, isKLBased=False):
        """Builds Canvas Operators on the components.
        Args:
            kOperator (object): Kraken operator that represents a Canvas
                operator.
            buildName (str): The name to use on the built object.
            isKLBased (bool): Whether the solver is based on a KL object.
        Return:
            bool: True if successful.
        """

        def validatePortValue(rtVal, portName, portDataType):
            """Validate port value type when passing built in Python types.
            Args:
                rtVal (RTVal): rtValue object.
                portName (str): Name of the argument being validated.
                portDataType (str): Type of the argument being validated.
            """

            # Validate types when passing a built in Python type
            if type(rtVal) in (bool, str, int, float):
                if portDataType in ('Scalar', 'Float32', 'UInt32'):
                    if type(rtVal) not in (float, int):
                        raise TypeError(
                            kOperator.getName() + ".evaluate(): Invalid Argument Value: " + str(rtVal) + " (" + type(
                                rtVal).__name__ + "), for Argument: " + portName + " (" + portDataType + ")")

                elif portDataType == 'Boolean':
                    if type(rtVal) != bool and not (type(rtVal) == int and (rtVal == 0 or rtVal == 1)):
                        raise TypeError(
                            kOperator.getName() + ".evaluate(): Invalid Argument Value: " + str(rtVal) + " (" + type(
                                rtVal).__name__ + "), for Argument: " + portName + " (" + portDataType + ")")

                elif portDataType == 'String':
                    if type(rtVal) != str:
                        raise TypeError(
                            kOperator.getName() + ".evaluate(): Invalid Argument Value: " + str(rtVal) + " (" + type(
                                rtVal).__name__ + "), for Argument: " + portName + " (" + portDataType + ")")

        try:
            if isKLBased is False:
                host = ks.getCoreClient().DFG.host
                opBinding = host.createBindingToPreset(kOperator.getPresetPath())
                node = opBinding.getExec()

                portTypeMap = {
                    0: 'In',
                    1: 'IO',
                    2: 'Out'
                }

            # Create Canvas Operator
            canvasNode = pm.createNode('canvasNode', name=buildName)
            self._registerSceneItemPair(kOperator, pm.PyNode(canvasNode))

            try:
                # disable the eval context
                pm.setAttr('%s.enableEvalContext' % canvasNode, False)
            except:
                pass

            config = Config.getInstance()
            nameTemplate = config.getNameTemplate()
            typeTokens = nameTemplate['types']
            opTypeToken = typeTokens.get(type(kOperator).__name__, 'op')
            solverNodeName = '_'.join([kOperator.getName(), opTypeToken])
            solverSolveNodeName = '_'.join([kOperator.getName(), 'solve', opTypeToken])

            if isKLBased is True:

                pm.FabricCanvasSetExtDeps(mayaNode=canvasNode,
                                          execPath="",
                                          extDep=kOperator.getExtension())

                solverTypeName = kOperator.getSolverTypeName()

                # Create Solver Function Node
                dfgEntry = "dfgEntry {\n  solver = " + solverTypeName + "();\n}"
                solverNodeCode = "{}\n\n{}".format('require ' + kOperator.getExtension() + ';', dfgEntry)

                pm.FabricCanvasAddFunc(mayaNode=canvasNode,
                                       execPath="",
                                       title=solverNodeName,
                                       code=solverNodeCode, xPos="-220", yPos="100")

                pm.FabricCanvasAddPort(mayaNode=canvasNode,
                                       execPath=solverNodeName,
                                       desiredPortName="solver",
                                       portType="Out",
                                       typeSpec=solverTypeName,
                                       connectToPortPath="",
                                       extDep=kOperator.getExtension())

                solverVarName = pm.FabricCanvasAddVar(mayaNode=canvasNode,
                                                      execPath="",
                                                      desiredNodeName="solverVar",
                                                      xPos="-75",
                                                      yPos="100",
                                                      type='{}::{}'.format(str(kOperator.getExtension()),
                                                                           str(solverTypeName)),
                                                      extDep=kOperator.getExtension())

                pm.FabricCanvasConnect(mayaNode=canvasNode,
                                       execPath="",
                                       srcPortPath=solverNodeName + ".solver",
                                       dstPortPath=solverVarName + ".value")

                # Crate Solver "Solve" Function Node
                pm.FabricCanvasAddFunc(mayaNode=canvasNode,
                                       execPath="",
                                       title=solverSolveNodeName,
                                       code="dfgEntry {}", xPos="100", yPos="100")

                pm.FabricCanvasAddPort(mayaNode=canvasNode,
                                       execPath=solverSolveNodeName,
                                       desiredPortName="solver",
                                       portType="IO",
                                       typeSpec=solverTypeName,
                                       connectToPortPath="",
                                       extDep=kOperator.getExtension())

                pm.FabricCanvasConnect(mayaNode=canvasNode,
                                       execPath="",
                                       srcPortPath=solverVarName + ".value",
                                       dstPortPath=solverSolveNodeName + ".solver")

                pm.FabricCanvasConnect(mayaNode=canvasNode,
                                       execPath="",
                                       srcPortPath=solverSolveNodeName + ".solver",
                                       dstPortPath="exec")
            else:
                pm.FabricCanvasSetExtDeps(mayaNode=canvasNode,
                                          execPath="",
                                          extDep="Kraken")

                graphNodeName = pm.FabricCanvasInstPreset(
                    mayaNode=canvasNode,
                    execPath="",
                    presetPath=kOperator.getPresetPath(),
                    xPos="100",
                    yPos="100")

            portCount = 0
            if isKLBased is True:
                portCount = len(kOperator.getSolverArgs())
            else:
                portCount = node.getExecPortCount()

            for i in xrange(portCount):

                if isKLBased is True:
                    args = kOperator.getSolverArgs()
                    arg = args[i]
                    portName = arg.name.getSimpleType()
                    portConnectionType = arg.connectionType.getSimpleType()
                    portDataType = arg.dataType.getSimpleType()
                else:
                    portName = node.getExecPortName(i)
                    portConnectionType = portTypeMap[node.getExecPortType(i)]
                    rtVal = opBinding.getArgValue(portName)
                    portDataType = rtVal.getTypeName().getSimpleType()

                if portConnectionType == 'In':
                    if isKLBased is True:
                        pm.FabricCanvasAddPort(mayaNode=canvasNode,
                                               execPath="",
                                               desiredPortName=portName,
                                               portType="In",
                                               typeSpec=portDataType,
                                               connectToPortPath="")

                        pm.FabricCanvasAddPort(mayaNode=canvasNode,
                                               execPath=solverSolveNodeName,
                                               desiredPortName=portName,
                                               portType="In",
                                               typeSpec=portDataType,
                                               connectToPortPath="")

                        pm.FabricCanvasConnect(mayaNode=canvasNode,
                                               execPath="",
                                               srcPortPath=portName,
                                               dstPortPath=solverSolveNodeName + "." + portName)

                    else:
                        if portDataType != 'Execute':
                            pm.FabricCanvasAddPort(
                                mayaNode=canvasNode,
                                execPath="",
                                desiredPortName=portName,
                                portType="In",
                                typeSpec=portDataType,
                                connectToPortPath="")

                        pm.FabricCanvasConnect(
                            mayaNode=canvasNode,
                            execPath="",
                            srcPortPath=portName,
                            dstPortPath=graphNodeName + "." + portName)

                elif portConnectionType in ['IO', 'Out']:

                    if portDataType in ('Execute', 'InlineInstance', 'DrawingHandle'):
                        # Don't expose invalid Maya data type InlineInstance, instead connect to exec port
                        dstPortPath = "exec"
                    else:
                        dstPortPath = portName

                    if isKLBased is True:
                        srcPortNode = solverSolveNodeName
                        pm.FabricCanvasAddPort(
                            mayaNode=canvasNode,
                            execPath=solverSolveNodeName,
                            desiredPortName=portName,
                            portType="Out",
                            typeSpec=portDataType,
                            connectToPortPath="")
                    else:
                        srcPortNode = graphNodeName

                    if portDataType not in ('Execute', 'InlineInstance', 'DrawingHandle'):
                        pm.FabricCanvasAddPort(
                            mayaNode=canvasNode,
                            execPath="",
                            desiredPortName=portName,
                            portType="Out",
                            typeSpec=portDataType,
                            connectToPortPath="")

                    pm.FabricCanvasConnect(
                        mayaNode=canvasNode,
                        execPath="",
                        srcPortPath=srcPortNode + "." + portName,
                        dstPortPath=dstPortPath)

                else:
                    raise Exception("Invalid connection type:" + portConnectionType)

                if portDataType == 'EvalContext':
                    continue
                elif portDataType == 'Execute':
                    continue
                elif portDataType == 'DrawingHandle':
                    continue
                elif portDataType == 'InlineDebugShape':
                    continue
                elif portDataType == 'Execute' and portName == 'exec':
                    continue

                if portName == 'time':
                    pm.expression(o=canvasNode + '.time', s=canvasNode + '.time = time;')
                    continue
                if portName == 'frame':
                    pm.expression(o=canvasNode + '.frame', s=canvasNode + '.frame = frame;')
                    continue

                # Get the port's input from the DCC
                if portConnectionType == 'In':
                    connectedObjects = kOperator.getInput(portName)
                elif portConnectionType in ['IO', 'Out']:
                    connectedObjects = kOperator.getOutput(portName)

                if portDataType.endswith('[]'):

                    # In CanvasMaya, output arrays are not resized by the system
                    # prior to calling into Canvas, so we explicily resize the
                    # arrays in the generated operator stub code.
                    if connectedObjects is None:
                        connectedObjects = []

                    connectionTargets = []
                    for i in xrange(len(connectedObjects)):
                        opObject = connectedObjects[i]
                        dccSceneItem = self.getDCCSceneItem(opObject)

                        if hasattr(opObject, "getName"):
                            # Handle output connections to visibility attributes.
                            if opObject.getName() == 'visibility' and opObject.getParent().getName() == 'implicitAttrGrp':
                                dccItem = self.getDCCSceneItem(opObject.getParent().getParent())
                                dccSceneItem = dccItem.attr('visibility')
                            elif opObject.getName() == 'shapeVisibility' and opObject.getParent().getName() == 'implicitAttrGrp':
                                dccItem = self.getDCCSceneItem(opObject.getParent().getParent())
                                shape = dccItem.getShape()
                                dccSceneItem = shape.attr('visibility')

                        connectionTargets.append(
                            {
                                'opObject': opObject,
                                'dccSceneItem': dccSceneItem
                            })
                else:
                    if connectedObjects is None:
                        if isKLBased:
                            opType = kOperator.getExtension() + ":" + kOperator.getSolverTypeName()
                        else:
                            opType = kOperator.getPresetPath()

                        logger.debug("Operator '" + solverSolveNodeName +
                                     "' of type '" + opType +
                                     "' port '" + portName + "' not connected.")

                    opObject = connectedObjects
                    dccSceneItem = self.getDCCSceneItem(opObject)
                    if hasattr(opObject, "getName"):
                        # Handle output connections to visibility attributes.
                        if opObject.getName() == 'visibility' and opObject.getParent().getName() == 'implicitAttrGrp':
                            dccItem = self.getDCCSceneItem(opObject.getParent().getParent())
                            dccSceneItem = dccItem.attr('visibility')
                        elif opObject.getName() == 'shapeVisibility' and opObject.getParent().getName() == 'implicitAttrGrp':
                            dccItem = self.getDCCSceneItem(opObject.getParent().getParent())
                            shape = dccItem.getShape()
                            dccSceneItem = shape.attr('visibility')

                    connectionTargets = {
                        'opObject': opObject,
                        'dccSceneItem': dccSceneItem
                    }

                # Add the Canvas Port for each port.
                if portConnectionType == 'In':

                    def connectInput(tgt, opObject, dccSceneItem):
                        if isinstance(opObject, Attribute):
                            pm.connectAttr(dccSceneItem, tgt)
                        elif isinstance(opObject, Object3D):
                            pm.connectAttr(dccSceneItem.attr('worldMatrix'), tgt)
                        elif isinstance(opObject, Xfo):
                            self.setMat44Attr(tgt.partition(".")[0], tgt.partition(".")[2], opObject.toMat44())
                        elif isinstance(opObject, Mat44):
                            self.setMat44Attr(tgt.partition(".")[0], tgt.partition(".")[2], opObject)
                        elif isinstance(opObject, Vec2):
                            pm.setAttr(tgt, opObject.x, opObject.y, type="double2")
                        elif isinstance(opObject, Vec3):
                            pm.setAttr(tgt, opObject.x, opObject.y, opObject.z, type="double3")
                        else:
                            validatePortValue(opObject, portName, portDataType)

                            pm.setAttr(tgt, opObject)

                    if portDataType.endswith('[]'):
                        for i in xrange(len(connectionTargets)):
                            connectInput(
                                canvasNode + "." + portName + '[' + str(i) + ']',
                                connectionTargets[i]['opObject'],
                                connectionTargets[i]['dccSceneItem'])
                    else:
                        connectInput(
                            canvasNode + "." + portName,
                            connectionTargets['opObject'],
                            connectionTargets['dccSceneItem'])

                elif portConnectionType in ['IO', 'Out']:

                    def connectOutput(src, opObject, dccSceneItem):
                        if isinstance(opObject, Attribute):
                            locked = dccSceneItem.isLocked()
                            dccSceneItem.unlock()
                            pm.connectAttr(src, dccSceneItem)
                            dccSceneItem.setLocked(locked)
                        elif isinstance(opObject, Object3D):
                            decomposeNode = pm.createNode('decomposeMatrix')
                            pm.connectAttr(src,
                                           decomposeNode.attr("inputMatrix"),
                                           force=True)

                            decomposeNode.attr("outputRotate").connect(dccSceneItem.attr("rotate"))
                            decomposeNode.attr("outputScale").connect(dccSceneItem.attr("scale"))
                            decomposeNode.attr("outputTranslate").connect(dccSceneItem.attr("translate"))
                        elif isinstance(opObject, Xfo):
                            raise NotImplementedError(
                                "Kraken Canvas Operator cannot set object [%s] outputs with Xfo outputs types directly!")
                        elif isinstance(opObject, Mat44):
                            raise NotImplementedError(
                                "Kraken Canvas Operator cannot set object [%s] outputs with Mat44 types directly!")
                        else:
                            raise NotImplementedError(
                                "Kraken Canvas Operator cannot set object [%s] outputs with Python built-in types [%s] directly!" % (
                                    src, opObject.__class__.__name__))

                    if portDataType.endswith('[]'):
                        for i in xrange(len(connectionTargets)):
                            connectOutput(
                                str(canvasNode + "." + portName) + '[' + str(i) + ']',
                                connectionTargets[i]['opObject'],
                                connectionTargets[i]['dccSceneItem'])
                    else:
                        if connectionTargets['opObject'] is not None:
                            connectOutput(
                                str(canvasNode + "." + portName),
                                connectionTargets['opObject'],
                                connectionTargets['dccSceneItem'])

            if isKLBased is True:
                opSourceCode = kOperator.generateSourceCode()
                pm.FabricCanvasSetCode(mayaNode=canvasNode,
                                       execPath=solverSolveNodeName,
                                       code=opSourceCode)

            if kOperator.testFlag('disableParallelEval') is False:
                pm.FabricCanvasSetExecuteShared(mayaNode=canvasNode, enable=True)

        finally:
            pass

        return True

    # ==================
    # Attribute Methods
    # ==================
    def lockAttribute(self, kAttribute):
        """Locks attributes.
        Args:
            kAttribute (object): kraken attributes to lock.
        """

        if kAttribute.getName() in ('visibility', 'ShapeVisibility'):
            dccSceneItem = self.getDCCSceneItem(kAttribute.getParent().getParent())

            if kAttribute.getName() == 'visibility':
                visAttr = dccSceneItem.attr('visibility')
                visAttr.setLocked(kAttribute.getLock())
            elif kAttribute.getName() == 'ShapeVisibility':
                shapeNodes = pm.listRelatives(dccSceneItem, shapes=True)
                for shape in shapeNodes:
                    visAttr = shape.attr('visibility')
                    visAttr.setLocked(kAttribute.getLock())
            else:
                pass

        else:
            dccSceneItem = self.getDCCSceneItem(kAttribute)
            dccSceneItem.setLocked(kAttribute.getLock())

    def lockTransformAttrs(self, kSceneItem):
        """Locks flagged SRT attributes.
        Args:
            kSceneItem (Object): Kraken object to lock the SRT attributes on.
        Return:
            bool: True if successful.
        """

        dccSceneItem = self.getDCCSceneItem(kSceneItem)

        # Lock Rotation
        if kSceneItem.testFlag("lockXRotation") is True:
            pm.setAttr(
                dccSceneItem.longName() + "." + 'rx',
                lock=True,
                keyable=False,
                channelBox=False)

        if kSceneItem.testFlag("lockYRotation") is True:
            pm.setAttr(
                dccSceneItem.longName() + "." + 'ry',
                lock=True,
                keyable=False,
                channelBox=False)

        if kSceneItem.testFlag("lockZRotation") is True:
            pm.setAttr(
                dccSceneItem.longName() + "." + 'rz',
                lock=True,
                keyable=False,
                channelBox=False)

        # Lock Scale
        if kSceneItem.testFlag("lockXScale") is True:
            pm.setAttr(
                dccSceneItem.longName() + "." + 'sx',
                lock=True,
                keyable=False,
                channelBox=False)

        if kSceneItem.testFlag("lockYScale") is True:
            pm.setAttr(
                dccSceneItem.longName() + "." + 'sy',
                lock=True,
                keyable=False,
                channelBox=False)

        if kSceneItem.testFlag("lockZScale") is True:
            pm.setAttr(
                dccSceneItem.longName() + "." + 'sz',
                lock=True,
                keyable=False,
                channelBox=False)

        # Lock Translation
        if kSceneItem.testFlag("lockXTranslation") is True:
            pm.setAttr(
                dccSceneItem.longName() + "." + 'tx',
                lock=True,
                keyable=False,
                channelBox=False)

        if kSceneItem.testFlag("lockYTranslation") is True:
            pm.setAttr(
                dccSceneItem.longName() + "." + 'ty',
                lock=True,
                keyable=False,
                channelBox=False)

        if kSceneItem.testFlag("lockZTranslation") is True:
            pm.setAttr(
                dccSceneItem.longName() + "." + 'tz',
                lock=True,
                keyable=False,
                channelBox=False)

        return True

    # ===================
    # Visibility Methods
    # ===================
    def setVisibility(self, kSceneItem):
        """Sets the visibility of the object after its been created.
        Args:
            kSceneItem (Object): The scene item to set the visibility on.
        Return:
            bool: True if successful.
        """

        dccSceneItem = self.getDCCSceneItem(kSceneItem)

        # Set Visibility
        visAttr = kSceneItem.getVisibilityAttr()
        if visAttr.isConnected() is False and kSceneItem.getVisibility() is False:
            dccSceneItem.visibility.set(False)

        # Set Shape Visibility
        shapeVisAttr = kSceneItem.getShapeVisibilityAttr()
        if shapeVisAttr.isConnected() is False and kSceneItem.getShapeVisibility() is False:
            # Get shape node, if it exists, hide it.
            shapeNodes = pm.listRelatives(dccSceneItem, shapes=True)
            for shape in shapeNodes:
                visAttr = shape.attr('visibility')
                visAttr.set(False)

        return True

    # ================
    # Display Methods
    # ================
    def setObjectColor(self, kSceneItem):
        """Sets the color on the dccSceneItem.
        Args:
            kSceneItem (object): kraken object to set the color on.
        Return:
            bool: True if successful.
        """

        colors = self.config.getColors()
        dccSceneItem = self.getDCCSceneItem(kSceneItem)
        buildColor = self.getBuildColor(kSceneItem)

        if buildColor is not None:

            if pm.about(version=True).startswith("2015"):
                dccSceneItem.overrideEnabled.set(True)

                def getClosestColor(colorIn):
                    maxValue = 10000000000
                    index = None
                    for i, key in enumerate(MAYA_2015_COLORS):
                        print "========================="
                        print colorIn
                        print MAYA_2015_COLORS[key][1]
                        print "========================="
                        dist = (MAYA_2015_COLORS[key][1][0] - colorIn[0]) * (MAYA_2015_COLORS[key][1][0] - colorIn[0]) + \
                               (MAYA_2015_COLORS[key][1][1] - colorIn[1]) * (MAYA_2015_COLORS[key][1][1] - colorIn[1]) + \
                               (MAYA_2015_COLORS[key][1][2] - colorIn[2]) * (MAYA_2015_COLORS[key][1][2] - colorIn[2])

                        dist /= 3.0
                        if dist < maxValue:
                            maxValue = dist
                            index = i
                            closestKey = key

                    return closestKey

                if type(buildColor) is str:

                    targetColor = colors[buildColor]

                    # Color in config is stored as a Color object
                    if type(colors[buildColor]).__name__ == 'Color':
                        targetColor = [colors[buildColor].r,
                                       colors[buildColor].g,
                                       colors[buildColor].b]

                    # Get the closest color to the limited Maya 2015 colors
                    buildColor = getClosestColor(targetColor)

                    dccSceneItem.overrideColor.set(MAYA_2015_COLORS[buildColor][0])

                elif type(buildColor).__name__ == 'Color':
                    buildColor = [buildColor.r,
                                  buildColor.g,
                                  buildColor.b]

                    # Get the closest color to the limited Maya 2015 colors
                    buildColor = getClosestColor(buildColor)

                    dccSceneItem.overrideColor.set(MAYA_2015_COLORS[buildColor][0])

            else:
                dccSceneItem.overrideEnabled.set(True)
                dccSceneItem.overrideRGBColors.set(True)

                if type(buildColor) is str:

                    # Color in config is stored as rgb scalar values in a list
                    if type(colors[buildColor]) is list:
                        dccSceneItem.overrideColorRGB.set(colors[buildColor][0], colors[buildColor][1],
                                                          colors[buildColor][2])

                    # Color in config is stored as a Color object
                    elif type(colors[buildColor]).__name__ == 'Color':
                        dccSceneItem.overrideColorRGB.set(colors[buildColor].r, colors[buildColor].g,
                                                          colors[buildColor].b)

                elif type(buildColor).__name__ == 'Color':
                    dccSceneItem.overrideColorRGB.set(colors[buildColor].r, colors[buildColor].g, colors[buildColor].b)

        return True

    # ==================
    # Transform Methods
    # ==================
    def setTransform(self, kSceneItem):
        """Translates the transform to Maya transform.
        Args:
            kSceneItem -- Object: object to set the transform on.
        Return:
            bool: True if successful.
        """

        dccSceneItem = self.getDCCSceneItem(kSceneItem)

        quat = dt.Quaternion(kSceneItem.xfo.ori.v.x,
                             kSceneItem.xfo.ori.v.y,
                             kSceneItem.xfo.ori.v.z,
                             kSceneItem.xfo.ori.w)

        dccSceneItem.setScale(dt.Vector(
            kSceneItem.xfo.sc.x,
            kSceneItem.xfo.sc.y,
            kSceneItem.xfo.sc.z))

        dccSceneItem.setTranslation(dt.Vector(
            kSceneItem.xfo.tr.x,
            kSceneItem.xfo.tr.y,
            kSceneItem.xfo.tr.z),
            "world")

        dccSceneItem.setRotation(quat, "world")

        order = ROT_ORDER_REMAP[kSceneItem.ro.order]

        #  Maya api is one off from Maya's own node enum pyMel uses API
        dccSceneItem.setRotationOrder(order + 1, False)

        pm.select(clear=True)

        return True

    def setMat44Attr(self, dccSceneItemName, attr, mat44):
        """Sets a matrix attribute directly with values from a fabric Mat44.
        Note: Fabric and Maya's matrix row orders are reversed, so we transpose
        the matrix first.
        Args:
            dccSceneItemName (str): name of dccSceneItem.
            attr (str): name of matrix attribute to set.
            mat44 (Mat44): matrix value.
        Return:
            bool: True if successful.
        """

        mat44 = mat44.transpose()
        matrix = []
        rows = [mat44.row0, mat44.row1, mat44.row2, mat44.row3]
        for row in rows:
            matrix.extend([row.x, row.y, row.z, row.t])

        cmds.setAttr(dccSceneItemName + "." + attr, matrix, type="matrix")

        return True

    # ==============
    # Build Methods
    # ==============
    def _preBuild(self, kSceneItem):
        """Pre-Build commands.
        Args:
            kSceneItem (Object): Kraken kSceneItem object to build.
        Return:
            bool: True if successful.
        """

        return True

    def _postBuild(self, kSceneItem):
        """Post-Build commands.
        Args:
            kSceneItem (object): kraken kSceneItem object to run post-build
                operations on.
        Return:
            bool: True if successful.
        """

        super(Builder, self)._postBuild(kSceneItem)

        return True
