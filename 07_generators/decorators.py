print("Decorators module");


### A Decorator is a highly powerful and elegant architectural pattern in Python that allows we to modify, extend, or inject behavior into an existing function.


### The core concept :- High order function (in JS we also have HOF);
### To understand decorators we have to realize functions are first-class citizen
### This means functions can be :-

### - Assigned to variables
### - Passed as arguments in other functions
### - Returned from other functions as output

### Simply decorator is a function that take other function as arguments. Then it wrap input function into a enternal helper function and then return wrapper function



def my_decorator(func):
    def wrapperFunc():
        print("This runs before main code")
        func()
        print("This runs after main code")

    return wrapperFunc


@my_decorator
def greet():
    print('Hello from decorator')


# greet()







### Decorating functions with arguments (*args , **kwargs)

### real-world production functions almost always accept inputs. If we try to decorate a function that accepts arguments using a basic wrapper() that accepts none, Python will throw a TypeError. To build a universal decorator capable of wrapping any function, we must use *args and kwargs inside our inner wrapper to collect and forward all passed values dynamically.


import time;

def execution_timer(main_func):
    def wrapper(*args , **kwargs):
        start_time = time.time()

        result = main_func(*args, *kwargs)

        end_time = time.time()
        duration = end_time - start_time
        print(f"[TIMER] '{main_func.__name__}' took {duration:.6f} seconds to execute.")

        return result
    return wrapper


@execution_timer
def heavy_math(power, limit):
    return sum(n ** power for n in range(limit))


# total = heavy_math(3, 1000000)
# print(f"Result: {total}")

# print(heavy_math.__name__)  ### It returned wrapper function's name not the actual function name








### Preserving Function Metadata (functools.wraps)

### When we decorate a function, we are technically replacing the original function identifier with the inner wrapper function object. Because of this, important metadata belonging to our original function—such as its name (__name__) or its structural documentation string (__doc__)—gets overwritten by the wrapper's details.

### To prevent this tracking loss, Python provides a built-in rescue decorator called @functools.wraps. We apply it to our inner wrapper function to seamlessly copy the original metadata back over.

# from functools import wraps
import functools

def decorator_2(func):
    # wraps(func)
    @functools.wraps(func)
    def wrapper(*args , **kwargs):
        return func(*args , **kwargs)
    return wrapper


@decorator_2
def analyze_trends():
    """This docstring performs enterprise text analysis."""
    pass

print(analyze_trends.__name__) 
print(analyze_trends.__doc__)