x = int(input("enter Value x :"))
y = int(input("enter Value y :"))

z = int(input("enter Value z :"))
n = int(input("enter value n :"))

final_list = []
for a in range(x + 1):
    for b in range(y + 1):
        for c in range(z + 1):
            final_list.append([a,b,c])
print(final_list)
