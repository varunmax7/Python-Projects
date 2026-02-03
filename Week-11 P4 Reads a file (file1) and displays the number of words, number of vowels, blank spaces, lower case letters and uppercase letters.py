# Week 11- Program 4
# Reads a file (file1) and displays the number of words, number of vowels, blank spaces, lower case letters and uppercase letters.
with open("file1.txt") as f:
    f1=f.read()
words=1
characters=0
vowels=0
lowercase=0
uppercase=0
digits=0
spaces=0
fullstops=0
for i in f1:
    characters = characters + 1
    if (i ==''):
        words = words + 1
    if (i =='a' or i =='e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i =='E' or i== 'I' or i == 'O' or i =='U'):
        vowels = vowels+1
    if(i.islower()):
        lowercase = lowercase +1
    elif(i.isupper()):
        uppercase=uppercase+1
    elif (i.isdigit()):
        digits = digits + 1
    if (i.isspace()) == True:
        spaces=spaces+1
    elif (i=="."):
        fullstops = fullstops +1
print("--------------------------")
print("File 1 content is as follows: ")
print(f1)
print("--------------------------")
print("Number of words in the string are : ", words)
print("Number of vowels are: ", vowels)
print("The number of lowercase characters are :", lowercase)
print("The number of uppercase characters are : ", uppercase)
print("The number of digit characters are: ", digits)
print("Number of spaces are: ", spaces)
print("The number of fullstops are : ", fullstops)
print("The number of characters are: ", characters)
print("Charcaters after summing up all different types of characters: ", uppercase+lowercase+digits+spaces+fullstops)
