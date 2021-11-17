# Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

# You may assume the input array always has a valid answer.

# Example 1:

# Input: nums = [1,5,1,1,6,4]
# Output: [1,6,1,5,1,4]
# Explanation: [1,4,1,5,1,6] is also accepted.
# Example 2:

# Input: nums = [1,3,2,2,3,1]
# Output: [2,3,1,3,1,2]
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# 0 <= nums[i] <= 5000
# It is guaranteed that there will be an answer for the given input nums.
 

# Follow Up: Can you do it in O(n) time and/or in-place with O(1) extra space?




class Solution(object):

    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        ####### option 2
        # sort the array and pop one from the beginning for odd possitions
        # then pop always the end item from sorted for even possitions until items are in the sorted.    

        sorted_arr = []
        odd_pos_item = 0
        even_pos_item = 0
      # I MUST DO QUICKSORT  
        quicksorted = [1,1,1,4,5,6]

        for i in range (len(quicksorted)):
            if (i+1) % 2 != 0:
                odd_pos_item = quicksorted.pop(0)
                sorted_arr.append(odd_pos_item)
                print("\n ODD ",odd_pos_item)
                print("\n SORTED ",sorted_arr)
            elif (i+1) % 2 == 0:
                even_pos_item = quicksorted.pop()
                print("\n EVEN ",even_pos_item)
                sorted_arr.append(even_pos_item)
                print("\n SORTED ",sorted_arr)
            


        return sorted_arr







nums = [1,5,1,1,6,4]
#nums = [1,6,1,5,1,4] # dummy example sorted works well.
solution = Solution()
#solution.wiggleSort(nums)
print(solution.wiggleSort(nums))




