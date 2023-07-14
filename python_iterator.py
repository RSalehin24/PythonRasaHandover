# An iterator which can be iterated upon, knows in which state it is in, can return the next item and contains __iter__() and __next__() methods

# Iterable objects conatins a iterator (or __iter__() function), they are iterable and returns the iterator when they are asked to be looped upon or iterated upon
# iterable objects inculde tuples, lists, string, dictionary, sets etc.

my_tuple = ("apple", "banana", "cherry")
print(dir(my_tuple))

my_tuple_iter = iter(my_tuple) # iter also contains __iter__() function it usually returns itself when calling it
print(iter(my_tuple_iter))
print(next(my_tuple_iter)) # iter remembers it state and when calling its next function, it returns the next item

my_string = "banana"  # strings are iterable objects and returns __iter__() function
print(iter(my_string).__next__())

# loops use an iter to iterate through an iterable object
# loop can be used to iterate through iter using for loop
for iter_item in my_tuple_iter:
  print(iter_item)

my_string_iter = iter(my_string)

for letter in my_string_iter:
  print(letter)
  
    
# Building my own iterator

class MyIterator:
  def __iter__(self):
    self.start = 0
    return self
  
  def __next__(self):
    if self.start < 30:
      self.start += 1
      return self.start
    else:
      raise StopIteration
    
my_iter_obj = MyIterator()
my_iter = iter(my_iter_obj)

for num in my_iter:
  print(num)
