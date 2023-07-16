# open()
# open(filename, opening_mode, encoding)
# default mode read ('r'), default encoding 'UTF-8'

# greet = open("hello.txt", 'r')
# print(greet.read())
# greet.close()

# using 'with' together with 'open', while using with, the file doesn't have to be closed seperately
# with has two built-in methods: __enter__() and __exit__()
# __exit__() automatically closes the file when the operation is done

# with open('hello.txt', 'r') as greet:
#   # print(greet.read())

with open('hello.txt', 'w') as my_file:
    my_file.write("Hello world \n")
    my_file.write("I hope you're doing well today \n")
    my_file.write("This is a text file \n")
    my_file.write("Have a nice time \n")

# with open("hello.txt", 'r') as file:
#     print(file.read())


# line by line reading

with open("hello.txt", 'r') as file:
  for line in file:
    print(line)
   
with open("hello.txt", 'r') as file:
  for line in file:
    for letter in line:
      print(letter)