# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.


# sample input: 10

# sample output: 35

#solution
add_func = lambda num:num + 25
number = int(input("Enter a number:"))
print(add_func(number))