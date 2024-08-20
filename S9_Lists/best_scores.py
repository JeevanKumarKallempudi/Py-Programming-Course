"""
Best Scores
From a class of n students, you are given marks of students who appeared in a test. Two or more students can have the same marks. Print the highest and second-highest marks in the class.
Sample Cases:
Input : [78, 86, 66, 81, 66, 81, 50, 81, 23, 45, 79, 62, 86, 33]
Output :
86
81
"""

import sys
lst = [int(i) for i in sys.argv[1].split(',')]

highest = second_highest = float('-inf')

for marks in lst:
    if marks > highest:
        second_highest = highest
        highest = marks
    elif marks > second_highest and marks != highest:
        second_highest = marks

print(highest)
print(second_highest)