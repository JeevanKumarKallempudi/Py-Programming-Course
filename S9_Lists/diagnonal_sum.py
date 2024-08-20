'''
Diagonal Sum
Given a 2D array calculate the sum of its principal diagonal elements.

Sample Cases:
Inputs:  [ [3,7], [0,-2] ]
Output : 1

Explanation : 3 - 2 = 1
Input: [ [1,3,5], [1,4,6], [7,6,9] ]
Output: 14
Explanation : 1 +  4 + 9 = 14
'''

def diagonal_sum(array):
    n = len(array)
    result = 0
    for i in range(n):
        result += array[i][i]
    
    print(result)