# Python is a OOP language
# Everything in the Python is an object
# And every object in Python has properties [attributes] and methods

class Thyself:
  def __init__(self, name, age, home, occupation):
    self.name = name
    self.age = age
    self.home = home
    self.occupation = occupation
    
  def __str__(self):  # a function to include what to return if the function is print or seen as a string
    return f"My name is {self.name}. I am {self.age} years old. And I am from {self.home}."
  
  def set_profile(self, college, varsity, phone, highest_degree):
    self.college = college
    self.varsity = varsity
    self.phone = phone
    self.degree = highest_degree
    
  def return_profile(self):
    return f"College: {self.college}  Varsity: {self.varsity}  Phone: {self.phone}  Degree: {self.degree}"
  
  def check_pass(self):
    pass
  
myself = Thyself("Reyan", 22, "Gaibandha", "SE")
myself.set_profile("NDC", "IUT", "Airtel", "BSc")

# print(myself.age)
# print(myself)  # this line prints __str__() method

# print(type(myself))
# print(myself.return_profile())
myself.college = "Ideal"  # modify properties

# print(myself.return_profile())

# del myself.college  # delete properties
# print(myself.return_profile())
# print(myself.check_pass())  # a method definition [or body] can't be empty but with pass keyword we can achieve it



## Inheritance 

class Person:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname
    
  def my_name(self):
    return f"{self.fname} {self.lname}"
    
class Student(Person):
  # pass     # even with pass the Student class will work very much like the person class as it has inherited it
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduation_year = year
    
  def intro(self):
    return f"{self.fname} {self.lname}, {self.graduation_year}"
    
rahid = Student("Rahid", "Hasan", 2023)

print(rahid.intro())


# Polymorphism

#function polymorphism

str = "hello world"
tupple  =  ("banana", "peach", "cherry")
dic = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

   
print(len(str))
print(len(tupple))   # in function polymorphism we can see the same len function is returning the length of different datatypes
print(len(dic))


#class polymorphism

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()


# inheritance class polymorphism

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
