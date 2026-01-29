# Program for Lower case or Upper case character or a Special Character

ch = input("Enter the Digit or Letter or Special Character: ")
if (ord(ch) >= 65 and ord(ch) <= 90):
    print("Uppercase character")
elif(ord(ch) >= 97 and ord(ch) <= 122):
    print("Lowercase character")
elif(ord(ch) >= 48 and ord(ch) <= 57):
    print ("Digit")
else:
    print("Special Char")
