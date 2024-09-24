"""
Write a function that takes input an array of distinct integrers and returns the length of highest mountain
    -> A mountain is defined as adjacent integers that are strictly increasing until they reach a peak, at which becomes strictly decreasing.
    -> At lease 3 numbers are required to form a mountain

Input: [5,6,1,2,3,4,5,4,3,2,0,1,2,3,-2,4]
Output : 9
"""

def mountain(arr):
    # Code
    ans = 0
    i = 1
    while i < len(arr) - 1:
        isPeak = arr[i] > arr[i-1] and arr[i+1] < arr[i]
        if isPeak:
            cnt = 1
            # go backward
            j = i
            while j>0 and arr[j-1] < arr[j]:
                cnt += 1
                j -= 1
            #go forward
            j = i
            while j < len(arr) - 1 and arr[j] > arr[j+1]:
                cnt += 1
                j += 1

            #bredth of mountains
            ans = max(cnt, ans)
            i = j
        else:
            i += 1
    return ans

if __name__ == "__main__":
    array = [5,6,1,2,3,4,5,4,3,2,0,1,2,3,-2,4]
    print(mountain(array))