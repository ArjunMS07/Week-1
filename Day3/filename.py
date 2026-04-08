# Declare Variables
user_name = "Arjun"
user_age = 20
user_height = 5.8

# Different Data Types
integer_num = 10
float_num = 10.5
string_text = "Hello"
boolean_val = True

# Check Types
print("Type of user_name:", type(user_name))
print("Type of user_age:", type(user_age))
print("Type of user_height:", type(user_height))
print("Type of integer_num:", type(integer_num))
print("Type of float_num:", type(float_num))
print("Type of string_text:", type(string_text))
print("Type of boolean_val:", type(boolean_val))

# Type Casting
num_str = "25"
converted_int = int(num_str)
print("Converted to int:", converted_int)

num = 50
converted_str = str(num)
print("Converted to string:", converted_str)

# String Formatting
print(f"Hello, my name is {user_name}. I am {user_age} years old and {user_height} feet tall.")

# Input Task
birth_year = input("Enter your birth year: ")
birth_year = int(birth_year)

current_year = 2026
age = current_year - birth_year

print(f"You are {age} years old.")