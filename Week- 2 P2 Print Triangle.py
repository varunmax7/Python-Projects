#Print the below Triangle using for loop

a = int(input("Enter the value"))
for i in range (a, 0, -1):
    for j in range(i, a+1):
        print(i, end=" ")
    print()
