num1=int(input('enter first number: '))
num2=int(input('enter second number: '))
num3=int(input('enter third number: '))
num4=int(input('ente fourth number: '))
# if(num1>num2 and num1>num3 and num1>num4):
#     print('greatest number is:',num1)
# elif(num2>num1 and num2>num3 and num2>num4):
#     print('greatest number is : ',num2)
# elif(num3>num1 and num3>num2 and num3>num4):
#     print('greatest number is :',num3)
# else:
#     print('greatest number is :',num4)
if(num1>num2):
    f1=num1
else:
    f1=num2

if(num3>num4):
    f2=num3
else:
    f2=num4

if(f1>f2):
    print(str(f1)+' is the greatest')
else:
    print(str(f2)+' is the greatest')
