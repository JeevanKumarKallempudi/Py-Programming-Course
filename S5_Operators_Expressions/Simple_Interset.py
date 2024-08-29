'''
Calculate and Print the Simple Interest, given Principal , rate and time.
Simple Interest can be computed using the expression: S.I = (P*R*T)/100
'''

P, R, T = int(input()), int(input()), int(input())

# Code
S_I = (P*T*R)/100
print(S_I)
