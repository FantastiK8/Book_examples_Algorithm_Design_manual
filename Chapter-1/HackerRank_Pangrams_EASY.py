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
Solution:
- n number has the number of all letters in english alphabet
- make a new empty arr
- loop through the string s
- chek if the char is already in the new arr if not add if yes skip
- after loop if the n is the same as the lenght of arr return pangram otherwsie return nto pangram
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
import string

def pangrams(s):
    # Write your code here
    if len(s) > 0 and len(s) < 10**3:
        n = 26 # number of letters in english alphabet
        unique_char_arr = []
        translator = str.maketrans('','', string.punctuation)
        s = s.translate(translator)

        print(s)
        for char in str.lower(s):
            if char.isspace() == False:
                if char not in unique_char_arr:
                    unique_char_arr.append(char)
                   # print(unique_char_arr)
        print("len", len(unique_char_arr))
        print("n ", n)
        if n == len(unique_char_arr):
            return "pangram"
        else:
            return "not pangram"

s = "We wwwww!!!!!@promptly judged antique ivory buckles for the next prize!"
print(pangrams(s))
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = pangrams(s)

#     fptr.write(result + '\n')

#     fptr.close()
