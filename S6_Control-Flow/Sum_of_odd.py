'''
Sum of Odd Numbers
You are given with an integer Number N. Your task is to find the sum of all odd numbers from 1 to N (Both inclusive).
Example:
Input: N = 10
Output: 25
Explanation: 1+3+5+7+9 = 25
'''

N = int(input())
odd_sum = 0
for i in range(1, N+1, 2):
    odd_sum += i
print(odd_sum)
