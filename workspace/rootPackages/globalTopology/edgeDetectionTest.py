import time
import skimage.io as io
from rootPackages.general.utils.dataExtraction import readImage
from rootPackages.general.utils.dataExploration import printTime, displayImage
from rootPackages.globalTopology.edgeDetection import extractEdges

def edgeDetectionTest():
    image2D = readImage("images/imageTest1.jpg")[:, :, 0]
    image = image2D[100:200, 100:200]

    start = time.time()
    edges = extractEdges(image)
    printTime(start)



