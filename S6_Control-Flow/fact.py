'''
Factorial of a Number
You're given a number n . You have to print the factorial of n.
Factorial of N = N * N-1 * N-2 * . . .  * 1

E.g
Input: N = 5
Output : 120
Explanation
5*4*3*2*1= 120
'''

N = int(input())

fact = 1
for i in range(1, N+1):
    fact *= i

print(fact)
