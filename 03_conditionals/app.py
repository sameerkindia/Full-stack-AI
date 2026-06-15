# In this module I will learn about Conditionals
# Conditionals are one of the key things in any programing language
# In Python there is three key words :- if, elif and else. If I compare it with JS there is also three keyword that control conditionals :- if, else if, and else

# Aprat from if else there is one more conditional and that is match - case (switch in JS)


# age = 17;
# with_dad = True;

# if age >= 18 :
#     print(f"You can rant a bike or car");
# elif with_dad:
#     print(f"Your dad can rant a bike or car")
# else:
#     print(f"You need to wait {18 - age} years to rant a bike or car")



### Condition with operator

age = 17;
with_dad = False;
has_driving_licance = False;

## Or operator (Js = || )

# if age >= 18 or with_dad :
#     print(f"You can rant a car")
# else:
#     print(f"You can't rant a car by yourself")


## and operator (Js = && )

# if age >= 18 and has_driving_licance :
#     print(f"You can rant a car");
# else:
#     print(f"You can't rant a car")

## not operator  (Js = ! )



### Inline conditionals (ternary operator)
## We can write conditionals in a single line

status = 'Adult' if age >= 18 else 'Minor'

print(status)