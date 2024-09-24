def factorial(n):
    #base case
    if n==0:
        return 1
    # recursive case
    ans = n * factorial(n-1)
    return ans

if __name__ == "__main__":
    n = int(input())
    print(factorial(n))