import numpy as np
import os
import time
import skimage.io as io
import pydicom as dcm
import matplotlib.pyplot as plt
from scipy.ndimage.morphology import generate_binary_structure

'''
This module will provide some helpful auxiliary permutations functions
'''

#Initial maximum value for spaceDimension:
maximumSpaceDimension = 10

def permutationAuxFunction1(n):
    return permutationAuxFunctionREC1(n, [], 0)

def permutationAuxFunctionREC1(n, l, i):
    if i == n:
        return [l]
    else:
        l1 = l[:]
        l2 = l[:]
        l3 = l[:]
        l1.append(-1/2)
        l2.append(0)
        l3.append(+1/2)
        return permutationAuxFunctionREC1(n, l1, i+1) + permutationAuxFunctionREC1(n, l2, i+1) + permutationAuxFunctionREC1(n, l3, i+1)

permutations1 = []
for i in range(maximumSpaceDimension+1):
    x = permutationAuxFunction1(i)
    x.remove([0]*i)
    permutations1.append(x)

