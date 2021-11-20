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



####### option 3
# sort the array and pop one from the beginning for odd possitions --> merge sort has the best performance in terms of
# time complexity Best, Average and Worst case is always O(N log2 N)
# nums --> [1,1,1,4,5,6]
# i = 0
# nr_sorted_elements = 0
# while nr_sorted_elements < then the len(nums) # means 6
# pop last element 6 and put it after the index = 0 which has value 1 SO IT MEANS insert in index i+1 = 1, 
# increase nr_sorted_elements by 2 and i increase by 2
#==> i = 2, nr_sorted_elements = 2, current nums --> [1,6,1,1,4,5]
# Repeat:
# pop last element 5 and put it after the element with index = 2 which has value 1 SO IT MEANS insert in index i+1 = 3 
# increase nr_sorted_elements by 2 and i increase by 2
#==> i = 4, nr_sorted_elements = 4, current nums --> [1,6,1,5,1,4]
# repeat: 
# pop last element 4 and put it after the element with index = 4 which has value 1 SO IT MEANS insert in index i+1 = 5 
# increase nr_sorted_elements by 2 and i increase by 2
#==> i = 6, nr_sorted_elements = 6, current nums --> [1,6,1,5,1,4]

 
class Solution(object):
    def bubbleSort(self, nums):
        #nr_itterations = 0
        swapped = True
        while(swapped):
            swapped = False
            for i in range(len(nums) -1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swapped = True

    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """  
        len_nums = len(nums)

        if len_nums == 1:
            return nums

        print(nums)
        self.bubbleSort(nums)


# while nr_sorted_elements < then the len(nums) # means 6
# pop last element 6 and put it after the index = 0 which has value 1 SO IT MEANS insert in index i+1 = 1, 
# increase nr_sorted_elements by 2 and i increase by 2
#==> i = 2, nr_sorted_elements = 2, current nums --> [1,6,1,1,4,5]
# Repeat:
# pop last element 5 and put it after the element with index = 2 which has value 1 SO IT MEANS insert in index i+1 = 3 
# increase nr_sorted_elements by 2 and i increase by 2
#==> i = 4, nr_sorted_elements = 4, current nums --> [1,6,1,5,1,4]
# repeat: 
# pop last element 4 and put it after the element with index = 4 which has value 1 SO IT MEANS insert in index i+1 = 5 
# increase nr_sorted_elements by 2 and i increase by 2
#==> i = 6, nr_sorted_elements = 6, current nums --> [1,6,1,5,1,4]
        

        nr_sorted = 0
        i = 0
       
        

        while i < len_nums:# and nr_sorted < len_nums: # -1:
            print("############rn of sorted: ", nr_sorted)
            print("I IS ", i)
            # end_element = nums.pop()
            print("len nums", len_nums)
           # print("nums 1 positions ", nums[1])
            #print("end element ", end_element)
            print(nums)
            print(i)
            print(len(nums))
            end_element_index = len_nums - 1
            end_element = nums.pop()
            print("end element index ", end_element_index)
            if end_element_index != i:

            # if num[i] != (len(nums) -):
                if end_element > nums[i]: # add only if it satisfies the exception
                    # print("here i is ", i, " and nr of sorted elements ", nr_sorted, " the lenght is ", len(nums))
                    nums.insert(i + 1, end_element)
                    i = i + 2
                    nr_sorted = nr_sorted + 2
                else: # swap the current even item with the first even element
                    # print("HEREEE")
                    first_even = nums[1]
                    print("00000000000000000previous even ", first_even)
                    print(nums)
                    print("#=============== nums[i]", nums[i])
                    print("#=============== end element  ", end_element)
                    nums.insert(i + 1, first_even)
                    
                    
                    print("nums after insertion \n ", nums)
                    nums.pop(1)
                    print("nums after pop  \n", nums)
                    nums.insert(1, end_element)
                    print("nums after insertion \n", nums)
                    #nums[1] = end_element
                    nr_sorted = nr_sorted + 2
                    i = i + 2
            else:
                print("hereeeeeeeeeeeeeeeeeeeeeeee")
                print(i)
                print(nums)
                print(len(nums))
                end_element_index = len_nums - 1
                print("end element index ", end_element_index)
                
                print(end_element)
                print("i-1 element ", nums[i-1])

                if (len_nums % 2 == 0):# or (len_nums % 2 == 0 and end_element == nums[i-1]): # if the last number is even:
                    if end_element <= nums[i-1]:
                        first_even = nums[1]
                        print("previous even ", first_even)
                        
                        print("#=============== nums[i-1]", nums[i-1])
                        print(nums)
                        nums.insert(i-1, first_even)
                        print("nums after insertion \n ", nums)
                        nums.pop(1)
                        print("nums after pop  \n", nums)
                        nums.insert(1, end_element)
                        print("nums after insertion \n", nums)
                        #nums[1] = end_element
                        nr_sorted = nr_sorted + 1
                        i = i + 100
                    else:
                        nums.append(end_element)
                        i = i + 100
                        nr_sorted = nr_sorted + 1

                elif len_nums % 2 != 0:# or (len_nums % 2 != 0 and end_element == nums[i-1]): #odd number of elements
                    if end_element >= nums[i-1]:
                        first_odd = nums[0]
                        print("firsst odd ", first_odd)
                        print("end element ", end_element)
                        print("#=============== nums[i-1]", nums[i-1])
                        print("before end ", nums[i-1])
                        print("#######first odd ", first_odd)
                        print(nums)
                        nums.append(first_odd)
                        print("####nums after insertion \n ", nums)
                        nums.pop(0)
                        print("####nums after pop  \n", nums)
                        nums.insert(0, end_element)
                        print("nums after insertion \n", nums)
                        #nums[1] = end_element
                        nr_sorted = nr_sorted + 1
                        i = i + 100
                    else:
                        nums.append(end_element)
                        i = i + 100
                        nr_sorted = nr_sorted + 1
  
                
               
                #if nr_sorted < len(nums) and i 
                
                # if (i - 1) > 0:
                #     previous_even = nums[i - 1]
                #     nums.insert(i + 1, previous_even)
                #     nums[i - 1] = end_element
                #     nr_sorted = nr_sorted + 2
                #     insterted = True



                # if not insterted:
                #     if (i - 3) > 0:
                #         previous_even = nums[i - 1]
                #         nums.insert(i + 1, previous_even)
                #         nums[i - 2] = end_element
                #         nr_sorted = nr_sorted + 2
                        
                    # else:
                    #     if (i + 3) < len(nu)

        print("\n \n sorted \n", copy_nums)
        print("Solution should be: \n [5, 6, 4, 5]" )
        print("final \n", nums)



#nums = [1]
nums = [4,5,5,6]
# nums = [1,4,3,4,1,2,1,3,1,3,2,3,3]
#nums = [1,1,2,1,2,2,1]
#nums =[1,3,2,2,3,1]
#nums = [1,5,1,1,6,4]
#nums = [1,3,2,2,3,1]
#nums = [1,5,1,1,6,4]
#nums = [1,6,1,5,1,4] # dummy example sorted works well.
solution = Solution()
#solution.wiggleSort(nums)
print(solution.wiggleSort(nums))










    #     sorted_arr = []
    #     odd_pos_item = 0
    #     even_pos_item = 0
    #     previous_even = 0
    #     previous_odd = 0
    #     previous_even_index = 0
    #     previous_odd_index = 0

    #     count = 0
    #     rules = 0

    #   # I MUST DO QUICKSORT  
    #     nums = sorted(nums) #[1,1,5,5,6]#[1,1,1,4,5,6]
    #     print(nums)

    #     for i in range (len(nums)):
    #         if i == 0:
    #             first_item_odd = nums.pop(0)
    #             sorted_arr.append(first_item_odd)

    #         else:

    #             if (i+1) % 2 != 0:
    #                 print("\n possition is ODD ", (i+1))
    #                 # remember previous odd
    #                 if (len(sorted_arr)) > 1:
    #                     print(len(sorted_arr))
    #                     previous_odd = sorted_arr[len(sorted_arr) - 2]
    #                     previous_odd_index = len(sorted_arr) - 2

    #                 odd_pos_item = nums.pop(0)
    #                 # CHECK IF IT SATISFIES THE RULE and then add
    # ###              if rules < 10:
    #                 # if (len(sorted_arr)-1) > 0:
    #                 if  sorted_arr[len(sorted_arr) - 1] > odd_pos_item:
    #                     #add it to the sorted   
    #                     sorted_arr.append(odd_pos_item)
    #                     print("\n ODD ",odd_pos_item)
    #                     rules = rules + 1
    #                 # if it does not satisfie the rules then swap it with the previous odd
    #                 else:
    #                     # swap previous number which is even with even before that.
    #                     print("\n PRINTING previous even: ", previous_even, " with the possition: ", previous_even_index)
    #                     current_even = sorted_arr[len(sorted_arr)-1]
    #                     print("\n #################### previsou even ", previous_even, " should be same as ",  sorted_arr[(previous_even_index)])                        
    #                     print("\n #################### current even ", current_even, " should be same as ",  sorted_arr[len(sorted_arr) - 1])
    #                     sorted_arr[len(sorted_arr) - 1] =  previous_even

    #                     sorted_arr[previous_even_index] = current_even #pre_previous_even
    #                     sorted_arr.append(odd_pos_item)

    #                 print("\n SORTED odd ",sorted_arr)
    #             elif (i+1) % 2 == 0:
    #                 print("\n possition is EVEN ", (i+1))
    #                 if (len(sorted_arr)) > 1:
    #                     print(len(sorted_arr))
    #                 # remember previous even from already sorted - this means not the last added but before thus -2
    #                     previous_even = sorted_arr[len(sorted_arr) - 2]
    #                     previous_even_index = len(sorted_arr) - 2
    #                     #count = count + 1

    #                 even_pos_item = nums.pop()
    #                 print("\n EVEN item ",even_pos_item)
    #                 # CHECK IF IT SATISFIES THE RULE and then add
    # ####               if rules < 3:
    #                 #if (len(sorted_arr)-1) > 0:
    #                 if sorted_arr[len(sorted_arr) - 1] < even_pos_item:
    #                     print("\n adding ", even_pos_item)
    #                     sorted_arr.append(even_pos_item)
    #                     rules = rules + 1
    #                    # print("\n rules number become ", rules)
    #                 # if it does not satisfie the rules then swap it with the previous odd
    #                 else:
    #                     print("\n PRINTING previous odd: ", previous_odd, " with the possition: ", len(sorted_arr) - 2)
    #                     current_odd = sorted_arr[len(sorted_arr)-1]
    #                     print("\n #################### previsou even ", previous_odd, " should be same as ",  sorted_arr[(previous_odd_index)])                        
    #                     print("\n #################### current even ", current_odd, " should be same as ",  sorted_arr[len(sorted_arr) - 1])
    #                     sorted_arr[len(sorted_arr) - 1] =  previous_odd

    #                     sorted_arr[previous_odd_index] = current_odd #pre_previous_even
    #                     sorted_arr.append(even_pos_item)

                        
    #                 print("\n SORTED even ",sorted_arr)
            

    #     print(" FINAL OUTPUT ", sorted_arr)
    #     return sorted_arr

#arr = [1,1,5,5,6]
# [1,6,1,5,5]
# my solution will have an issue if 
# [1,5,1,6,5]

# #nums = [1,4,3,4,1,2,1,3,1,3,2,3,3]
# nums = [1,1,2,1,2,2,1]
# # nums = [1,1,2,1,2,2,1]#
# #nums =[1,3,2,2,3,1]
# #nums = [1,5,1,1,6,4]
# #nums = [1,3,2,2,3,1]
# #nums = [1,5,1,1,6,4]
# #nums = [1,6,1,5,1,4] # dummy example sorted works well.
# solution = Solution()
# #solution.wiggleSort(nums)
# print(solution.wiggleSort(nums))


# #### options:
# # I make an array of bol where will have all false for not fitted yet in the lenght of nums
# # while looping through nums take ith item in nums and check if already fitted in the array of bol
# # if fitted skip, if not try to fit and assign in bol array as fitted, if it does not fit skip the item and go to the next in nums.
# ####### option 2
# # sort the array and pop one from the beginning for odd possitions
# # then pop always the end item from sorted for even possitions until items are in the sorted.
# class Solution(object):

#     def wiggleSort(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
       

#         ####### option 2
#         # sort the array and pop one from the beginning for odd possitions
#         # then pop always the end item from sorted for even possitions until items are in the sorted.    

#         sorted_arr = []
#         odd_pos_item = 0
#         even_pos_item = 0
#         previous_even = 0
#         previous_odd = 0
#         previous_even_index = 0
#         previous_odd_index = 0

#         count = 0
#         rules = 0

#       # I MUST DO QUICKSORT  
#         nums = sorted(nums) #[1,1,5,5,6]#[1,1,1,4,5,6]
#         print(nums)

#         for i in range (len(nums)):
#             if i == 0:
#                 first_item_odd = nums.pop(0)
#                 sorted_arr.append(first_item_odd)

#             else:

#                 if (i+1) % 2 != 0:
#                     print("\n possition is ODD ", (i+1))
#                     # remember previous odd
#                     if (len(sorted_arr)) > 1:
#                         print(len(sorted_arr))
#                         previous_odd = sorted_arr[len(sorted_arr) - 2]
#                         previous_odd_index = len(sorted_arr) - 2

#                     odd_pos_item = nums.pop(0)
#                     # CHECK IF IT SATISFIES THE RULE and then add
#     ###              if rules < 10:
#                     # if (len(sorted_arr)-1) > 0:
#                     if  sorted_arr[len(sorted_arr) - 1] > odd_pos_item:
#                         #add it to the sorted   
#                         sorted_arr.append(odd_pos_item)
#                         print("\n ODD ",odd_pos_item)
#                         rules = rules + 1
#                     # if it does not satisfie the rules then swap it with the previous odd
#                     else:
#                         # swap previous number which is even with even before that.
#                         print("\n PRINTING previous even: ", previous_even, " with the possition: ", previous_even_index)
#                         current_even = sorted_arr[len(sorted_arr)-1]
#                         print("\n #################### previsou even ", previous_even, " should be same as ",  sorted_arr[(previous_even_index)])                        
#                         print("\n #################### current even ", current_even, " should be same as ",  sorted_arr[len(sorted_arr) - 1])
#                         sorted_arr[len(sorted_arr) - 1] =  previous_even

#                         sorted_arr[previous_even_index] = current_even #pre_previous_even
#                         sorted_arr.append(odd_pos_item)

#                     print("\n SORTED odd ",sorted_arr)
#                 elif (i+1) % 2 == 0:
#                     print("\n possition is EVEN ", (i+1))
#                     if (len(sorted_arr)) > 1:
#                         print(len(sorted_arr))
#                     # remember previous even from already sorted - this means not the last added but before thus -2
#                         previous_even = sorted_arr[len(sorted_arr) - 2]
#                         previous_even_index = len(sorted_arr) - 2
#                         #count = count + 1

#                     even_pos_item = nums.pop()
#                     print("\n EVEN item ",even_pos_item)
#                     # CHECK IF IT SATISFIES THE RULE and then add
#     ####               if rules < 3:
#                     #if (len(sorted_arr)-1) > 0:
#                     if sorted_arr[len(sorted_arr) - 1] < even_pos_item:
#                         print("\n adding ", even_pos_item)
#                         sorted_arr.append(even_pos_item)
#                         rules = rules + 1
#                        # print("\n rules number become ", rules)
#                     # if it does not satisfie the rules then swap it with the previous odd
#                     else:
#                         print("\n PRINTING previous odd: ", previous_odd, " with the possition: ", len(sorted_arr) - 2)
#                         current_odd = sorted_arr[len(sorted_arr)-1]
#                         print("\n #################### previsou even ", previous_odd, " should be same as ",  sorted_arr[(previous_odd_index)])                        
#                         print("\n #################### current even ", current_odd, " should be same as ",  sorted_arr[len(sorted_arr) - 1])
#                         sorted_arr[len(sorted_arr) - 1] =  previous_odd

#                         sorted_arr[previous_odd_index] = current_odd #pre_previous_even
#                         sorted_arr.append(even_pos_item)

                        
#                     print("\n SORTED even ",sorted_arr)
            

#         print(" FINAL OUTPUT ", sorted_arr)
#         return sorted_arr

# #arr = [1,1,5,5,6]
# # [1,6,1,5,5]
# # my solution will have an issue if 
# # [1,5,1,6,5]



# nums = [1,5,1,1,6,4]

# #nums = [1,5,1,1,6,4]
# #nums = [1,6,1,5,1,4] # dummy example sorted works well.
# solution = Solution()
# #solution.wiggleSort(nums)
# print(solution.wiggleSort(nums))





