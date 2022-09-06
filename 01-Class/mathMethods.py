import numpy as np


def calcMean(arr):
    return sum(arr) / len(arr)


def calcMedian(arr):
    arr.sort()
    middleNumber = len(arr) // 2
    if len(arr) % 2 == 0:
        return calcMean(arr[middleNumber - 1:middleNumber + 1])
    else:
        return arr[len(arr) // 2]


def calcTruncateMean(arr, percentage):
    arr.sort()
    var1 = int((len(arr) * percentage) // 2)
    arr = arr[var1:-var1]
    return calcMean(arr)
