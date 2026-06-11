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

# print(f"This is memebership 'in' = {'Pali' in city_data}")
# print(f"This is memebership 'not in' = {'Pali' not in city_data}")





# List in python (in JS it's called array)

# What is List in python ?

# List is a mutable data type. We can store multiple items in it like we can do in tuple but in List we can modify it. We can crate List with []. All the key consept is the same as JS array

my_list = ["Sameer","Khan", "Pali", "Rajasthan", True, 26]

# print(f"this is my list {my_list}")
# print(f"this is the first item in my list {my_list[0]}")
# print(f"this is the last item in my list {my_list[-1]}")

# my_list[4] = False
# print(f"my list after mutating item {my_list}")

# my_list.append("India")
# print(f"my list after appending {my_list}")

# my_list.insert(2, "Innu")
# print(f"my list after inserting an item at index 2 {my_list}")

# my_list.remove("Innu")
# print(f"my list after remove an item {my_list}")

# There are more method in List but we go through as we move ahead with learning





# Alising Danger

# Like JS in list also we can't diractly copy a list into a new variable.

my_colors_1 = ['red', 'blue', 'green']

my_colors_2 = my_colors_1

my_colors_2.append('pink')

# print(f"this is my color 2 {my_colors_2}") # output -> ['red', 'blue', 'green', 'pink']
# print(f"this is my color 1 {my_colors_1}") # output -> ['red', 'blue', 'green', 'pink']

# This happen becouse Python just point the my_colors_2 to my_colors_1 memory 


# To prevent this we need to use .copy() method

my_colors_2 = my_colors_1.copy()

my_colors_2.pop()

# print(f"this is my color 2 {my_colors_2}") # Output -> ['red', 'blue', 'green']
# print(f"this is my color 1 {my_colors_1}") # Output -> ['red', 'blue', 'green', 'pink']




# Let's learn about Operator overloading

# What is Operator overloading ?
# When we do 2 + 3 we got 5
# When we do 'Sameer' + ' ' + 'Khan' we got 'Sameer Khan'
# This is called operator overloading in Python.

t_list = [1,2,3] + [4,5,6] # -> [1, 2, 3, 4, 5, 6]
t_list_2 = [1,2,3] * 2 # -> [1, 2, 3, 1, 2, 3]
t_list_3 = [1,2,3] * 2
# print(t_list)
# print(t_list_2)





# Dictionary (Object in JS)

# Today im gonna learn about Dictionary. It's a data structure same like Objact in JS.
# It's a mutable data type

user_profile = {"name": "Sameer",
                "age": 26,
                "city":'Pali',
                'country':'India'}

# print(f"This is user_profile {user_profile}")

# Rules for Dictionary
# 1. Keys should be unique other wise Python overwrite old value
# 2. Keys should be immutable data types like :- String, Int or tuple etc.
# 3. Value can be anything


# Modifying data
user_profile["name"] = "Sameer Khan"
# print(f"This is user_profile {user_profile}")

# print(f"This is user_profile {user_profile['age']}")
# With this approach we have a problem. If Key isn't there in the Dictionary then our Python will crash. To overcome this problem we can use .get() methond.

# print(f"With get method {user_profile.get('age')}")
# print(f"With get method if Key isn't there {user_profile.get('new_age')}")
# print(f"We can throw custom message if Key isn't there {user_profile.get('new_age', 'Not found')}")


# We can add new items in Dictionary like this
user_profile['house_number'] = '192'
# print(f"This is user_profile {user_profile}")


# We can also get Keys, Values and Items and loop over it
# print(f"This is user_profile's Keys {user_profile.keys()}")
# print(f"This is user_profile's Values {user_profile.values()}")
# print(f"This is user_profile's Items {user_profile.items()}")

# for key,value in user_profile.items():
#     print(f"{key} and {value}")

# for item in user_profile.items():
#     print(f"This is item {item}")


# # We have .pop() method to remove items and store in a variable 
# user_name = user_profile.pop("name")

# print(f"This is user name {user_name}")
# print(f"This is user_profile after removing name {user_profile}")

# We can clear whole list with .clear() method
# And we can delete any item without storing in any variable

del user_profile["house_number"]
# print(f"This is user_profile after deleting house number {user_profile}")


# With this we are done with basic data types in python module