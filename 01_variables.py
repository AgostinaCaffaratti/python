# Variables

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Variable concatenation in a print
print(my_string_variable, str(my_int_variable) , my_bool_variable)
print('this is the value of:', my_string_variable, 'and the value of:', my_int_variable, 'and the value of:', my_bool_variable)

# Some system functions
print(len(my_string_variable))

# Variables in a single line
name, surname, alias, age = "Agostina", "Caffaratti", "gostu", 25
print("My name is:", name, surname, "my age is:", age, "and my alias is:", alias)

# Inputs
name = input("What is your name? ")
age = input("How old are you? ")

print(name)
print(age)

# Changing type
name = 25
age = "Agostina"

print(name)
print(age)

# Forcing the type?
address: str = "My address"
address = 32
print(type(address))






