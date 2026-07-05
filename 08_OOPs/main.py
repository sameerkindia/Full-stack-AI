class User:
   def __init__(self, name , age):  # Constructor or __init__ and self keyword
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

# print(user_1.name)

# user_1.say_my_name()
# user_2.say_my_name()

user_1.name = "Sameer Khan" # Attribute shadowing
# print(user_1.name)
# user_1.say_my_name()




### Inheritance and Composition

### A. Inheritance
###  Inheritance allows a new class to adopt the attributes and methods of an existing class
###   It's an "Is-a" relationship. For example:
###     - A Dog is a Animal.
###     - A Car is a Vehicle.

## Parent class or Superclass
class Vehical:
   def __init__(self, brand, model):
      self.brand = brand
      self.model = model

   def start_engine(self):
      # print(f"The {self.brand} {self.model}'s engine is running.")
      return f"The {self.brand} {self.model}'s engine is running."


### Child class
class Car(Vehical): # We inherit class like this
   def __init__(self, brand, model, color):
      super().__init__(brand, model) # super keyword call parents constructor function
      self.color = color

   def start_engine(self):
      parent_engine = super().start_engine()
      return f"{parent_engine} Smooth and quiet in {self.color} color."
   

my_car = Car("Jeep", 'top model', 'black')
# print(my_car.start_engine())




### B. Composition (The "Has-A" Relationship)
### Composition is a design pattern where a class combines one or more completely independent objects as its attributes to build more complex behavior. Instead of inheriting features, it buys or uses them.

###   It represents a "Has-A" relationship. For example:
###   - A Car has an Engine.
###   - A User has a Profile.



### Independent Class 1
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def ignite(self):
        return "Vroom! Engine ignites."

### Independent Class 2
class Stereo:
    def __init__(self, brand):
        self.brand = brand

    def play_music(self):
        return f"Playing tunes on the {self.brand} system."

class ComplexCar:
    def __init__(self, brand, model, hp, stereo_brand):
        self.brand = brand
        self.model = model

        self.engine = Engine(horsepower=hp)
        self.stereo = Stereo(brand=stereo_brand)

    def drive(self):
        # Delegating behavior to internal component objects
        status = self.engine.ignite()
        entertainment = self.stereo.play_music()
        return f"Driving the {self.brand}. {status} {entertainment}"


my_complex_car = ComplexCar("Ford", "Mustang", 450, "Bang & Olufsen")
# print(my_complex_car.drive())





### Method Resolution Order (MRO)

### MRO is the strict order or hidden "roadmap" Python follows to look up a method or attribute when a class uses Multiple Inheritance (inheriting from more than one parent class).

class A:
    def process(self) : return "Process A"

class B(A): # B Inherit A Class
    # B's process method overrides A's process method
    def process(self): return "Process B"

class C(A):
    def process(): return "Process C"


# Parents are checked in the exact order they are listed in the class definition. (First it checks B and if he founds the method he will stop searching and call the method)
class D(B,C): # Multiple Inheritance
    pass

obj = D()

# print(obj.process())
# print(D.__mro__)











### Static Methods (@staticmethod)
### A Static Method is a regular function housed inside a class namespace purely for organizational or logical grouping.

class MathUtility:
    @staticmethod
    def is_even(number): # No self or cls argument
        return number % 2 == 0
    

# print(MathUtility.is_even(10))
# print(MathUtility.is_even(9))




### Class Methods vs. Static Methods

### A Class Method is tightly linked to the class itself rather than individual instances. It automatically takes a first argument named cls, which represents the class object. It is heavily used to create factory methods (alternative ways to initialize objects).


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split('-')
        return cls(name, int(age))
    
    @classmethod
    def from_dict(cls, data):
        # return cls(data)
        return cls(data["name"], data["age"])
    

    @staticmethod
    def is_workday(day):
        return day not in ["Saturday", "Sunday"]
    

sameer = Employee.from_string("Sameer Khan-26")
sameer2 = Employee.from_dict({"name": "Sameer khan", "age": 26})

print(sameer.name)
print(sameer2.name)

print(sameer2.is_workday("Friday"))
print(Employee.is_workday('Monday'))



### Property Decorators (Getters & Setters)
### The @property decorator allows we to turn a standard method into an encapsulated attribute. This lets we run logic or validation behind the scenes while keeping our public-facing code looking like simple attribute access (obj.attribute).

### Getter (@property): Runs whenever someone reads the attribute value.

### Setter (@attribute.setter): Runs whenever someone attempts to modify or overwrite the attribute value. Allows we to intercept bad values before they break our code.


class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # Protected attribute (under the hood)

    # Getter: Accesses property like an attribute
    @property
    def celsius(self):
        print("Getting temperature value...")
        return self._celsius

    # Setter: Validates and intercepts assignments
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below Absolute Zero is impossible!")
        print("Setting temperature value...")
        self._celsius = value

t = Temperature(25)

print(t.celsius)

t.celsius = 30
