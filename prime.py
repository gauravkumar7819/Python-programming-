a=int(input("Enter the number = "))
if(a>1):
    for i in range(2,int(a/2)+1):
        if(a%i==0):
            print(a,"is not a Prime number")
        else:
            print(a,"is a Prime number ")
else:
    print(a,"is not a Prime number")