a=int(input("Enter the number of Rows = "))
for i in range(a+1,1,-1):
    for j in range(1,i):
        print("*",end=" ")
    print()