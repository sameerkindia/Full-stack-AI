### Today I'm going to learn about function in Python

### 1. Basic function

# def greet_user():
#     print('hello! how are you');

# greet_user()


### Function with parameter

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

new_user('Sameer', 26, 'Pali')
new_user(26, 'Pali', 'Sameer')


### B. Keywords Arguments
## With keywords arguments we can manualy assign parameter as we want. Physical order no longer matters

new_user(age=26, city="Pali", name="Sameer");



### C. Default parameter value
## We can assign default value to parameters.

def new_user_2(name, age, country="India"):
    print(f"name = {name}, age = {age}, country = {country}");



new_user_2(age=26, name="Sameer");
