'''
Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
'''

def celcius2fahr(cel):
    return int((cel * 9/5) + 32)

def fahr2celcius2(fah):
    return int((fah - 32) * (5/9))

if __name__ == "__main__":
    print("Enter the temparature in Celcius")
    t1 = int(input())
    print("Enter the temparature in fahrenheit")
    t2 = int(input())

    print("Celcius {} in fahrenheit is {}".format(t1, celcius2fahr(t1)))
    print("fahrenheit {} in Celcius is {}".format(t2, fahr2celcius2(t2)))