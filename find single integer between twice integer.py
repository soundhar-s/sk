def findSingle( ar, n):
    res = ar[0]
    for i in range(1,n):
        res = res ^ ar[i]
    return res
ar = [2, 3, 5, 4, 5, 3, 4]
print("Element occuring once is", findSingle(ar, len(ar)))

