##########################
# 739. Daily Temperatures
##########################
# Given an array of integers temperatures represents the daily temperatures, return an array answer such 
# that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.
# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]

# Constraints:
# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

#############################################################
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        if 0 > len(temperatures) > 105:
            return

        highest_temp = 0
        highest_temp_i = - 1
        day_count = 0
        days = 0
        days_arr = []#len(temperatures)

        for i, temp in enumerate(temperatures):
            print("days each iter: ", days_arr)
            print(" days ", days)
            print("temp each iter: ", temp, " :  i: ", i)
            
            # if i == len(temperatures) - 1:
            #     days_arr.append(0)
           
            if i == 0:
                highest_temp = temp
                highest_temp_i = i
            else:
                if highest_temp < temp:
                    days = (i) - (highest_temp_i)
                    days_arr.append(days)

                    
                    # print("#################days ", days)
                    # if days > 1:
                    #     # CALCULATE THE MISSING SPACES IN THE NEW ARRAY
                    #     for j, temp2 in enumerate(temperatures[highest_temp_i + 1 : i - 1]):
                    #         previous_highest_temp = temperatures[highest_temp_i + j]
                    #         preivous_temp_i = highest_temp_i + j
                    #         print("previous temp: ", previous_highest_temp, " AND its i: ", preivous_temp_i)



                    

            
        

        print(days_arr)
temperatures = [73,74,75,71,69,72,76,73]
#temperatures = [30,40,50,60]
#temperatures = [30,60,90]
solution = Solution()
solution.dailyTemperatures(temperatures)