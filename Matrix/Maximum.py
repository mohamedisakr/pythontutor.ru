n , m = [int(i) for i in input().split()]   #int(input()) , int(input()) # rows , # cols
a = [[int(j) for j in input().split()] for i in range(n)]
largest = a[0][0]
row_index = 0
col_index = 0
for i in range(n):
    for j in range(m):
        if a[i][j] > largest:
            largest = a[i][j]
            row_index = i
            col_index = j
print(row_index, col_index, end=' ')
