n , m = [int(x) for x in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
i , j = [int(x) for x in input().split()]

def swap_columns(a, i, j):
    for row in range(n):
        a[row][i], a[row][j] = a[row][j], a[row][i]
    
swap_columns(a, i, j)

for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()
