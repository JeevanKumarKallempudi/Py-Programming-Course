"""
-- Selection Sort --
Key Idea : Repeatedly find the minimum element from unsorted part and putting it 
at the beginning

"""
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
    
def selectionSort(array):
    n = len(array)
    for idx in range(0, n-1):
        current_ele = array[idx]
        min_idx = idx

        for j in range(idx, n):
            if(array[j] < array[min_idx]):
                min_idx = j
        swap(min_idx, idx, array)

if __name__ == "__main__":
    array = [10,12,5,4,1,3,2]
    selectionSort(array)
    print(array)