def SQFirstTen():
  i = 1
  while i <= 10:
    yield i**2   # yield keywords creates the generator, it acts like __next__() function instead of return keywords 
    i += 1
    
for sq in SQFirstTen():
  print(sq)
  