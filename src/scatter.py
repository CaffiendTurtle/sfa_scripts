import logging

from PySide2 import QtWidgets, QtCore, QtGui
import maya.cmds as cmds

def random_scale():



def random_rotate():
    # print(random rotate)
    # determine range of rotation from range of 0 to 360 in each axis
    # determine position of vertice
    # check determined rotation numbers
    # Check if object is rotated
    # If not then rotate based upon random number selection
    # this will be a for loop


def place_instances():
    selected_verts = cmds.ls(flatten=True, orderedSelection=True)
    for vert in selected_verts:
        # user can select an object to instance(grabs string name)
        # create an instance
        path_to_instance = cmds.instance('pCube1')
        # move it to selected vert
        position = cmds.pointPosition(vert)
        cmds.move(position[0], position[1], position[2], path_to_instance)
        # call random_scale()
        # call random_rotate()
