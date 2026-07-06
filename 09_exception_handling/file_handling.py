

### 1. The Traditional Way: try-except-finally

file = None

try :
    file = open('demo.txt' , 'w')
    file.write("Hello, This is demo text")
    pass
except :
    print("There is some error")
finally:
    if file:
        file.close()
        print("File closed")



### 2. The Modern Standard: The with Statement

### The file automatically closes as soon as this block is exited
with open('demo.txt', "r") as file:
    content = file.read()
    print(content)

### No file.close() needed here!





### 3. The Bulletproof Combo: Combining with and try-except

try:
    with open('demo1.txt', 'r') as file:
        # file.write(" More data")
        content = file.read()
        print(content)

except FileNotFoundError:
    print("Error: The demo file is completely missing.")