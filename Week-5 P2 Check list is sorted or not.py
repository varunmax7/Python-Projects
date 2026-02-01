#Week-5 P2 Check list is sorted or not
def invertdictcontent(dict1):
    dict2={}
    for i, j in dict1.items():
        dict2[j]=i
    return dict2
n = int(input("Enter the number of elements in dictonary= "))
dict1={}
for i in range(n):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    dict1[key]=value
print(dict1)
print(invertdictcontent(dict1))
