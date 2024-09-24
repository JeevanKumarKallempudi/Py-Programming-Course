def ladder(n):
    #Base Case
    if n==0:
        return 1
    if n < 0:
        return 0
    
    #Recursive case
    ans = ladder (n-1) + ladder(n -2) + ladder(n-3)
    return ans

if __name__ == "__main__":
    n = int(input())
    print(ladder(n))