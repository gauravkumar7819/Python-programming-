import random
x = int(input(""))
c = random.randint(1, 100)
if x < c:
    print("Number is Two low")
elif x > c:
    print("Number is to high")
elif x == c:
    print("You gussed")