"""This module contains the building blocks for rig concepts implemented via organized groups of DCC nodes."""
import base
import control
import sub_rig
import rig
import chunk

from base import AbstractGrouping
from control import Control
from sub_rig import SubRig
from rig import Rig
from chunk import BaseCollection
from chunk import NodeChain
from chunk import NodeSet

__all__ = ['base',
           'control',
           'sub_rig',
           'rig',
           'chunk',
           'Control',
           'SubRig',
           'Rig',
           'AbstractGrouping',
           'BaseCollection',
           'NodeChain',
           'NodeSet']
