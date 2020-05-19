import numpy as np
import time
from scipy.ndimage import label, find_objects
from scipy.ndimage.morphology import generate_binary_structure
from rootPackages.general.utils.dataPreProcessing import binarize
from rootPackages.globalTopology.edgeDetection import extractEdges

'''
This module is intended to define functions to extract CCs from a ndimage, 
by gray level differentiation
'''

def getGrayValueCoordinates(image, grayValue):
    #return a list of all coordinates where image ncells takes the value grayValue
    out = []
    info = np.where(image == grayValue)
    for i in range(len(info[0])):
        a = []
        for dim in info:
            a.append(dim[i])
        out.append(np.array(a))
    return out

def extractCCInfoByGrayValue(image, connectivity = -1):
    #return a list of lists of tuples such as: (ccEdges, ccSize) ordered by grayValues
    if connectivity<1 or connectivity>np.ndim(image):
        connectivity = np.ndim(image)
    out = []
    binary_structure = generate_binary_structure(np.ndim(image), connectivity)
    grayValues = np.delete(np.unique(image), 0)
    for i, g in enumerate(grayValues):
        out.append([])
        binarized = binarize(image, g)
        labeled, n = label(binarized, binary_structure)
        slices = find_objects(labeled)
        for l in range(1, n+1):
            sliced = labeled[slices[l-1]]
            sliced = binarize(sliced, l)
            cc = getGrayValueCoordinates(sliced, 1)
            out[i].append((extractEdges(sliced), len(cc)))
    return out

def extractCCListByGrayValue(image, connectivity = -1):
    #return a list of CC ordered by gray values
    #start1 = time.time()
    if connectivity<1 or connectivity>np.ndim(image):
        connectivity = np.ndim(image)
    out = []
    binary_structure = generate_binary_structure(np.ndim(image), connectivity)
    grayValues = np.delete(np.unique(image), 0)
    for i, g in enumerate(grayValues):
        out.append([])
        binarized = binarize(image, g)
        labeled, n = label(binarized, binary_structure)
        slices = find_objects(labeled)
        for l in range(1, n+1):
            sliced = labeled[slices[l-1]]
            out[i].append(getGrayValueCoordinates(sliced, l))
    #print("extractCCListbyGrayValue: {}".format(round(time.time() - start1, 2)))
    return out


'''
def getGrayValueCoordinates(image, grayValue):
    #return a list of all coordinates where image ncells takes the value grayValue
    out = []
    info = np.where(image == grayValue)
    for i in range(len(info[0])):
        a = []
        for dim in info:
            a.append(dim[i])
        out.append(np.array(a))
    return out

def extractCCListByGrayValue(image, connectivity = -1):
    #return a list of CC ordered by gray values
    #start1 = time.time()
    if connectivity<1 or connectivity>np.ndim(image):
        connectivity = np.ndim(image)
    out = []
    binary_structure = generate_binary_structure(np.ndim(image), connectivity)
    grayValues = np.delete(np.unique(image), 0)
    for i, g in enumerate(grayValues):
        out.append([])
        binarized = binarize(image, g)
        labeled, n = label(binarized, binary_structure)
        slices = find_objects(labeled)
        for l in range(1, n+1):
            sliced = labeled[slices[l-1]]
            out[i].append(getGrayValueCoordinates(sliced, l))
    #print("extractCCListbyGrayValue: {}".format(round(time.time() - start1, 2)))
    return out
'''

