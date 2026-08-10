l1  = [11,52,32,54,5,6,75,158,95]
def bubble_sort(l):
    n = len(l)

    for i in range(n):
        print(l[i])
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]











bubble_sort(l1)
print(l1)