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

name = "sameer"

print(f"first letter of name {name[0]}")
print(f"last letter of name {name[-1]}")
print(f"total 'e' letter in name {name.count("e")}")
print(f"name with uppercase {name.upper()}")
print(f"name with titlecase {name.title()}")

# print(f"name slicing {name[0:4]}")
# print(f"name slicing {name[::2]}")
# print(f"name slicing {name[0:4:2]}")


print(f"replace word e with h {name.replace('e', 'h')}")
print(f"finding index of substring mee {name.find('mee')}")
print(f"spliting name into an array/list {name.split('e')}")