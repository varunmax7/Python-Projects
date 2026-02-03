#Week10- Program 2
# Phone No. and Email Validation
phno=input("enter number:")
email=input("enter email id:")
if((len(phno)==10)and(phno[0]=='6'or'7'or'8'or'9')):
    print('given number is valid')
else:
    print('given number is invalid')
substr='@email.com'
result=email.find(substr)
if(result==-1):
    print('invalid email')
else:
    print('valid email')
