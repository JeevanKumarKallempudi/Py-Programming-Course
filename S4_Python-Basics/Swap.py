'''
Swap two numbers
You are given 2 variables num1 & num2 . You have to swap the values of these variables, 
such that the value of the variable num1  comes to variable num2 , and value of num2 comes to num1.
E.g. num1 = 5 num2 = 10
After swapping,
num1 is 10, and num2 is 5
'''

num1, num2 = input(), input()

#Code starts here
num1, num2 = num2, num1
print(num1, num2)