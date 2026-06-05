print("hello this is data type module")

# Numbers, Floats, Strings, Bool, Sets, Tople's are immutable

# Numbers and Floats

num_a = 5

# print(f"this is num_a")
# print(f"this is num_a's Id {id(num_a)}")

num_a = 6

# print(f"this is num_a after change")
# print(f"this is num_a's Id after change {id(num_a)}")



num_float = 1.5

# print(f"Float number {num_float}")



# If we perform a divison then result always come in float number

# print(f"10 divide by 2 with true divison {10 / 2}")
# print(f"10 divide by 2 with floor divison {10 // 2}")

# print(f"abs method give us absolute value for ex. -10 with abs() is {abs(-10)}")

# print(f"Round method {round(14.77777834, 3)}")


# String

# name = "sameer"

# print(f"first letter of name {name[0]}")
# print(f"last letter of name {name[-1]}")
# print(f"total 'e' letter in name {name.count("e")}")
# print(f"name with uppercase {name.upper()}")
# print(f"name with titlecase {name.title()}")

# print(f"name slicing {name[0:4]}")
# print(f"name slicing {name[::2]}")
# print(f"name slicing {name[0:4:2]}")


# print(f"replace word e with h {name.replace('e', 'h')}")
# print(f"finding index of substring mee {name.find('mee')}")
# print(f"spliting name into an array/list {name.split('e')}")



# Let's learn about tuple

# 1. tuple is immutable. We can't modify it after it created in memory

# first_tuple = ('sameer', 'khan', 26, True)

# print(f"this is first tuple {first_tuple}")
# print(f"We can access single item {first_tuple[2]}")
# # print(f"If we access item far more then it's index we got IndexError {first_tuple[6]}")
# print(f"-1 always give us last items {first_tuple[-1]}")



# # 2. Without ',' (comma) Python treat value as a string

# tuple_1 = ('sameer') # It's treated like a string
# tuple_2 = ('sameer',)

# print(f"this is without comma ',' = {tuple_1}")
# print(f"this is with comma ',' = {tuple_2}")



## Membership in Python (in or not in)

city_data = ("Pali", "Rajasthan", "India")

# city,state,country = city_data

# print(f"We can destructure items in variables = {city}, {state}, {country}")

print(f"This is memebership 'in' = {'Pali' in city_data}")
print(f"This is memebership 'not in' = {'Pali' not in city_data}")