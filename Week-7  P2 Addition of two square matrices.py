#Week-7 P2
#Addition of two square matrices
a = [[1, 2, 3],[2, 4, 6], [4, 5, 6]]
b = [[3, 6, 9], [4, 6, 8], [7, 8, 9]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        result[i][j]=a[i][j]+b[i][j]
for s in result:
    print(s)
    
