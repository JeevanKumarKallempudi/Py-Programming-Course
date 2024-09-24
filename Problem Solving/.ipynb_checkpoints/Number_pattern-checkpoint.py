""" 
Print the following pattern
N = 4
1 
2 3
4 5 6
7 8 9 10

Observations : 
Print N rows
Print I numbers in ith row
Values starts at 1, and increases by 1 after every number is printed
"""

def pattern_num(n):
    ##Code starts Here
    val = 1
    #Outer loop - Rows
    for i in range(1, n + 1):
        #Inner loop - print each row
        for j in range(1, i+1):   
            print(val, end=" ")
            val += 1
        print(" ")

if __name__ == "__main__":
    n = int(input())
    pattern_num(n)