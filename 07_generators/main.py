print("Genetators Module");

### What is Generator ?
### Generator is a spacial type of function that returns a lazy iterator. Instead of returning a single value and treminating. A generator pauses its execution and yields a value to the caller using the yield keyword. When requested again, it resumes exactly where it left off, maintaining its internal state and variable values.


def simple_generator():
    print('starting')
    yield 'first item'
    print('resuming')
    yield 'second item'
    print('endind')


# print(next(simple_generator()))
# print(next(simple_generator()) , "2")

gen = simple_generator()

# print(next(gen))
# print(next(gen))
# print(next(gen))  # StopIteration error


### 2. Infinite generator

def infinite_counter(start=0):
    current = start

    while True:
        yield current

        current += 1

counter_1 = infinite_counter(1)

# print(next(counter_1))
# print(next(counter_1))
# print(next(counter_1))
# print(next(counter_1))
# print(next(counter_1))
# print(next(counter_1))



### 3. Sending values to generator (.send())

def live_replacer():
    sam = 'Default text'

    while True:
        new_value = yield sam
        if new_value is not None:
            sam = new_value


# new_gen = live_replacer()
# print(next(new_gen))
# # print(new_gen.send('sameer'))
# print(new_gen.send([]))
# print(next(new_gen))





### 4. yield from and Closing Generators

def sub_task_1():
    yield 'Sub step 1 A'
    yield 'Sub step 1 B'
    yield 'Sub step 1 C'

def sub_task_2():
    yield 'Sub step 2 A'
    yield 'Sub step 2 B'
    yield 'Sub task 2 C'

def main_task():
    yield 'Main task 1'
    yield from sub_task_1()
    yield 'Main task 2'
    yield from sub_task_2()

# for step in main_task():
#     print(step)


task_pipline = main_task()

# print(next(task_pipline))
# print(next(task_pipline))
# print(next(task_pipline))
# print(next(task_pipline))
# print(next(task_pipline))
# print(next(task_pipline))

task_pipline.close()