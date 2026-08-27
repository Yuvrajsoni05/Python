l = [10,20,22,21,223,333]

def second_largest_number(l):
    res = l[0]
    res2 = l[0]
    for i in l:
        if i > res:
            res = i

    for i in l:
        if i > res2 and i != res:
            res2 = i
    return  res2

l2 = [20,20,20]
def second_largest_number_2(l2):
    largest  = None
    second = None
    for i in l2:
        if largest == None or i > largest:
            second = largest
            largest = i
        elif i != largest and (second is None or i > second):
            second= i

        return second
l3 = [1,2,3,4,5]
def missing_number(l3):
    for i in range(1 , len(l3) + 1):
        if i not in l3:
            return i





d3 = missing_number(l3)
print(d3)
d2 = second_largest_number_2(l2)
print(d2)
d = second_largest_number(l)
print(d)

