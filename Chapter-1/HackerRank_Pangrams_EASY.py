# A pangram is a string that contains every letter of the alphabet. Given a 
# sentence determine whether it is a pangram in the English alphabet. Ignore case. 
# Return either pangram or not pangram as appropriate.

# Example
# s = 'The quick brown fox jumps over the lazy dog'

# The string contains all letters in the English alphabet, so return pangram.

# Function Description

# Complete the function pangrams in the editor below. It should return the string pangram if 
# the input string is a pangram. Otherwise, it should return not pangram.

# pangrams has the following parameter(s):

# string s: a string to test
# Returns

# string: either pangram or not pangram

# Input Format
# A single line with string s.

# Constraints
#0< lenght of s<= 10**3
# Each character of s, s[i] E {a-z, A-Z, space}, 

# Sample Input
# Sample Input 0
# We promptly judged antique ivory buckles for the next prize
# Sample Output 0
# pangram
# Sample Explanation 0
# All of the letters of the alphabet are present in the string.
# Sample Input 1
# We promptly judged antique ivory buckles for the prize
# Sample Output 1
# not pangram
# Sample Explanation 0
# The string lacks an x.

"""
Solution 1 NOT WORKING: - missing restrictions for other symbols and characterous like 
punctuation, numbers and math symbols
- n number has the number of all letters in english alphabet
- make a new empty arr
- loop through the string s
- chek if the char is already in the new arr if not add if yes skip
- after loop if the n is the same as the lenght of arr return pangram otherwsie return nto pangram

Solution 2:  WORKS!!
- Create an array full of intetrgers representing the order in memory for letter a - z -->
as the programming languages are in english...
- loop through the string s
- check if the order of the char from s is in the array of unique orders
- if yes remove it fromt he unique orders array
- after loop if the lenght of the unique orders array is 0 then return pangram else not pangram.

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    unique_char_arr_ord = [ord_ for ord_ in range(ord('a'), ord('z'))]   #print([i**2 for i in range(10)])
    
    for char in str.lower(s):
        if ord(char) in unique_char_arr_ord:
            unique_char_arr_ord.remove(ord(char))

    return "pangram" if len(unique_char_arr_ord) == 0 else "not pangram"


s = "We wwwww!!!!!@promptly judged antique ivory buckles for the next prize!"
print(pangrams(s))
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = pangrams(s)

#     fptr.write(result + '\n')

#     fptr.close()
