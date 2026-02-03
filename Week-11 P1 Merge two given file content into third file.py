# Week11- Program 1
# Merge two given file content into third file
with open("file1.txt") as F1:
    f1=F1.read()
with open("file2.txt") as F2: 
    f2=F2.read()
with open("file3.txt","w") as F3:
    f3=f1+f2
    F3.write(f3)
print("------------------------")
print("File 1 content is as follows: ")
print(f1)
print("------------------------")
print("File 2 content is as follows: ")
print(f2)
print("------------------------")
print("File 3 content is as follows: ")
print(f3)
print("-------------------------")

