### Today I'm going to learn about function in Python

### 1. Basic function

# def greet_user():
#     print('hello! how are you');

# greet_user()


### 2. Function with parameter

def greet_user(name): #Parameter
    print(f"Hello {name}");

# greet_user('Sameer') #Arguments
# greet_user('Sahil') #Arguments


### Parameter vs Arguments
## Parameter:- The variable placeholders listed inside the function's definition parentheses.
## Arguments:- The actual values you pass into the function when you call it.


def new_user(name,age,city):
    print(f"name = {name}, age = {age}, city = {city}");


### A. Positional Arguments
## Python by default assing argument in exact order as we pass

# new_user('Sameer', 26, 'Pali')
# new_user(26, 'Pali', 'Sameer')


### B. Keywords Arguments
## With keywords arguments we can manualy assign parameter as we want. Physical order no longer matters

# new_user(age=26, city="Pali", name="Sameer");


### C. Default parameter value
## We can assign default value to parameters.

def new_user_2(name, age, country="India"):
    print(f"name = {name}, age = {age}, country = {country}");

# new_user_2(age=26, name="Sameer");



### 3. Returning values
### We can return values from a function. If we can't return anything then by default return value is None.
### We can return values with return keyword. In Python we can return multiple values. Python pack multiple values into a Tuple. we can unpack those values and use them.

def return_5():
    return 5;

return_5_value = return_5();
# print(return_5_value)


def return_multiple_value():
    return 1,2,3,"sameer";

return_value = return_multiple_value()

# print(return_value)



### Arbitrary Arguments (*args and **kwargs)

### *args (Arbitrary Positional Arguments): The single asterisk (*) gathers any extra positional arguments passed to the function and packs them into a tuple.

### kwargs (Arbitrary Keyword Arguments): Two asterisks (**) accept any extra keyword arguments and pack them into a dictionary, where the parameter name becomes the key

# def master_function(*args, **kwargs):
#     print(f"Positional arguments {args}")
#     print(f"Keywordz arguments {kwargs}")

def master_function(*test, **kwtest):
    print(f"Positional arguments {test}")
    print(f"Keywordz arguments {kwtest}")

    return test, kwtest;

# master_function(1,2,3,"sameer", name="Sameer Khan", city="Pali", age=26)
# test1 , test2 = master_function(1,2,3,"sameer", name="Sameer Khan", city="Pali", age=26);

# print(f"*args :- {test1}")
# print(f"*kwargs :- {test2}")





### Lambda expresson
### Lambda is like arrow function in JS. It's annomous function expression. We don't use def keyword to define these function and don't use return keyword.
### It's single line function expression.

lambda_expression = lambda x : x * x;

# print(lambda_expression(4))


### Pure vs Impure function 
### Pure function :- These functions generate same output with same input. It doesn't change any global variables.

### Impure function :- These function change global state. It's behavior depend on external variables