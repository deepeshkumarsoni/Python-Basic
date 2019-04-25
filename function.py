#Basic Function
def function():
    print('Hello World')
function()

#Bydefault argument name given do not show error when argument not given
def fun(name='Deepesh'):
    print(name)
fun()
fun('Mohan')
fun()
fun('Ram')

#Function to Add 2 No's
def add(a,b):
    return(a+b)
print('The Addition of Two No is :',add(10,20))

#function to print square
def square(a):
    print('Square of Given No is :',a**2)
square(int(input('Enter No to check its Square :')))

#Taking User Input check Whether No is odd/even
def check(a):
    if a%2==0:
        print('Given No is Even')
    else:
        print('Given No is Odd')

check(int(input('Enter the No :')))
