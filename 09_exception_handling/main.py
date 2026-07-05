

### 1. The Core Exception Handling Blocks

### Python uses four main keywords to manage exceptions:
### try, except, else, and finally.  

### try: The code block where you anticipate an error might happen. Python monitors this block.
### except: The rescue block. If an error occurs inside the try block, Python stops executing it and jumps straight here. 
### else: Runs only if the code inside the try block executed perfectly without raising any errors.
### finally: The safety net. It runs no matter what—whether an error happened or not. This is typically used for clean-up actions like closing database connections or files.  


def set_age(age):
    try:
        if age <= 0:
            raise ValueError("Age can't be less then 0")
    except ValueError as err :
        print(err)
    else:
        return age + 2
    finally:
        print("function is closed")


print(set_age(0))