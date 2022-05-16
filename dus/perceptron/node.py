def hi(xx, dd):
    return 1 if xx[0]*dd[0] + xx[1]*dd[1] > dd[2] else 0

if __name__ =="__main__":
    AND = (1, 1, 1)
    NAND = (-0.5, -0.5, -0.7)
    OR = (0.6, 0.6 , 1)


    LL =[]
    ii = []
    for LOGIC in [AND, NAND, OR]:
        for POINT in [[0,0], [1, 0], [0, 1], [1, 1]]:
            LL.append(hi(POINT, LOGIC))
        
        ii.append(LL)
        LL = []
            
    print(ii)