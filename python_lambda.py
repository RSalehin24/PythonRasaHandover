# Lambda functions are anonymous functions
# Anonymous functions are any function which are without names

# Lambda function:
# Any number of arguments
# Only one expression [strict, can't exceed one expression]


from functools import reduce

# example

# string to uppercase


def uppr(string): return string.upper()


# print(uppr("reyan"))


# condition checking

def format_numeric(num): return f"{num:e}" if isinstance(
    num, int) else f"{num:,.2f}"

# print(format_numeric(10000000))
# print(format_numeric(0.343342434))


# difference

def cube(y):
    return y*y*y


def lambda_cube(y): return y*y*y


# print(cube(10))
# print(lambda_cube(10))

# lambda with list comprehension
is_even_list = [lambda arg=x: arg*10 for x in range(1, 5)]

# for item in is_even_list:
#     print(item())

# max


def max(a, b): return a if a > b else b


# print(max(9, 5))


# Lamba with multiple statements but
# we can create 2 lambda functions and pass one as an argument to other


List = [[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]

# Sort each sublist


def sortList(x): return (sorted(i) for i in x)

# Get the second largest element


def secondLargest(x, f): return [y[len(y)-2] for y in f(x)]


res = secondLargest(List, sortList)

# print(res)

# filter odd numbers using filter and lambda

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x % 2 != 0), li))
# print(final_list)

ages = [13, 90, 17, 59, 21, 60, 5]
more_than_eightteen = list(filter(lambda x: (x > 18), ages))
# print(more_than_eightteen)


# Multiply all elements by 2 using lambda and map
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
two_times = list(map(lambda x: (2*x), li))
# print(two_times)

animals = ['dog', 'cat', 'parrot', 'rabbit']

upper_case = list(map(lambda x: x.upper(), animals))
# print(upper_case)


# reduce with lambda
li = [5, 8, 10, 20, 50, 100]

sum = reduce((lambda x, y: x+y), li)
print(sum)

lis = [1, 3, 5, 6, 2, ]
max = reduce((lambda a, b: a if a > b else b), lis)
print(max)
