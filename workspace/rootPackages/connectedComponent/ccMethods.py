import numpy as np
from copy import copy
from rootPackages.connectedComponent.cell import getSubCells, dim
from rootPackages.general.utils.voxels import makeUnique

'''
This module will define functions to extract CC features, 
such as its eulerchar.
'''

#A CC is a list of arrays (coordinates of cells belonging to the CC)

def getAllCells(cc):
    out = copy(cc)
    for cell in cc:
        out = out + getSubCells(cell)
    return makeUnique(out)

def euler(cc):
    out = 0
    out2 = tuple()
    #allCells = getAllCells(cc)
    allCells = cc
    for d in range(len(cc[0])+1):
        out = out + ((-1)**d) * len([c for c in allCells if dim(c) == d])
        out2 = out2 + (len([c for c in allCells if dim(c) == d]), )
    return out2

