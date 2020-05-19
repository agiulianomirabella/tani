import numpy as np
import matplotlib.pyplot as plt
from rootPackages.globalTopology.globalTopology import topologicalHistogram
from rootPackages.general.utils.dataExploration import display2DImage

'''
This module is intended to verify the reliability of the global topological functions outputs

The correct analysis of the 2D array 'a' should be the following:
gray value: 5
   1 CC of eulerchar 0 of size 1200
   1 CC of eulerchar 0 of size 32

gray value: 10
   1 CC of eulerchar 0 of size 2800
   1 CC of eulerchar 1 of size 4

gray value: 20
   2 CC of eulerchar 1 of size 25
   1 CC of eulerchar -2 of size 192
'''

def globalTopologyCheckUp():
   a = np.zeros([120, 120])

   a[10:90, 10:90] = 10
   a[20:80, 20:80] = 0
   a[30:70, 30:70] = 5
   a[40:60, 40:60] = 0

   a[100:105, 100:105] = 20
   a[106:111, 106:111] = 20

   a[100:110, 20:50] = 20
   a[102:108, 22:28] = 0
   a[102:108, 32:38] = 0
   a[102:108, 42:48] = 5
   a[104:106, 44:46] = 10

   display2DImage(a)

   t = topologicalHistogram(a)

   print('\nExpected output:')
   print('{(5.0, 0, 1200): 1, (5.0, 0, 32): 1, (10.0, 0, 2800): 1, (10.0, 1, 4): 1, (20.0, -2, 192): 1, (20.0, 1, 25): 2}')
   print('\nObtained output:')
   print(t)
   print()
