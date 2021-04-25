import logging

from PySide2 import QtWidgets, QtCore, QtGui
import maya.cmds as cmds


def place_instances():
    selected_geo = cmds.ls(orderedSelection=True, flatten=True)
    selected_verts = cmds.filterExpand(expand=True, selectionMask=31)

    for vert in selected_verts:
        # create a new instance based upon first selection
        new_instance = cmds.instance(selected_geo)
        # find the positions of selected vertices
        position = cmds.pointPosition(vert)
        # place the newly created instances onto the vertice positions
        cmds.move(position[0], position[1], position[2], new_instance)
