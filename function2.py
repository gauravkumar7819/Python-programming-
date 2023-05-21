'''def add(a,b):
    c=a+b
    print(c)
x=int(input("Enter the number = "))
y=int(input("Enter the number = "))
add(x,y)

def sum(e,f):
    d=e+f
    print(d)
r=print(sum(4,5))
print(r)

def add(x,y):
    return x+y
a=int(input("Enter the number = "))
b=int(input("Enter the number = "))
r=add(a,b)
print(r)
a=int(input("Enter the number = "))
b=int(input("Enter the number = "))

def add():
    return a+b
#print(add())
r=add()
print(r)

def find_max(a,b):
    if a>b:
        return a
    else:
        return b
# Example usage:
x=int(input("Enter the number = "))
y=int(input("Enter the number = "))
max_num = find_max(x,y)
print(f"The maximum of {x} and {y} is {max_num}")

def display(name,Aniket='Kumar'):
    print('Hello', name,Aniket)
display('Aniket')

def display(name, lastname='country'):
    print('Hello', name, lastname)
display('Aniket', 'India')'''

def details(name, rollnumber, mobilenumber):
    student={'name': name,'rollnumber': rollnumber,'mobilenumber': mobilenumber}
    return student
# Taking input from the user
name=input("Enter name: ")
rollnumber=input("Enter roll number: ")
mobilenumber=input("Enter mobile number: ")
# Calling the function with user inputs
student_details=details(name, rollnumber, mobilenumber)
# Printing the student details
print("Name:", student_details['name'])
print("Roll Number:", student_details['rollnumber'])
print("Mobile Number:", student_details['mobilenumber'])


