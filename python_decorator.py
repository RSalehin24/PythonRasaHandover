# In Python functions are first class objects which means they can be used or passed as an argument
import math
import time


def shout(text):
  return text.upper()

# assigning function to a variable
yell = shout

# print(yell("Hello"))


def whisper(text):
  return text.lower()

# declaring a function with function as a parameter 
def greet(func):
  greeting = func("Hello")
  print(greeting)
  
# greet(shout)
# greet(whisper)

# declaring a function which returns a function
def create_adder(x):
  def adder(y):
    return x+y
  return adder

add_15 = create_adder(15)

# print(add_15(8))


## Example of decorator

def calculate_time(func):
  def inner(*args, **kwargs):
    begin = time.time()
    func(*args, **kwargs)
    end = time.time()
    
    print("Time taken for executing the function:", func.__name__, end - begin)
  
  return inner

@calculate_time
def factorial(num):
  time.sleep(2)
  print(math.factorial(num))
  
# factorial(5)

# functions with return value

def decorator_function(func):
  def inner(*args, **kwargs):
    print("Before Execution")
    returned_value = func(*args, **kwargs)
    print("After Execution")
    return returned_value
  return inner

@decorator_function
def factorial(num):
  return math.factorial(num)

# print(factorial(8))


## chaining decorator

def decor_square(func):
  def inner():
    x = func()
    return x * x
  return inner

def decor_two_times(func):
  def inner():
    x = func()
    return 2 * x
  return inner


# decor_square(decor_two_times(return_10))

@decor_square
def return_ten():               
  return 10



# decor_square(decor_two_times(return_10))
@decor_two_times
@decor_square
def return_ten_again():
  return 10

print(return_ten())
print(return_ten_again())