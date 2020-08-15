import numpy as np
import time
from root.globalTopology.ccExtraction import extractCCListByGrayValue
from root.connectedComponent.ccMethods import euler

'''
This module will define functions to compute a global topology output of an image.
Several uncomment may be done to analyze the functions' time performance
'''

def topologicalHistogram(image, connectivity = -1):
    #return a dictionary which keys are: (grayValue, euler, size) and values: number of occurrences
    out = dict()
    grayValues = np.delete(np.unique(image), 0)
    ccListByGrayValue = extractCCListByGrayValue(image, connectivity)
    for i, ccList in enumerate(ccListByGrayValue):
        for cc in ccList:
            x = euler(cc)
            if (grayValues[i], x, len(cc)) in out.keys():
                out[(grayValues[i], x, len(cc))] = out[(grayValues[i], x, len(cc))] + 1
            else:
                out.update({(grayValues[i], x, len(cc)) : 1})
    return out

