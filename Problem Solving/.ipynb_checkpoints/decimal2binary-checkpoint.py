"""
Convert a number from decimal format into binary format
Input : N = 10
Output = 1010
"""

def decimal2binary(n):
    ans = 0
    p = 1
    while n > 0:
        rem = n%2
        ans = ans + rem * p
        p = p*10
        n = n//2
    return ans

def decimal2BinaryBitwise(n):
    ans = 0
    p = 1
    while n > 0:
        lst_bit = n & 1
        ans = ans + lst_bit *p
        p = p * 10
        n = n >> 1

    return ans

if __name__ == "__main__":
    n = int(input())
    print(decimal2binary(n))