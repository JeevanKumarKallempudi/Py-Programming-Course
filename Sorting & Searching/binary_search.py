"""
Binary Search
Efficient searchong algorithm to find the index of element in a given sorted array.

arr = {1,2,10,11,19,29,30}
key = 19

start = 0
end = n-1
while (s<=e):
    find mid
    do compare at mid
        - equal to mid
        - greater
        - less
    return mid
return -1
"""

def binarySearch(arr, x):
    s = 0
    e = len(arr) - 1
    while s <= e:
        mid = (s+e)//2

        if arr[mid] < x :
            s = mid + 1
        elif arr[mid] > x:
            e = mid -1
        else:
            return mid
    return -1


if __name__ == "__main__":
    arr = [1,2,10,11,19,29,30]
    x = int(input())

    idx = binarySearch(arr,x)
    if idx == -1:
        print("Element is not present")
    else:
        print("Element is preset at", str(idx))
    