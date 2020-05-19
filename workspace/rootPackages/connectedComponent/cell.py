import numpy as np
from rootPackages.general.utils.permutations import permutations1
from rootPackages.general.utils.voxels import makeUnique

'''
This module is intended to process and access cell's features, 
such as its dimension, or subcells. A cell is a ndarray.

There is no need of declaring the function 'isCell'. 

Furthermore, if it is declared, the global topological output will be incorrect
because of the localization of objects by slices in the image, once labeled.
See find_objects function in topological Module for more info

def isCell(cell):
    return all(cell >= 1/2)
'''

def dim(cell):
    return len([i for i in range(len(cell)) if cell[i]%1 == 0])

def getRationalIndices(cell):
    return [i for i in range(len(cell)) if cell[i]%1 != 0]

def getSubCells(cell): #return a list of subCells
    out = []
    x = permutations1[len(cell)]
    for l in x:
        if all(l[i]==0 for i in getRationalIndices(cell)):
            a = cell + np.array(l)
            out.append(a)
    return makeUnique(out)

