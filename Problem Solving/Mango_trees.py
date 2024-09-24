"""
Rahul's father has left a farm organized as an N x N drid.
Each square in the grid either has or does not have a mango tree.
He has to divide the farm with his three sisters as follows: 
he will draw one horizontal line and one vertical line to divide the 
field into four rectangles. His sisters will choose three of of the four 
smaller filelds and he gets the last one.

Input                 Output    
. # # . . .          . # | # . . .
# . . # # .          # . | . # # .
. # . . . .          . # | . . . .
                    -----+---------
. # # . . #          . # | # . . #
# . . # # .          # . | . # # .
. # . . . .          . # | . . . .

Goal : Maximum number of trees that rahul can get. (maximize his minimum)

Make a cut at every i,j and find the sum of each quadrant
    -> Compute S1,S2,S3,S4 ==> X
    -> Keep tarck of max X
    ==> O(N4) times

using concept of - 2D Prefix Sums

Let M[x,y] be the number of mango trees in the rectangle between (0,0) and (x,y).
We can calculate M[x,y] as follows:
    M[x,y] = 1 + M[x-1, y] + M[x, y-1] - M[x-1, y-1], if tree at (x,y)
    = 0 + M[x-1, y] + M[x, y-1] - M[x-1, y-1], if no tree at (x,y)
----------------------------------------------------------------------------------
To right rectangle:
    M[N,y] - M[x-y] : Number of mango trees in rectangle defined by (x,y) and (N,0)
Bottom Left rectangle
    M[x,N] - M[x-y] : Number of mango trees in rectangle defined by (0,N) and (x,y)
"""




