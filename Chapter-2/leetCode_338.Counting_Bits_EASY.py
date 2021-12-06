# 338. Counting Bits
"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is 
the number of 1's in the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105
 

Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) 
and possibly in a single pass?
Can you do it without using any built-in function?


#################################################################
WHAT IS BINARY REPRESENTATION and DECIMAL AND HOW TO CONVERT IT
https://www.cuemath.com/numbers/decimal-to-binary/
https://www.cuemath.com/decimal-to-binary-formula/

What is Decimal to Binary Formula?
In the formula to convert decimal to the binary method, we will perform division on the given decimal number 
recursively by 2 and note down the remainders till we have either 0 or 1 as the final quotient. Steps that are 
used to convert decimal to the binary number using decimal to the binary formula are shown below,

Step 1: Divide the given decimal number by 2, note down the remainder.
Step 2: Now divide the quotient thus obtained in the above step by 2, note down the remainder.
Step 3: Repeat the above steps until we get 0 or 1 as a quotient.
Step 4: Write down the last quotient in line with remainders from last to the first, this is our binary conversion 
of the given decimal number.

Example 1: Using decimal to binary formula, convert 29 decimal into a binary number.

Solution:

Using decimal to binary formula, we have,
Step 1: Divide the number by 2, note down the remainder:
29 ÷ 2 gives Q1 = 14, R = 1

Step 2: Divide Q1 by 2, note down the remainder:
14 ÷ 2 gives Q2 = 7, R = 0

Step 3: Divide Q2 by 2, note down the remainder:
7 ÷ 2 gives Q3 = 3, R = 1

Step 4: Divide Q3 by 2, note down the remainder:
3 ÷ 2 gives Q4 = 1, R = 1

Step 5: Write down the last quotient in line with remainders from last to the first, this is our binary conversion of the given decimal number:
11101

Answer: Hence, 29 as binary is 
11101 with lower 2 (opposite to ^) - probably binary representation.

#################################################
RESULTS:
Runtime: 564 ms, faster than 5.03% of Python online submissions for Counting Bits.
Memory Usage: 29.3 MB, less than 11.97% of Python online submissions for Counting Bits.

NO IDEA SO FAR HOW TO OPTIMISE IT.
"""

import numpy as np

class Solution(object):

    def convert_i_to_binary(self, decimal_num, remainder):
        
        result_of_division = np.inf
        print("number to divide is ", decimal_num)
        if decimal_num % 2 == 0:# and decimal_num != 2:
            remainder += 0
            result_of_division = decimal_num / 2
            print("number divided by 2: ", decimal_num, " was devided by 2 and is = ", result_of_division)
        else:
            remainder += 1
            result_of_division = (decimal_num - 1) / 2
        
        print("## \n result of division is is ", result_of_division)
        print("### result of reminder is ", remainder)

        if result_of_division >= 1:
            print("result of division is is bigger than 0 then recursivelly ", result_of_division, "\n")
            remainder = self.convert_i_to_binary(result_of_division, remainder)
        return remainder

    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if (0 > n > 10**5):
            return
        #arr_n = np.arange(start = 0, stop = n)
        output_arr = []
        remainder = 0
        
        
        for i in range(n + 1):
            remainder = 0
            print("i ", i)
            binary_sum = self.convert_i_to_binary(i, remainder)
            print(binary_sum)
            output_arr.append(binary_sum)
            print(output_arr)
        
        return output_arr 



sol = Solution()
# n = 2
n = 5
print(sol.countBits(n))