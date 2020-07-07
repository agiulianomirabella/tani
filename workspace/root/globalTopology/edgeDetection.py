import numpy as np
import time
from root.general.utils.voxels import makeUnique
from root.general.utils.dataExploration import printTime
from root.general.utils.dataPreProcessing import addZeroMargins
from root.textureAnalysis.convolutionUtils import extractWindow, is3x3Window
from root.connectedComponent.ccMethods import getAllCells

'''
The pourpose of this module is to acquire all edges coordinates in a given an image
'''

def extractEdges(image):
    image = addZeroMargins(image)
    edges = []
    windowCenter = tuple()
    for _ in range(image.ndim):
        windowCenter = windowCenter + (1, )
    rank = image.ndim
    aux = np.fabs(np.indices([3] * rank) - 1)
    aux = np.add.reduce(aux, 0)
    expectedShape = aux.shape
    ones = np.ones(image.ndim)
    
    for center in np.ndindex(image.shape):
        grayValueToCompare = image[center]
        window = extractWindow(image, center, 3)
        #check also if window is monochrome
        if window.size!=0 and is3x3Window(window, expectedShape): #border-elements-centered windows size will equal zero
            edges = edges + [np.array(center) + i - ones for i in localEdgeExtraction(window, grayValueToCompare, windowCenter)]
    return makeUnique(edges)

def localEdgeExtraction(window, grayValueToCompare, windowCenter):
    #return a list of all edges coordinates in a 3x3x...x3 window
    out = []
    for index in np.ndindex(window.shape):
        if window[index] != grayValueToCompare:
            out.append((np.array(index)-windowCenter)/2)
    return out
