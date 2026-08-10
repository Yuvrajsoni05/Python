n = 5
mat  = [[0] * n for _ in range(n)]
top = 0
bottom = n - 1
left = 0
right = n - 1
ma = 1

while top <= bottom and left <= right:
    for i in range(left,right+1):
        mat[top][i] = ma
        ma += 1
    top += 1

    for i in range(top, bottom+1):
        mat[i][right] = ma
        ma += 1
    right -= 1

    if top <= bottom:

        for i in range(right, left-1, -1):
            mat[bottom][i] = ma
            ma += 1
        bottom -= 1

    if left <= right:
        for i in range(bottom, top-1, -1):
            mat[i][left] = ma
            ma += 1
        left += 1



for row in mat:
    print(row)