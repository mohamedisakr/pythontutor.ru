n = int(input())
a = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        if (i+j) == (n-1):      a[i][j] = 1
        elif (i+j) > (n-1):     a[i][j] = 2        
                    
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
