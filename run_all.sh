#! /bin/bash

echo "Today is" `date`  #  ` ` for printing the value of a system function or variable

pwd

echo -e "\nenter the path to dirctory"
read the_path   # like input

echo -e "\nThe path has the following file has the following files and folders: "
ls $the_path  # the_path is a variable, we get the value in the_path using $ synbol

chmod u+x filename  # access for user for executing the file [replace filename with the real file name

