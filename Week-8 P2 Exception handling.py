#Week-8 P2
#Exception handling
try:
    a = int(input("Enter First number: "))
    b = int(input("Enter Second number: "))
    c = a/b
    print(c)
except zerodivisionerror:
    print("Denominator should not be zero")
except valueerror:
    print("Enter only integers")
except nameerror:
    print("It should be c value")
else:
    print("Completed")
finally:
    print("Program Done")
