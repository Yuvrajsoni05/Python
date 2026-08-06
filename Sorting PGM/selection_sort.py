def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        # print("not mini")
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
                # print("mini ",arr[min_index])
        arr[i], arr[min_index] = arr[min_index], arr[i]


def bubble_sort(arr2):
    n = len(arr2)
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if arr2[j] > arr2[j+1]:
                arr2[j], arr2[j+1] = arr2[j+1], arr2[j]



        # print(arr[i],end=" ")
        #

arr1 = [33,44,22,35,23,5]
arr2 = [33,44,22,35,23,5]
selection_sort(arr1)
bubble_sort(arr2)
print(arr2)
print(arr1)