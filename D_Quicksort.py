from D_Quicksort_methods import quicksort, partition

arr = [int(x) for x in input("Write integers (divided by space) to order: ").split()]
n = len(arr)
quicksort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])