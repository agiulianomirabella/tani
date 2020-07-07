import numpy as np
import time
from root.globalTopology.ccExtraction import extractCCInfoByGrayValue
from root.connectedComponent.ccMethods import euler

'''
This module will define functions to compute a global topology output of an image.
Several uncomment may be done to analyze the functions' time performance
'''

def topologicalHistogram(image, connectivity = -1):
    #return a dictionary which keys are: (grayValue, euler, size) and values: number of occurrences
    out = dict()
    grayValues = np.delete(np.unique(image), 0)
    ccInfoListByGrayValue = extractCCInfoByGrayValue(image, connectivity)
    for i, ccList in enumerate(ccInfoListByGrayValue):
        for ccInfo in ccList:
            x = euler(ccInfo[0])
            print(x)
            if (grayValues[i], x, ccInfo[1]) in out.keys():
                out[(grayValues[i], x, ccInfo[1])] = out[(grayValues[i], x, ccInfo[1])] + 1
            else:
                out.update({(grayValues[i], x, ccInfo[1]) : 1})
    return out

