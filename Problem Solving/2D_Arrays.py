"""
2D Array
"""
def main():
    R = int(input())
    C = int(input())
    mat = [[int(input()) for x in range(C)] for row in range(R)]

    print(mat)

def printMat(mat):
    rows = len(mat)

    for i in range(rows):
        for j in range(len(mat[i])):
            print(mat[i][j], end=" ")
        print()

def array2D():
    # 2D Array Input/Output
    
    R = int(input())
    C = int(input())
    mat = []
    #Scan the IP for each row
    for i in range(R):
        row = [int(x) for x in input().split()]
        mat.append(row)
    #print(mat)
    printMat(mat)



if __name__ == "__main__":
    # array2D()
    main()
    