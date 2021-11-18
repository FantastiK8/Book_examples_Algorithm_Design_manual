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



#### options:
# I make an array of bol where will have all false for not fitted yet in the lenght of nums
# while looping through nums take ith item in nums and check if already fitted in the array of bol
# if fitted skip, if not try to fit and assign in bol array as fitted, if it does not fit skip the item and go to the next in nums.
####### option 2
# sort the array and pop one from the beginning for odd possitions
# then pop always the end item from sorted for even possitions until items are in the sorted.
class Solution(object):
    def sort(self, nums, sorted_arr, not_fit_arr, len_int):
        
        # RECURSION
        # # make a new empty array where sorted items will be added
        # sorted_arr = []
        # # create an empty array where items which do not fit will be stored
        # not_fit_arr = []
        failed_bol = False

        #base case:
        if len(sorted_arr) == len_int or failed_bol or len(not_fit_arr) == 4:
            return sorted_arr
        
        else:
            i = len(sorted_arr)
            while i < len_int -1: # do i need -1???
                
                print("\n \n len of nums ", len(nums))
                print("\n ################################################ ")
                print("\n i ", i, " sorted_array ", sorted_arr)#

                # if is the first item add to sorted:
                if i == 0:
                    sorted_arr.append(nums[i])
                    # print("\n i ", i, " sorted_array ", sorted_arr)
                
                    
                # else if not the first item
                elif i > 0:
                    print("\n ############## i ", i, " sorted_array ", sorted_arr)
                    #print(i)
                    # check if i is not the last i:
                    if i+1 <= len(nums)-1:
                        print("#############",i)
                        # if i is odd
                        if i % 2 != 0: 
                            print("\n EVEN nums[i] ", nums[i], "\n nums[i-1] ", nums[i-1])#, nums[i+1]])
                            print("\n i even: ",i)
                            # both neighbours must be smaller
                            if nums[i-1] < nums[i]:
                                sorted_arr.append(nums[i])
                                #provisional_i += 1
                                print("\n ADDED ITEM even 1 : ", nums[i], "  to sorted ", sorted_arr)
                                if nums[i] > nums[i+1]:
                                    sorted_arr.append(nums[i+1])
                                    print("\n ADDED ITEM even 2 : ", nums[i+1], "  to sorted ", sorted_arr)
                                    #provisional_i = 1
                                    i = i + 1
                                # print("\n provisional i added ", provisional_i)
                                else:
                                    not_fit_arr.append(nums[i+1])
                                    print("\n NOT FIT even 1 ", not_fit_arr)
                            else:
                                not_fit_arr.append(nums[i])
                                print("\n NOT FIT even 2 ", not_fit_arr)

                        elif i % 2 == 0:
                            print("\n i odd possition i+1 where i is : ",i)
                            # check if nums[i] < [i-1]
                            print("\n nums[i] ", nums[i], "\n nums[i-1] ", nums[i-1])#, nums[i+1]])
                            
                            if nums[i-1] > nums[i]:
                                #add it to the sorted
                                sorted_arr.append(nums[i])
                                #provisional_i += 1
                                print("\n ADDED ITEM: ", nums[i], "  to sorted ", sorted_arr)
                                if nums[i] < nums[i+1]:
                                    sorted_arr.append(nums[i+1])
                                    print("\n SORTED: ", sorted_arr)
                                    # provisional_i += 1
                                    i = i + 1
                                else:
                                    not_fit_arr.append(nums[i+1])
                                    print("\n NOT FIT odd 1 ", not_fit_arr)
                            else:
                                not_fit_arr.append(nums[i])
                                print("\n not fit nums[i] : ", nums[i], " at i: ", i)
                                print("\n NOT FIT arr odd 2 ", not_fit_arr)

                    else:
                        pass # work only with the nums[i] element meaning not i+1

                i = i+1

            self.sort(nums, sorted_arr, not_fit_arr, len_int)

            print("\n ========================= i: ", i)
            # print("\n ========================= provisional i: ", provisional_i)
            # # if i == 1:
            # #     i += provisional_i + 2
            # #     print("======================= i updated ", i)
            # # else:
            # #     i += provisional_i + 1 # +1 because that would be a normal addition
            
            # #i = i + provisional_i
            # print("\n ========================= updated i: ", i)
            # #provisional_i = 0


    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # # I make an array of bol where will have all false for not fitted yet in the lenght of nums
        # # while or for looping through nums take ith item in nums and check if already fitted in the 
        # # array of bol if fitted skip, if not try to fit and assign in bol array as fitted, if it 
        # # does not fit skip the item and go to the next in nums.

        # fitted_bol_arr = [False] * len(nums)
        # #print(fitted_bol_arr, "    ", nums)
        # i = 0
        # sorted_arr = []
        # fitted = True
        # not_sorted = True
        # nr_of_sorted = 0

        # #k = 0
        # while not_sorted:
        # #while k < len(nums): # go over each possition in array to be sorted to fill all possitions one by one
        # #for i in range(len(nums)):
        #     print(i)
        #     if i == 0:
        #         sorted_arr.append(nums[i])
        #         fitted_bol_arr[i] = True
        #         nr_of_sorted = nr_of_sorted + 1
        #         #print(fitted_bol_arr[i])
        #         i = i + 1
        #         print("i + 1 first item on 0 index added i is: ", i)
        #    # print("\n \n sorted array ", sorted_arr)
        #    # go over the nums items till you find suitable item and check if it is not fitted in fitted array.
        #    # if fitted go to the next j.
        #     elif i > 0:
        #         for j in range(len(nums)-1): # do i need -1?  
        #             if fitted_bol_arr[i] != fitted:
                
        #             # else if not the first item
        #                 if i > 0:
        #                     print("\n ############## i ", i, " sorted_array ", sorted_arr)
        #                     #print(i)
        #                     # check if i is not the last i:
        #                     if i+1 <= len(nums)-1:
        #                         print("#############",i)
        #                         # if i is even
        #                         if (i+1) % 2 != 0: 
        #                             print("\n ODD i must be even and possition i+1 must be odd: ",i, " POSITION ODD ", i+1)
        #                             # check if nums[i] < [i-1]
        #                             print("\n nums[i] ", nums[i], "\n nums[i-1] ", nums[i-1])#, nums[i+1]])
                                    
        #                             if nums[i-1] > nums[i]:
        #                                 #add it to the sorted
        #                                 sorted_arr.append(nums[i])
        #                                 nr_of_sorted = nr_of_sorted + 1
        #                                 i = i + 1
        #                                 #provisional_i += 1
        #                                 print("\n ADDED ITEM: ", nums[i], "  to sorted ", sorted_arr)
        #                                 if nums[i] < nums[i+1]:
        #                                     sorted_arr.append(nums[i+1])
        #                                     fitted_bol_arr[i+1] = True
        #                                     print("\n SORTED: ", sorted_arr)
        #                                     # provisional_i += 1
        #                                     nr_of_sorted = nr_of_sorted + 1
        #                                 #   i = i + 1

        #                         elif (i+1) % 2 == 0:
        #                             #print("\n EVEN position in nums[i] ", nums[i], "\n nums[i-1] ", nums[i-1])#, nums[i+1]])
        #                             print("\n EVEEEENNN i must be odd and possition i+1 must be even: ",i, " POSITION EVEN ", i+1)
        #                             # both neighbours must be smaller
        #                             if nums[i-1] < nums[i]:
        #                                 sorted_arr.append(nums[i])
        #                                 fitted_bol_arr[i] = True
        #                                 #provisional_i += 1
        #                                 nr_of_sorted = nr_of_sorted + 1
        #                                 i = i + 1
        #                                 print("\n ADDED ITEM even 1 : ", nums[i], "  to sorted ", sorted_arr)
        #                                 if nums[i] > nums[i+1]:
        #                                     sorted_arr.append(nums[i+1])
        #                                     fitted_bol_arr[i+1] = True
        #                                     print("\n ADDED ITEM even 2 : ", nums[i+1], "  to sorted ", sorted_arr)
        #                                     #provisional_i = 1
        #                                     nr_of_sorted = nr_of_sorted + 1
        #                                     i = i + 1
        #                                 # print("\n provisional i added ", provisional_i)
                    
        #                 if nr_of_sorted == len(nums):
        #                     not_sorted = False                    
   
           # i = i + 1 


        ####### option 2
        # sort the array and pop one from the beginning for odd possitions
        # then pop always the end item from sorted for even possitions until items are in the sorted.    

        sorted_arr = []
        odd_pos_item = 0
        even_pos_item = 0
        previous_even = 0
        previous_odd = 0
        previous_even_index = 0
        previous_odd_index = 0

        count = 0
        rules = 0

      # I MUST DO QUICKSORT  
        quicksorted = [1,1,5,5,6]#[1,1,1,4,5,6]

        for i in range (len(quicksorted)):
            if i == 0:
                first_item_odd = quicksorted.pop(0)
                sorted_arr.append(first_item_odd)

            else:

                if (i+1) % 2 != 0:
                    print("\n possition is ODD ", (i+1))
                    # remember previous odd
                    if (len(sorted_arr)) > 1:
                        print(len(sorted_arr))
                        previous_odd = sorted_arr[len(sorted_arr) - 2]
                        previous_odd_index = len(sorted_arr) - 2

                    odd_pos_item = quicksorted.pop(0)
                    # CHECK IF IT SATISFIES THE RULE and then add
    ###              if rules < 10:
                    # if (len(sorted_arr)-1) > 0:
                    if  sorted_arr[len(sorted_arr) - 1] > odd_pos_item:
                        #add it to the sorted   
                        sorted_arr.append(odd_pos_item)
                        print("\n ODD ",odd_pos_item)
                        rules = rules + 1
                    # if it does not satisfie the rules then swap it with the previous odd
                    else:
                        # swap previous number which is even with even before that.
                        print("\n PRINTING previous even: ", previous_even, " with the possition: ", previous_even_index)
                        current_even = sorted_arr[len(sorted_arr)-1]
                        print("\n #################### previsou even ", previous_even, " should be same as ",  sorted_arr[(previous_even_index)])                        
                        print("\n #################### current even ", current_even, " should be same as ",  sorted_arr[len(sorted_arr) - 1])
                        sorted_arr[len(sorted_arr) - 1] =  previous_even

                        sorted_arr[previous_even_index] = current_even #pre_previous_even
                        sorted_arr.append(odd_pos_item)

                    print("\n SORTED odd ",sorted_arr)
                elif (i+1) % 2 == 0:
                    print("\n possition is EVEN ", (i+1))
                    if (len(sorted_arr)) > 1:
                        print(len(sorted_arr))
                    # remember previous even from already sorted - this means not the last added but before thus -2
                        previous_even = sorted_arr[len(sorted_arr) - 2]
                        previous_even_index = len(sorted_arr) - 2
                        #count = count + 1

                    even_pos_item = quicksorted.pop()
                    print("\n EVEN item ",even_pos_item)
                    # CHECK IF IT SATISFIES THE RULE and then add
    ####               if rules < 3:
                    #if (len(sorted_arr)-1) > 0:
                    if sorted_arr[len(sorted_arr) - 1] < even_pos_item:
                        print("\n adding ", even_pos_item)
                        sorted_arr.append(even_pos_item)
                        rules = rules + 1
                       # print("\n rules number become ", rules)
                    # if it does not satisfie the rules then swap it with the previous odd
                    else:
                        print("\n PRINTING previous odd: ", previous_odd, " with the possition: ", len(sorted_arr) - 2)
                        current_odd = sorted_arr[len(sorted_arr)-1]
                        print("\n #################### previsou even ", previous_odd, " should be same as ",  sorted_arr[(previous_odd_index)])                        
                        print("\n #################### current even ", current_odd, " should be same as ",  sorted_arr[len(sorted_arr) - 1])
                        sorted_arr[len(sorted_arr) - 1] =  previous_odd

                        sorted_arr[previous_odd_index] = current_odd #pre_previous_even
                        sorted_arr.append(even_pos_item)

                        
                    print("\n SORTED even ",sorted_arr)
            


        return sorted_arr

arr = [1,1,5,5,6]
# [1,6,1,5,5]
# my solution will have an issue if 
# [1,5,1,6,5]





nums = [1,5,1,1,6,4]
#nums = [1,6,1,5,1,4] # dummy example sorted works well.
solution = Solution()
#solution.wiggleSort(nums)
print(solution.wiggleSort(nums))




