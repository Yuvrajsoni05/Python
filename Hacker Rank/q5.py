num = [1,22,3,4,5,6,7,8,22]
fr = {}
for i in num:
    fr[i] = fr.get(i,0) + 1
print(fr)


def first_non_repeat(text):
    if text in fr:
        return fr[text]
    else:
        return 0



first = first_non_repeat('aaaabbc')
print(first)