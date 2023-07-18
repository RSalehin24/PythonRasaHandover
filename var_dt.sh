#! /bin/bash
# no data types (dt) in bash 
# variables can store int, decimal, char, string

# assign values to variable
# country=Bangladesh

# $ is used to access the value of the variable
# same_country=$country

# echo $country
# echo $same_country

# variable can't:
# start with a number 
# no space or special characters
# no reserved words (keywords)

# reading the input and storing it in a variable
# cd ../

# echo "Please enter the name of the directory"
# read directory

# echo "The mentioned directory contains the following files and folders:"
# ls $directory

# cd ./bash_scripting

# read file
  # while read line
  # do
  #   echo $line
  # done < hello_bash.txt


# passing arguments: $1 for first argument, $2 for second argument
# print the output using echo
echo "hello, $1!"

# write to a file using echo
echo "this is writing to a file" > output.txt

# appending to a file
echo "more text" >> output.txt

# redirecting output 
ls > files.txt
