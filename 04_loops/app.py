### Today I'm going to learn about Loops in Python.
### There is 2 primary types of loops 1. for loops 2. while loop

## for loops

fruits = ['apple', 'banana', 'cherry']

# for fruit in fruits:
#     print(fruit);


## The range() function
## Whenever we need numbers count or want to repeat action in a set number time we use range()

# for num in range(3):
#     print(num , fruits[num]);


## Last index doesn't count
# for num in range(1,11):
#     print(num);



### The while loop
### We use while loop when we want to repeat an action till a specific condition is True;

count = 1;

# while count < 5:
#     print(f"This is count in while loop {count}");
#     count += 1;



### Loop control keywords: break and continue

# while count < 10:
#     if count == 5:
#         print(f"number 5 is skiped");
#         count += 1;
#         continue;

#     print(count);
#     count += 1;


# while count < 10:
#     if count == 5:
#         print(f"number 5 loop break");
#         count += 1;
#         break;

#     print(count);
#     count += 1;


### else on loop
### This is a uniqe feature of Python. After loop is completed without break else block will executed

# while count < 10:
#     if count == 5:
#         print(f"number 5 loop break");
#         count += 1;
#         break;
    
#     print(count);
#     count += 1;
# else:
#     print("Loop is completed")



### enumerate()
### When we need collection item with index we use enumerate().


fruits = ['apple', 'banana', 'cherry']

# for index, fruit in enumerate(fruits):
#     print(f"This is enumerate {index} {fruit}");




### zip()
### When we want to process two ordered sequences togather we use zip()

# for item in zip([1,2,3], fruits):
#     print(f"This is enumerate {item}");


### The walrus operator (:=)
### This is an assingment operator

a = [1,2,3,4,5,6,6,7,8,8,8,56,43]

if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")