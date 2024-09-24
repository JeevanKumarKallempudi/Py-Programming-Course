"""
Problem : Given an array containing N integers, and an number S denoting a target sum,

Find two distinct integers that can pair up to form target sum. Let us assume there will be only one such pair.

Input:
array = [10,5,2,3,-6,9,11]
S = 4

Output:
[10, -6]
"""
def pairSum(arr, S):
    #Brute Force Approach
    # All pairs
    for i in range (len(arr)-1):
        for j in range(i+1, len(arr)):
            if(arr[i] + arr[j] == S):
                return[arr[i], arr[j]]
    return[]
#Data Structure (Dictionary)
def pairSumhashing(arr, S):
    hashtable = {}
    
    for x in arr:
        y = S - x
        if (y in hashtable):
            return [x,y]
        else:
            hashtable[x] = True
    return []        

#Data Structure (Dictionary)
def pairSumSet(arr, S):
    store = set()
    for x in arr:
        y = S - x
        if y in store:
            return [x, y]
        else:
            store.add(x)
    return []

if __name__ == "__main__":
    array = [3,4,5,-6,12,11,10,14]
    s = 5
print(pairSum(array, s))
print(pairSumhashing(array, s))
print(pairSumSet(array, s))
