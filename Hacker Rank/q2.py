
n = int(input())
arr = list(map(int, input().split()))
print(arr)
highest = max(arr)
while(highest in arr):
    arr.remove(highest)
print(max(arr))