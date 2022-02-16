num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
print("Which operator will you wish to use?")
ch=input("enter any of the specific operator +,-,*,/:")
result=0
if ch=='+':
    result=num1+num2
elif ch=='-':
    result=num1-num2
elif ch=='*':
    result=num1*num2
elif ch=='/':
    result=num1/num2
else:
    print("Please character is not recognized!")
print(num1,ch,num2,':',result)
