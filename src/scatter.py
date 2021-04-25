import logging

from PySide2 import QtWidgets, QtCore, QtGui
import random
import maya.cmds as cmds


def ran_rotation(new_instance):
    minX_rotation = int(input())
    maxX_rotation = int(input())
    minY_rotation = int(input())
    maxY_rotation = int(input())
    minZ_rotation = int(input())
    maxZ_rotation = int(input())
    xRot = random.uniform(minX_rotation, maxX_rotation)
    yRot = random.uniform(minY_rotation, maxY_rotation)
    zRot = random.uniform(minZ_rotation, maxZ_rotation)
    cmds.rotate(xRot, yRot, zRot, new_instance)


def ran_scaling(new_instance):
     # allows user to set their own min max scale
     # needs to be placed in its own function and needs to be a for loop
     min_scale = int(input())
     max_scale = int(input())
     scaling_Factor = random.uniform(min_scale, max_scale)
     cmds.scale(scaling_Factor, scaling_Factor, scaling_Factor, new_instance)


def place_instances():
    selected_geo = cmds.ls(orderedSelection=True, flatten=True)
    selected_verts = cmds.filterExpand(expand=True, selectionMask=31)
    # min_scale = int(input())
    # max_scale = int(input())
    for vert in selected_verts:
        # create a new instance based upon first selection
        new_instance = cmds.instance(selected_geo)
        # find the positions of selected vertices
        position = cmds.pointPosition(vert)
        # place the newly created instances onto the vertice positions
        cmds.move(position[0], position[1], position[2], new_instance)
        # creates random rotations for each instance created
        # user can create min max values for their rotation range per axis
        # need to create its own function so that I can just place that in
        ran_rotation(new_instance)
        ran_scaling(new_instance)
