"""
Write a Python program to find those numbers 
which are divisible by 7 and multiples of 5, 
between 1500 and 2700 (both included).
"""

def numberDivideby7Multiplyby5():
    # Empty list to store the numbers
    n = []
    # # Iteratinng through numbers from 1500 to 2700
    for num in range (1500, 2701):
        # Checking the condition
        if(num % 7 == 0) and (num % 5 == 0):
            # If condition met, storing the number as string in list
            n.append(str(num))
    # joining the numbers with comma separated.
    print(','.join(n))
    return 0

if __name__ == "__main__":
   numberDivideby7Multiplyby5()