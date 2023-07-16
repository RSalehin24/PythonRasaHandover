#   what single asterisk (*) and double asterisks (**) do to a python parameter?

# *args -> non keyword arguments, receives arguments as a tuple
# **kwargs -> key word arguments, receives arguments as a dictionary

# asterisk wildcard (*) indicates a variable number of arguments can be passed to a function
# Variable associted with the asterisk (*) sign (*args) becomes iterable, meaning we can iterate over it and use high-order function like map and filter on it


### *args
def example_args(*args):
  for value in args:
    print(value)

# example_args("My", "name", "is", "Reyan")    


# one required argument
def example_args0(arg, *args):
  print("Required Argument:", arg)
  for other in args:
    print("another argument: ", other)

# example_args0("My", "name", "is")




### **kwargs

# Used to pass keyworded variable-length argument list
# Keyword Argument is where you provide a name to the variable as you pass it into the function
# kwargs like a dictionary which maps value to the key and no specific order for iteration
# *kwargs for a variable number of keyword arguments 
# **kwargs accept keyworded variable-length argument

def example_kwargs(**kwargs):
  for key, value in kwargs.items():
    print("%s==%s" % (key, value))
    
# example_kwargs(first="geeks", second="not for", third="geeks")

# one required argument

def example_kwargs(kwarg, **kwargs):
  for key, value in kwargs.items():
    print("%s==%s" % (key, value))
    
# example_kwargs("Hi", first="geeks", second="not for", third="geeks")


def example_kw_args(arg1, arg2, arg3):
  print("arg1:", arg1) 
  print("arg2:", arg2) 
  print("arg3:", arg3) 
  
args = ("My", "name", "is")
kwargs = {"arg1" : "Geeks", "arg3":"not for", "arg2":"Geeks"}

# example_kw_args(*args)
# example_kw_args(**kwargs)

def example_kw_args0(*args, **kwargs):
  print("args:", args)
  print("kwargs:", kwargs)

# example_kw_args0('geeks', 'not for', 'geeks', first="Geeks", mid="not for", last="Geeks")

class car():
  def __init__(self, *args):
    self.color = args[0]
    self.speed = args[1]
    
audi = car('red', 200)
bmw = car('black', 250)

print(audi.color)
print(bmw.speed)


class car():
  def __init__(self, **kwargs):
    self.color = kwargs['c']
    self.speed = kwargs['s']

audi = car(c='red', s=200)
bmw = car(c='black', s=250)

print(audi.speed)
print(bmw.color)
