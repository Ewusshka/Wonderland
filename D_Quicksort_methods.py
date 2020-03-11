# Last element as pivot, places the pivot element at its correct position in sorted
# array. Places all smaller to left of pivot and all greater elements to right of pivot


def partition(arr, low, high):

    i = (low - 1)  # index of smaller element
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot: # if element is smaller than pivot
            i = i + 1 # increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# The main function of QuickSort: arr[] = array, low = Starting index, high = Ending index

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high) # pi is partitioning index, arr[p] is at right place
        quicksort(arr, low, pi - 1) # Sort elements before and after partition
        quicksort(arr, pi + 1, high)