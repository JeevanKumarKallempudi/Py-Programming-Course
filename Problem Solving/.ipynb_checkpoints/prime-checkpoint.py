"""
Is Prime - Write a function to check given number is prime or not?
Input - 11
Output - Yes
"""
def IsPrime(n):
    for i in range (2, n-1):
        if n%i == 0:
            return False
    return True

if __name__ == "__main__":
    n = int(input())
    """
    if (IsPrime(n)):
        print("Yes, it is Prime")
    else:
        print("Not a Prime")
    """
    for i in range(1, n+1):
        if(IsPrime(i)):
            print(i, end=" ")