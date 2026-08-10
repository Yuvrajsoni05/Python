l1 = [1,34,56,78,99,11]


def insertion_sort(l):

    n = len(l)
    for i in range(1,n):
        k  = l[i]
        j = i-1
        while j >= 0 and k < l[j]:
            l[j+1] = l[j]
            j -= 1
            print(l[j])
            l[j+1] = k








insertion_sort(l1)
print(l1)