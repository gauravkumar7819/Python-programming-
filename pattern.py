# num_rows = int(input("Enter the number of rows: "))
# for i in range(num_rows):
#     for j in range(i+1):
#         print("*", end="")
#     for k in range(2*num_rows-2*i-2):
#         print(" ", end="")
#     for j in range(i+1):
#         print("*", end="")
#     print()
my_list = [1, 2, 3]
last_element = my_list.pop()
print(last_element) # prints 3
second_element = my_list.pop(1)
print(second_element) # prints 2
