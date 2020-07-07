import numpy as np
import time
import pydicom as dcm
import skimage.io as io
import os
from root.globalTopology.globalTopology import topologicalHistogram
from root.general.utils.dataPreProcessing import digitizeToEqualWidth
from root.globalTopology.ccExtraction import extractCCListByGrayValue
from root.general.utils.dataExtraction import readDicomImageAsArray

'''
This module is intended to test the global topology analysis on real biomedical images
'''

def globalTopologyTest():
    image2D = io.imread("images/imageTest1.jpg")[:, :, 0]
    image3D = readDicomImageAsArray("images/case1/")

    image = image3D
    print(np.shape(image))
    preProcessed = digitizeToEqualWidth(image, 50)
    start = time.time()
    t = topologicalHistogram(preProcessed)
    print("Total execution time: {}".format(time.time()-start))


