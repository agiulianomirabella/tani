import numpy as np
from root.connectedComponent.ccMethods import euler

'''
This module is intended to verify the reliability of the euler function output

The cc1 is a 3x3x3 cube containing all 27 voxels.   Its euler char should equal 1 (solid sphere)
In the cc2 the central voxel is removed.            Its euler char should equal 2 (hollow sphere)
In the cc3 two central-faces voxel are removed.     Its euler char should equal 0 (cylinder)
'''

def eulerCheckup():
    c1 = np.array([1,1,1]); c10 = np.array([1,1,2]); c19 = np.array([1,1,3])
    c2 = np.array([1,2,1]); c11 = np.array([1,2,2]); c20 = np.array([1,2,3])
    c3 = np.array([1,3,1]); c12 = np.array([1,3,2]); c21 = np.array([1,3,3])
    c4 = np.array([2,1,1]); c13 = np.array([2,1,2]); c22 = np.array([2,1,3])
    c5 = np.array([2,2,1]); c14 = np.array([2,2,2]); c23 = np.array([2,2,3])
    c6 = np.array([2,3,1]); c15 = np.array([2,3,2]); c24 = np.array([2,3,3])
    c7 = np.array([3,1,1]); c16 = np.array([3,1,2]); c25 = np.array([3,1,3])
    c8 = np.array([3,2,1]); c17 = np.array([3,2,2]); c26 = np.array([3,2,3])
    c9 = np.array([3,3,1]); c18 = np.array([3,3,2]); c27 = np.array([3,3,3])

    cc1 = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14,
        c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27]

    #remove c14: (2,2,2)
    cc2 = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13,
        c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27]

    #remove c5: (2,2,1) and c23: (2,2,3)
    cc3 = [c1, c2, c3, c4, c6, c7, c8, c9, c10, c11, c12, c13,
        c15, c16, c17, c18, c19, c20, c21, c22, c24, c25, c26, c27]

    print('\nEuler Characteristic computation checkup:\n')
    print('The cc1 euler char should equal 1. {} was obtained'.format(euler(cc1)))
    print('The cc2 euler char should equal 2. {} was obtained'.format(euler(cc2)))
    print('The cc3 euler char should equal 0. {} was obtained\n'.format(euler(cc3)))
