"""
Write a function that searches for an element in row wise and column wise
sorted 2D array
"""

def staircaseSearch(mat, m, n, key):
    i = 0
    j = n - 1

    while(i < m and j>=0):
        if(mat[i][j] == key):
            return(i, j)
        elif mat[i][j] > key:
            j -= 1
        else:
            i += 1
    return -1


if __name__ == "__main__":
    mat =[[10,20,30,40],
    	  [15,25,35,45],
    	  [27,29,37,48],
    	  [32,33,39,50]]
    
    m,n = 4,4
    key = int(input())
    result = staircaseSearch(mat, m, n, key)
    if result == -1:
        print(key, "not Found")
    else:
        print(result)