import logging

from PySide2 import QtWidgets, QtCore, QtGui
import random
import maya.cmds as cmds


# rotx = int(input())
# roty = int(input())
# rotz = int(input())


# def ran_rotation(new_instance):



# def ran_scaling():


def place_instances():
    selected_geo = cmds.ls(orderedSelection=True, flatten=True)
    selected_verts = cmds.filterExpand(expand=True, selectionMask=31)
    fx_select = int(input())
    sx_select = int(input())
    fy_select = int(input())
    sy_select = int(input())
    fz_select = int(input())
    sz_select = int(input())
    for vert in selected_verts:
        # create a new instance based upon first selection
        new_instance = cmds.instance(selected_geo)
        # find the positions of selected vertices
        position = cmds.pointPosition(vert)
        # place the newly created instances onto the vertice positions
        cmds.move(position[0], position[1], position[2], new_instance)
        # creates random rotations for each instance created
        # need to create its own function so that I can just place that in
        xRot = random.uniform(fx_select, sx_select)
        yRot = random.uniform(fy_select, sy_select)
        zRot = random.uniform(fz_select, sz_select)
        cmds.rotate(xRot, yRot, zRot, new_instance)
        # creates random scaling for each instance based upon a hard code range
        # needs to be placed in its own function and needs to be a for loop
        # need the range to be selective
        scaling_Factor = random.uniform(100, 200)
        cmds.scale(scaling_Factor, scaling_Factor, scaling_Factor,
                   new_instance)
