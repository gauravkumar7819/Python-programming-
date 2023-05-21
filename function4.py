'''def display():
    global a
    a=15
    print("Inside function", a)
a=20
print('Before function call', a)
display()
print("after function call",a)'''
def display():
    a=15
    print("Inside Function", a)
    def d1():
        a=70
        print("Nested Function",a)
    d1()
a=100
print("Before Function call",a)
display()
print("After function call",a)