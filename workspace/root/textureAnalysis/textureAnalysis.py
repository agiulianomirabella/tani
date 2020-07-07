from rootPackages.globalTopology.globalTopology import topologicalHistogram
from rootPackages.textureAnalysis.localTopology import diversity, auxiliarLocalCompleteTopologyForMonochromeWindow
from rootPackages.textureAnalysis.convolutions import applyFunctionConvolution, applyNonMonochromeFunctionConvolution

'''
This module is intended to define functions 
to compute the texture analysis on a complete image
'''

def completeLocalTopologicalHistogram(image, windowWidth):
    return applyNonMonochromeFunctionConvolution(image, auxiliarLocalCompleteTopologyForMonochromeWindow, 
        topologicalHistogram, windowWidth)

def diversityTextureAnalysis(image, windowWidth):
    return applyFunctionConvolution(image, diversity, windowWidth)

