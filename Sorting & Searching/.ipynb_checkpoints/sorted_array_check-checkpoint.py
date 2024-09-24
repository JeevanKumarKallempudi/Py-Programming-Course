def isSorted(arr):
     # Base case: if there's only one or zero elements, it's sorted
    n = len(arr)
    if (n == 1 or n == 0):
        return True
    # Recursive case: check if the first two elements are in order
    # and if the rest of the array is sorted
    if arr[0] <= arr[1] and isSorted(arr[1:]):
        return True
    return False

if __name__ == "__main__":
    arr = [1,2,3,4,6]
    res = isSorted(arr)
    print(res)
    