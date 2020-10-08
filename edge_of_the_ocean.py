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

def almostIncreasingSequence(sequence):
    removed_one = False
    prev_maxval = None
    maxval = None
    for s in sequence:
        if not maxval or s > maxval:
            prev_maxval = maxval
            maxval = s
        elif not prev_maxval or s > prev_maxval:
            if removed_one:
                return False
            removed_one = True
            maxval = s
        else:
            if removed_one:
                return False
            removed_one = True
    return True

def matrixElementsSum(matrix):
    skipcol = [-1]*5
    skipsize=0
    total=0
    for i in range(len(matrix)):
         for j in range(len(matrix[0])):
             if(j not in skipcol):
                 if(matrix[i][j] == 0):
                     skipcol[skipsize] = j
                     skipsize+=1
                 total += matrix[i][j]
    return total
