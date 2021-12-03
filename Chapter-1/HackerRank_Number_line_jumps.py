"""
You are choreographing a circus show with various animals. For one act, you are given two 
kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

- The first kangaroo starts at location "x1" and moves at a rate of "v1" meters per jump.
- The second kangaroo starts at location "x2" and moves at a rate of "v2" meters per jump.

You have to figure out a way to get both kangaroos at the same location at the same time 
as part of the show. If it is possible, return YES, otherwise return NO.

Example
x1 = 2
v1 = 1
x2 = 1
v2 = 2

After one jump, they are both at x = 3, (x1 + v1 = 2 + 1, x2 + v2 = 1 + 2), so the answer is YES.

Function Description
Complete the function kangaroo in the editor below.
kangaroo has the following parameter(s):

- int x1, int v1: starting position and jump distance for kangaroo 1
- int x2, int v2: starting position and jump distance for kangaroo 2

Returns:
- string: either YES or NO

Input Format
A single line of four space-separated integers denoting the respective values of x1, v1, x2, and v2.

Constraints:
0 <= x1 < x2 <= 10000
1 <=v1 <= 10000
1 <= v2 <= 10000


Sample Input 0
0 3 4 2
Sample Output 0
YES

Explanation 0
The two kangaroos jump through the following sequence of locations:

image... not available here

From the image, it is clear that the kangaroos meet at the same location (number 12 on the number line) 
after same number of jumps (4 jumps), and we print YES.

Sample Input 1
0 2 5 3
Sample Output 1
NO
Explanation 1
The second kangaroo has a starting location that is ahead (further to the right) of the first
 kangaroo's starting location (i.e., x2 > x1). Because the second kangaroo moves at a faster 
 rate (meaning v2 > v1) and is already ahead of the first kangaroo, the first kangaroo will 
 never be able to catch up. Thus, we print NO.


Option Solution 1:
* max distance is 10000

- check if x1 == x2 if yes return YES else do:
- while x1 or x2 is not equal or bigger 10000 or x1 is not equal x2 do:
- take x1 add v1 and take x2 and add v2
- check if x1 is equal x2 if yes return YES else repeat

Option Solution 2:

include extra checks e.g.
- check if x1 < x2 and v1 < v2 then return NO

# I CHEATED AND LOOKED AT THE DISCUSSION AND FOUND THIS... MY LACK OF MATH IS AN ISSUE...
THIS SOLUTION IS NOT CORRECT AS IT HAS TO BE bigger first minus smaller value
X2 - X1 AND V1 - V2!v==> (x2 - x1) % (v1 - v2) == 0

"We just need solve equation : 
x1 + y * v1 = x2 + y * v2 where "y" is number of jumps... so if (x1 - x2) % (v2 - v1) == 0 then our 
kangaroos will meet each other"


"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if v1 < 1 or v2 < 1 or x1 == x2 or v1 == v2 or (x1 < x2 and v1 < v2) or (x1 < 0 and x2 < x1):
        return "NO"

    if (x2 - x1) % (v1 - v2) == 0:
        return "YES"
    else: 
        return "NO"
    
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     x1 = int(first_multiple_input[0])

#     v1 = int(first_multiple_input[1])

#     x2 = int(first_multiple_input[2])

#     v2 = int(first_multiple_input[3])

#     result = kangaroo(x1, v1, x2, v2)

#     fptr.write(result + '\n')

#     fptr.close()

# 0 2 5 3 output NO                                      (5-0) % (2-3) = 
# 0 3 4 2 ouput YES  if (x2 - x1) % (v1 - v2) == 0:      (4-0) % (3-2) = 0

# x1 = 0
# x2 = 5
# v1 = 2
# v2 = 3


x1 = 0
x2 = 4
v1 = 3
v2 = 2

print(kangaroo(x1, v1, x2, v2))
