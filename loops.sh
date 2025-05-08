#!/usr/bin/evn bash
# # This script demonstrates the use of loops in bash

# for fruit in apple banana cherry
# do
#   echo "I love eating snacks $fruit"
# done


# This script demonstrates the use of loops in Python

fruits=("apple" "banana" "cherry")

for fruit in "${fruits[@]}"
do
    echo "I love eating snacks like $fruit"
done
