class User:
   def __init__(self, name , age):  # Constructor and __init__
      self.name = name
      self.age = age
   
#    name = "Sameer"  # Class namespace
#    age = 26
   def say_my_name(self):     # Method and self keyword
      print(f"My name is {self.name}")


# user_1 = User() # Object created from User class
user_1 = User("Sameer Khan" , 26) # Object created with constructor
user_2 = User("Sahil Khan" , 28) # Object created with constructor

user_1.city = "Pali" # Object namesapce

print(user_1.name)

user_1.say_my_name()
user_2.say_my_name()

user_1.name = "Sameer Khan" # Attribute shadowing
print(user_1.name)
user_1.say_my_name()