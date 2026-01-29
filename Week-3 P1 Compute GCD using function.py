# Compute GCD using function

def computeGCD (x, y):
    if (x > y):
        small = y
    else:
        small = x
    for i in range (1, small + 1):
        if ((x%i == 0) and (y%i == 0)):
            GCD = i
    return GCD
x=int(input("Enter x value: "))
y=int(input("Enter y value: "))
print("The gcd of given number is ")
print(computeGCD (x, y))
