# num = [1,22,3,4,5,6,7,8,22]
# fr = {}
# for i in num:
#     fr[i] = fr.get(i,0) + 1
# print(fr)


def first_non_repeat(text):
    co = {}
    for i in text:
        # print(i)


        co[i]  = co.get(i, 0) + 1
    for i in text:
        if co[i] == 1:
            return i





first = first_non_repeat('aaaabbc')
print(first)