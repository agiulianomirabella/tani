import time
import skimage.io as io
from root.general.utils.dataExtraction import readImage
from root.general.utils.dataExploration import printTime, displayImage
from root.globalTopology.edgeDetection import extractEdges

def edgeDetectionTest():
    image2D = readImage("images/imageTest1.jpg")[:, :, 0]
    image = image2D[100:200, 100:200]

    start = time.time()
    edges = extractEdges(image)
    printTime(start)



