n  = int(input())
l1 = []
for i in range(0,n):
    vc = input().split()

    if vc[0] == 'insert':
        l1.insert(int(vc[1]), int(vc[2]))
    elif vc[0] == 'remove':
        l1.remove(int(vc[1]))
    elif vc[0] == 'print':
        print(l1)
    elif vc[0] == 'append':
        l1.append(int(vc[1]))
        print(l1)
    elif vc[0] == 'pop':
        l1.pop()
        print(l1)
    elif vc[0] == 'reverse':
        l1.reverse()
        print(l1)
    elif vc[0] == 'sort':
        l1.sort()
        print(l1)
