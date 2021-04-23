import logging

from PySide2 import QtWidgets, QtCore, QtGui
import maya.cmds as cmds


def random_scale():
    print('random scaling')


def place_instances():
    selected_verts = cmds.ls(flatten=True, orderedSelection=True)
    for vert in selected_verts:
        # create an instance
        path_to_instance = cmds.instance('pCube4')
        # move it to selected vert
        position = cmds.pointPosition(vert)
        cmds.move(position[0], position[1], position[2], path_to_instance)
        random_scale()
        # random_rotate()
