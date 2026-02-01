#Week-6 P5 String of the ame length
def alternate_string(s1, s2):
    newstring=''
    if len(s1)==len(s2):
        print("The two strings are of same length, the string altered string is")
        for i in range(len(s1)):
            newstring=newstring+s1[i]+s2[i]
    else:
        print("The two string are not of same length")
    return newstring
string1=input("Enter string1: ")
string2=input("Enter string2: ")
print(alternate_string(string1, string2))
