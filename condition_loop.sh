#!/bin/bash

echo "please enter a number:"
read num


# if - else condition
if [ $num -gt 0 ]; then
  echo "$num is positive"
elif [ $num -lt 0]; then
  echo "$num is negative"
else
  echo "$num is 0"
fi

# while loop
i=1
while [[ $i -le 10 ]]; do
  echo "$i"
  ((i += 1))
done

# for loop
for i in {1..5}
do
  echo $i
done

# case statement
fruit="apple"

case $fruit in
  "apple")
    echo "This is a red fruit"
    ;;
  "banana")
    echo "This is a yellow fruit"
    ;;
  "orange")
    echo "This is an orange fruit"
    ;;
  *)
    echo "Unknown fruit"
    ;;
esac
