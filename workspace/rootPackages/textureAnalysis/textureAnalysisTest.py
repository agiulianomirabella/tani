import sys
sys.path.append('/home/giuliano/Desktop/tabi/VSCodeWS_TABI')

import numpy as np
import time
from general.preProcessing import colorNormalizationRange
from textureAnalysis import completeLocalTopologicalHistogram, diversityTextureAnalysis
from general.utils import readImage, displayImageShape

'''
The pourpose of this module is testing the texture analysis on real biomedical images
'''

def textureAnalysisTest():
    image2D = readImage("images/imageTest1.jpg")[:, :, 0]

    image = image2D
    displayImageShape(image)

    image = colorNormalizationRange(image, 3)

    start = time.time()
    analyzed = completeLocalTopologicalHistogram(image, 3)
    print("Total execution time: {}".format(round(time.time()-start, 2)))

