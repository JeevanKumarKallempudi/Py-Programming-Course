'''
Sum of Digits
You are given with an integer number N. You have to print the sum of each digit of N.
E.g.
Input: N = 2534
Output: 14
Explanation : 2+5+3+4 = 14
'''

N = int(input())

sum = 0
while N != 0:
    sum = sum + (N%10)
    N = N//10
print(sum)