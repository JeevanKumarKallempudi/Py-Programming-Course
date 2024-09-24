# Problem : Find the first repeating character in a string

def fisrtRepeatingChar(str):
    # Code
    table = {}
    for char in str.lower():
        if char in table:
            table[char] += 1
            return char
        elif char!= " ":
            table[char] = True
    return


if __name__ == "__main__":
    string = input()
    print(fisrtRepeatingChar(string))