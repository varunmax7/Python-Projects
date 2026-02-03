#Week 11-Program 2
# Open file and find given word
with open("file1.txt") as f:
    f1=f.read()
    f2=f1.lower().replace('.','').split()
print("-----------------------")
print("File 1 content is as follows: ")
print(f1)
print("-----------------------")
print("File 1 content after splitting will look like as follows: ")
print(f2)
print("-----------------------")
x=input("enter the word to search :" ).lower()
if (x in f2):
    print("word found")
else:
    print("word not found")
