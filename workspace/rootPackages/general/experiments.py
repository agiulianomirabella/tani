import numpy as np
from rootPackages.globalTopology.edgeDetection import extractEdges

a = np.array([
    [0,0,0],
    [0,1,0],
    [0,0,0]
])

b = np.array([a for _ in range(3)])

image = a
print(np.ones(3))

