#Week-7 P3
#Multiplication of two square matrices
a=[[1, 2, 3], [2, 3, 4], [3, 4, 5]]
b=[[5, 4, 3], [4, 3, 2], [3, 2, 1]]
result=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j]+=a[i][k]*b[k][j]
for r in result:
    print(r)
