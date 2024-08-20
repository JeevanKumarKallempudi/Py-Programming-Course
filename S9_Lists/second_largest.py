"""
Second Largest Element
Problem Statement
Given a list (lst) of N Numbers, Print the second largest element if there exists any, otherwise print None
Inputs: List of N elements
Output: Print the Second largest Element if there's any. Otherwise Print None

Sample Cases
Input : [5,2,7,9,3,2,0]
Output : 7

Input : [8,8,8]
Output : None
"""

import sys
lst = [int(i) for i in sys.argv[1].split()]

first = second = float('-inf')

for num in lst:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

if second == float('-inf'):
    print(None)
else:
    print(second)