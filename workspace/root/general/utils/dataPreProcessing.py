import numpy as np
import copy
from scipy.ndimage import label, find_objects
 
'''
This module will define functions to preProcess an image, before further analysis is done
'''

def normalize(image):
    #return the normalized image
    image = image - np.min(image)
    return image/np.max(image)

def binarize(image, grayLevel):
    #set grayLevel voxels to 1 and different to 0
    out = np.zeros(image.shape)
    out[image == grayLevel] = 1
    return out

def setGrayThreshold(image, grayLevel):
    #set grayLevel or less voxels to 0 and more-than-grayLevel voxels to 1
    out = copy.copy(image)
    out[image <= grayLevel] = 0
    out[image > grayLevel] = 1
    return out

def setGrayThresholds(image, lowerLimit = 0, upperLimit = 1):
    #set lower than lowerLimit grayValues to 0 and higher to 1

    out = copy.copy(image)
    if lowerLimit < 0:
        lowerLimit = 0
    if upperLimit > 1:
        upperLimit = 1

    out[image < lowerLimit] = 0
    out[image > upperLimit] = upperLimit
    return normalize(out)

def setPercentileGrayThresholds(image, lowerLimitPercentile = 0, upperLimitPercentile = 100):
    #Set lowerLimitPercentile grayLeves to 0 and upperLimitPercentile to 1

    if lowerLimitPercentile < 0:
        lowerLimitPercentile = 0
    if upperLimitPercentile > 100:
        upperLimitPercentile = 100

    lowerLimit = np.percentile(image, lowerLimitPercentile)
    upperLimit = np.percentile(image, upperLimitPercentile)

    #print()
    #print('The {} (lower) percentile gray level is: {}'.format(lowerLimitPercentile, round(lowerLimit, 2)))
    #print('The {} (upper) percentile gray level is: {}'.format(upperLimitPercentile, round(upperLimit, 2)))

    return setGrayThresholds(image, lowerLimit, upperLimit)

def digitizeToEqualFrequencies(image, binsNumber):
    #equal frequency binning of the image
    out = np.zeros(image.shape)
    labels = [i for i in range(binsNumber)]
    elements = np.sort(image.flatten())
    elementsPerBin = image.size//binsNumber
    bin_edges = [elements[i*elementsPerBin] for i in labels]
    for i, e in enumerate(bin_edges):
        out[image > e] = labels[i]
    return normalize(out)
    
def digitizeToEqualWidth(image, GrayLevelsNumber):
    #equal width binning of the image
    if GrayLevelsNumber > len(np.unique(image)):
        GrayLevelsNumber = len(np.unique(image))
    return normalize(np.digitize(image, bins = np.linspace(0, np.max(image), GrayLevelsNumber)) - 1)

def centerImage(image):
    #delete empty borders of the image
    aux = copy.copy(image)
    aux[image>0] = 1
    aux = aux.astype(int)
    margins = find_objects(aux)[0]
    return image[margins], margins

def addZeroMargins(image):
    #add zero margins to ndarray
    padWidth = tuple()
    constantValues = tuple()
    for _ in range(image.ndim):
        padWidth = padWidth  + ((1, 1), )
        constantValues = constantValues  + ((0, 0), )
    return np.pad(image, padWidth, 'constant', constant_values=constantValues)

