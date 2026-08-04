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



        # print(arr[i],end=" ")
        #

arr1 = [33,44,22,35,23,5]
selection_sort(arr1)
print(arr1)