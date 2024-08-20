"""
Concatenate Maximum Tuples
Given a list of tuples, where each tuple is (string and its magnitude), 
you have to write a python program to join all the strings with maximum magnitudes.
Example :
Input :  [(“Hello Buddy”, 11), (“sample”, 6), (“to”, 2), (“how are you”, 11)]
Output: “Hello Buddy how are you”
Explanation: 11 is the maximum tuple element and 
concatenation of keys yield this result.
"""
import sys
strings = [ele for ele in sys.argv[1].split(',')]
magnitudes = [int(ele) for ele in sys.argv[2].split()]
 
lst_of_tuples = [(strings[i], magnitudes[i]) for i in range(len(strings))]

# Initialize max_magnitude to a very small number and create a list for strings
max_magnitude = float('-inf')
max_magnitude_strings = []
# Iterate through the list to find the maximum magnitude
for string, magnitude in lst_of_tuples:
    if magnitude > max_magnitude:
        max_magnitude = magnitude
        max_magnitude_strings = [string]  # Start a new list with this string
    elif magnitude == max_magnitude:
        max_magnitude_strings.append(string)  # Add the string to the existing list
# Join the strings with space separator
result = ' '.join(max_magnitude_strings)

print(result)
