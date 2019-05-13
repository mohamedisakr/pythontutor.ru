n = int(input())
a = [['.' for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:               a[i][j] = '*'
        elif (i+j) == (n -1):    a[i][j] = '*'
        elif (i == n//2):        a[i][j] = '*'
        elif (j == n//2):        a[i][j] = '*'
        else:                    continue

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
