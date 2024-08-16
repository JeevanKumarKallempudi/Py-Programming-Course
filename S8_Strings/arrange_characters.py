"""
Arrange characters
You're Given a string st. Arrange the string characters in such a way that lowercase letters should come first. The lowercase and Uppercase letter should be in the same order as in the input string. Print the new string.

Sample Cases:
Inputs : “HellO”
Output = ellHO

Inputs : "WoRLd"
Output : odWRL
"""

st = input()

lower = [char for char in st if char.islower()]
upper = [char for char in st if char.isupper()]
result = ''.join(lower + upper)
print(result)