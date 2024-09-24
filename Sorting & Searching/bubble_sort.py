"""
What is sorting ??

Unsorted Array : [10,12,5,4,1,3,2]
Sorted Array (Increasing Order):
    a = [1,2,3,4,5,10,12]
Sorted Array (Decreasing Order):
    a = [12,10,5,4,3,2,1]

Bubble Sort: 
Key Idea : Take larger element to the end by repeatedly swapping adjacent elements.

"""

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

def bubbleSort(array):

    n = len(array)
    for items in range(n-1):
        for j in range (n-items-1):
            if array[j] > array[j+1]:
                swap(j, j+1, array)

if __name__ == "__main__":
    array = [10,12,5,4,1,3,2]
    bubbleSort(array)
    print(array)