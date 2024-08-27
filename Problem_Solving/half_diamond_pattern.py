"""
Print the following pattern for a given N
N = 4

    *
   * * *
 * * * * *
* * * * * * *
Rows    Spaces    Stars
  1       3         1
  2       2         3
  3       1         5
  4       0         7
  i      N - i    
"""

def diamondPattern(n):
    # print N rows
    for i in range (1, n+1):
        # N - i row spaces
        for space in range (0, n - i):
            print(" ", end="")
            
        # 2*i - 1 starts
        for star in range(0, 2 * i -1):
            print("*",end="")
        #new line
        print()

def diamondPattern2(n):
    # print N rows
    for i in range (1, n+1):
        # N - i row spaces
            print(" "*(n - i), end="") 
        # 2*i - 1 starts
            print("*" * (2 * i -1),end="")
        #new line
            print()

if __name__ == '__main__':
    n = int(input())
    diamondPattern2(n)