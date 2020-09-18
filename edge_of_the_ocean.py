def adjacentElementsProduct(inputArray):
    smax = -1000
    ssum = 0
    for j in range(len(inputArray)-1):
        ssum = inputArray[j] * inputArray[j+1]
        if ssum > smax:
            smax = ssum
    return smax

def shapeArea(n):
    val=1
    for i in range(1,n):
        val += n*2
    return val

def makeArrayConsecutive2(statues):
    statues.sort()
    res=0
    for i in range(len(statues)):
        if i < (len(statues)-1):
            res += (statues[i+1] - statues[i])-1
    return res

