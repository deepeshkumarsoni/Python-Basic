def add(a,b):
    print('First No. is :',a)
    print('Second No. is :',b)
    print("Addition of A & B is :",a+b)
def sub(a,b):
    print('First No. is :', a)
    print('Second No. is :', b)
    print("Subtraction of A & B is :", a - b)
def mul(a,b):
    print('First No. is :', a)
    print('Second No. is :', b)
    print("Multiplication of A & B is :", a * b)
def div(a,b):
    print('First No. is :', a)
    print('Second No. is :', b)
    print("Division of A & B is :", a // b)

d=int(input('Enter 1st No. :'))
e=int(input('Enter 2nd No. :'))
print('\nEnter 1 for Addition')
print('Enter 2 for Substraction')
print('Enter 3 for Multiplication')
print('Enter 4 for Division')
c=int(input('Enter Your Choice :'))
if c==1:
    add(d,e)

elif c==2:
    sub(d,e)

elif c==3:
    mul(d,e)

elif c==4:
    div(d,e)

else:
    print("Invalid choice Entered")