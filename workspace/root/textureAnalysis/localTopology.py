import numpy as np
from rootPackages.globalTopology.ccExtraction import extractCCListByGrayValue
from rootPackages.connectedComponent.ccMethods import euler

'''
This module will define functions to convolve on an image in order to acquire later a texture analysis.
Window parameter is therefore supposed to be a small sized squared ndarray
'''

def diversity(window):
    return len(np.unique(window))

def localReducedTopologicalHistogram(window, connectivity = -1):
    #return a dictionary which keys are: (grayValue, euler, size) and values: number of occurrences
    #start = time.time()
    out = dict()
    grayValues = np.delete(np.unique(window), 0)
    ccListByGrayValue = extractCCListByGrayValue(window, connectivity)
    for i, grayValueCCs in enumerate(ccListByGrayValue):
        for cc in grayValueCCs:
            x = euler(cc)
            if (grayValues[i], x, len(cc)) in out.keys():
                out[(grayValues[i], x, len(cc))] = out[(grayValues[i], x, len(cc))] + 1
            else:
                out.update({(grayValues[i], x, len(cc)) : 1})
    return out

def auxiliarLocalCompleteTopologyForMonochromeWindow(window):
    #return a dict such (grayValue, euler, size) : 1
    return {(np.unique(window)[0], 1, np.size(window)) : 1}


        

