a=int(input("Enter the number = "))
if((a%3==0) & (a%7==0)):
    print("The number is divisible by 3 and 7")
if((a%3==0) & (a%7!=0)):
    print("The number is not divisible by 7")
if((a%3!=0) & (a%7==0)):
    print("The number not is divisible by 3 ")

