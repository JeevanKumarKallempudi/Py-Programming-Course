# Linear Search Algorithm

def search(arr, key):
    # Code
    n = len(arr)
    for i in range(n):
        if arr[i] == key:
            return i
    return -1

if __name__ == "__main__":
    arr = [1,3,2,5,0,7,8]
    K = 5
    idx = search(arr, K)
    if idx == -1:
        print("Element not present")
    else:
        print(idx)