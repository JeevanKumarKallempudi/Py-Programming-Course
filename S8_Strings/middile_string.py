'''
Middle String
You are given a string of odd length greater than equal to 7, print a new string made up of the middle three characters of the given String.
Input : st
Output : middle string

Sample Cases:
Input : "JhonDipPeta"
Output :  Dip

Input  : "JaSonAy"
Output :  Son
'''

st = input()

length = len(st)
mid = length//2

if length < 3:
    pass
else:
    print("{}{}{}".format(st[mid-1],st[mid],st[mid+1]))