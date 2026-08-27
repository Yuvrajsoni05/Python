t = int(input())
for _ in range(t):
    n = input()
    # print(len(n))

    if len(n) > 0:
        print(int(n[0]) + int(n[len(n) - 1]))

