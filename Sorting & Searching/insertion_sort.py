"""
Insertion Sort --
    Insertion sort is similar to playing cards in our hands.
    Insert the card in its correct position in a sorted part.
"""

def insertionSort(array):
    #Code starts here
    n = len(array)

    for i in range(1,n):

        current_val = array[i]
        prev = i - 1

        while prev >= 0 and array[prev] > current_val:
            array[prev+1] = array[prev]
            prev = prev - 1
        # Current element in the right index (prev +1)
        array[prev + 1] = current_val
    
if __name__ == "__main__":
    array = [10,5,3,4,2,1]
    insertionSort(array)
    print(array)