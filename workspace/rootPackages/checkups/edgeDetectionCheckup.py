import numpy as np
from rootPackages.globalTopology.edgeDetection import extractEdges
from rootPackages.connectedComponent.cell import dim

'''
This module is intended to verify the reliability of the edge detection function

The expected output is:

0-cells:
[1.5 3.5]
[-0.5  2.5]
[2.5 1.5]
[0.5 3.5]
[-0.5  3.5]
[2.5 4.5]
[1.5 2.5]
[2.5 5.5]
[1.5 5.5]
[-0.5  4.5]
[0.5 4.5]
[2.5 2.5]
[4.5 1.5]
[-0.5  0.5]
[-0.5 -0.5]
[ 0.5 -0.5]
[0.5 0.5]
[3.5 2.5]
[1.5 4.5]
[-0.5  5.5]
[0.5 5.5]
[2.5 3.5]
[ 1.5 -0.5]
[1.5 0.5]
[4.5 2.5]
[3.5 1.5]
[ 2.5 -0.5]
[2.5 0.5]
[0.5 2.5]

1-cells:
[1.  3.5]
[0.  2.5]
[-0.5  3. ]
[2.5 4. ]
[2.  5.5]
[1.  2.5]
[2.5 5. ]
[1.  5.5]
[0.5 4. ]
[-0.5  4. ]
[2.  2.5]
[2.5 2. ]
[4.  1.5]
[3.  2.5]
[ 0.  -0.5]
[-0.5  0. ]
[0.  0.5]
[1.  4.5]
[1.5 4. ]
[-0.5  5. ]
[0.  5.5]
[2.5 3. ]
[ 1.  -0.5]
[1.  0.5]
[4.  2.5]
[4.5 2. ]
[3.  1.5]
[ 2.  -0.5]
[2.  0.5]
[2.5 0. ]
'''

def edgeDetectionCheckUp():
    image = np.array([
        [1,0,0,1,1,1],
        [1,0,0,1,3,1],
        [1,0,0,1,1,1],
        [0,0,2,0,0,0],
        [0,0,2,0,0,0]
    ])

    print('\nObtained output:\n')
    edges = extractEdges(image)

    print('0-cells:')
    for i in edges:
        if dim(i) == 0:
            print(i)

    print('\n1-cells:')
    for i in edges:
        if dim(i) == 1:
            print(i)
    print()

