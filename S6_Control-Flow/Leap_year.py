'''
Check a Leap Year?
In this question, you have to check whether the input year is a leap year or not?
E.g.
Input - 2017
Output - Not a leap year

Input - 2012
Output - Leap year
'''

import sys
year = int(input())

# Write your code here
if ( (year % 400 == 0) and (year % 100 == 0)):
    print("Leap year")
elif ((year % 4 == 0) and (year % 100 != 0)):
    print("Leap year")
else:
    print("not a leap year")
# Code end