import random as rnd
import numpy as np
import skimage.io as io
from dataPreProcessing import normalize
import os
import pydicom as dcm

def readImage(path):
    #given an image path, return the image as an numpy array
    return normalize(np.array(io.imread(path)))

def readDicomImageAsArray(path):
    #given a dicom file folder path, return its image as a numpy array
    if path[-1] != "/":
        path = path + "/"
    ds = []
    for i in os.listdir(path):
        ds.append(dcm.dcmread(path + i))
    slices = []
    for f in ds:
        if hasattr(f, 'SliceLocation'):
            slices.append(f)

    # ensure they are in the correct order
    image = np.array([s.pixel_array for s in sorted(slices, key=lambda s: s.SliceLocation)])
    return normalize(np.swapaxes(image[::-1, ::-1, :], 1, 2))

