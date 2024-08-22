"""
Symmetric Difference of Multiple sets
Symmetric Differences among groups of sets are elements \ 
that belong to any one of the sets but are not present in any other set. 
Given a list of multiple sets  the task is to write a Python program \ 
to get the symmetric difference of the same.

Input :  = [{5, 3, 2, 6, 1}, {7, 5, 3, 8, 2}, {9, 3}, {0, 3, 6, 7}]
Output : {8, 1, 9, 0}
Explanation: 8, 1, 9, 0 occurs in just one set among all the sets.
Input : test_list = [{2, 6, 0}, {7, 5, 3, 2}, {5, 4, 3, 6}]
Output : {0, 4, 7}
"""

N = int(input())
lst_of_sets = [{int(e) for e in input().split()} for i in range(N)]

# Write your code here
result = lst_of_sets[0]

for s in lst_of_sets[1:]:
        result = result.symmetric_difference(s)
print(result)
# Code ends here