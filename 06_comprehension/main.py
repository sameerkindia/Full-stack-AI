print("Comprehension in Python module")

### In Python comprehension is a concise and elegent syntex that create new collection with existing iterables.
### Instead of writing a mulit-line for loop to build a collection piece-by-piece, comprehensions allow you to do it all in a single, highly readable line of code.

numbers_list = [1,2,3,4,5]

### 1. List Comprehension

### [expression for item in iterable if condition]

squres = [num ** 2 for num in numbers_list]
squres_2 = [num ** 2 for num in numbers_list if num % 2 == 0]

# print(squres)
# print(squres_2)


### 2. Dictionary Comprehension 
squres_dict = {num: num **2 for num in numbers_list }

print(squres_dict)




### 3. Set Comprehension
word_str = 'banana'

unique_letters = {word for word in word_str}

print(unique_letters)