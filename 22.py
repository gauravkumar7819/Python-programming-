x = 5
if x > 3 and x < 10:  # the second operand is not evaluated because x > 3 is True
    print("x is between 3 and 10")
if x < 3 or x > 10:   # the second operand is not evaluated because x < 3 is False
    print("x is not between 3 and 10")
