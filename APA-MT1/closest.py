def findClosestValueIndex(arr, val):
    dif = 0
    closest = 1000
    if (arr == []):
        return -1
    else:
        for x in arr:
            dif = abs(val-x)
            if (dif < closest):
                closest = dif
        return dif
            
        