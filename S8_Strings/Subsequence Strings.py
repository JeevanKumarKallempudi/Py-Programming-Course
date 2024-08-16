"""
Subsequence Strings
You're Given 2 strings s1 and s2. You have to check if s1 is a subsequence of s2.
Subsequence means - if all the characters of string s1 appear in the string s2. S2 can have more or equal numbers of characters.

Sample Cases:
Inputs :
s1 = "cdngmutes"
s2 = "coding minutes"
Output = True

Inputs :
s1 = "cdng python"
s2 = "coding minutes"
Output : False
"""

s1, s2  = input(), input() 

i, j = 0, 0
len_s1 = len(s1) 
len_s2 = len(s2)

while i < len_s1 and j < len_s2:
    if s1[i] == s2[j]:
        i += 1
    j += 1

is_subsequence = (i == len_s1)

print(is_subsequence)
