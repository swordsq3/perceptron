import numpy as np

from ..perceptron.node import hi

AND = (1, 1, 1)
NAND = (-0.5, -0.5, -0.7)
OR = (0.5, 0.5 , -0.2)


LL =[]
ii = []
for LOGIC in [AND, NAND, OR]:
    for POINT in [[0,0], [1, 0], [0, 1], [1, 1]]:
        LL.append(hi(POINT, LOGIC))
    
    ii.append(LL)
    LL = []
        
print(ii)