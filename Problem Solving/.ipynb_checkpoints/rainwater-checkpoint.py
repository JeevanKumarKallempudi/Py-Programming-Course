"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how mach water it can trap after raining.

Input = [0,1,0,2,1,0,1,3,2,1,2,1]

Output = 6

"""

def rainwater(array):
    #Code
    n = len(array)
    if n<=2:
        return 0

    left = [0 for x in array]
    right = [0 for x in array]

    left[0] = array[0]
    right[n-1] = array[n-1]
    for i in range(1,n):
        left[i] = max(left[i-1], array[i])
        right[n-i-1] = max(right[n-i], array[n-i-1])

    #Water calu
    water = 0
    for i in range (n):
        water += min(left[i], right[i]) - array[i]
    return water

if __name__ == "__main__":
    arr = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(rainwater(arr))