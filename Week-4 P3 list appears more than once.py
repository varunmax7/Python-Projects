#Week-4 P3
def has_duplicate(anylist):
    if len(anylist)!= len(set(anylist)):
        return True
    else:
        return False
mylist = [5, 3, 5, 2, 1, 7, 6, 4]
print(mylist)
if has_duplicate(mylist):
    print("duplicate is found in list")
else:
    print("no duplicates found in list")
