# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution(object):
#     def rotateRight(self, head, k):
#         """
#         :type head: ListNode
#         :type k: int
#         :rtype: ListNode
#         """
#         #rotated_list = head.copy()

#         for i in range(k):

#             last_item = head.pop()
#             head.insert(0, last_item)

#         return head


# head = [1,2,3,4,5]
# k = 2
# solution = Solution()
# print(solution.rotateRight(head, k))




# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if (head is None):
            return None
        
        head_copy = head
        last_node = ListNode()
        counter = 0

        if k == 0 :
            return head
        
        for i in range(k):

            if head_copy.next is None:
                  #  print("here ", head)
                    return head
            else:         
                while head_copy.next is not None:
                    
                    previous_node = head_copy
                    next_node = head_copy.next

                    if next_node.next is None:
                     #   print(next_node.next)
                        counter += 1
                        previous_node.next = None # remove the link to the last node
                        previous_node = last_node
                        last_node = next_node 
                        if counter == 1:
                            last_node.next = head 
                        else: last_node.next = previous_node

                    elif head_copy.next is not None:
                        head_copy = head_copy.next

                head_copy = last_node
        
        rotated_head = last_node
            
        print(rotated_head)
        return rotated_head


# class Solution(object):
#     def rotateRight(self, head, k):
#         """
#         :type head: ListNode
#         :type k: int
#         :rtype: ListNode
#         """
# ### print(head) #=> output ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}

   
#         # head is the main first Node and that one contain the nested next Node(s)
# # OPTIONS:
# ######## 1. 
# #        loop through the linked list to get lenght of the linked list and "pop" (=remove and store in new node) the final node and its information.
# #    
# #        insert at the beginning and add info e.g. to the next node, head initialisatin.     
# #        
# #        loop k-1 times to repeat: remove last node - stored info thanks to the lenght of the linkedList, and insert it to the biginning + add information such as a new link to the next node
      
#       #PSEUDO CODE:
#         # for i in range(k):
#             # for node in head: 
#                 #if node.next == null 
#                     #last_node = node
#                     #remove node
#                     #remove link from previous
#                     #add removed node to head and add info to next.
#                 #previous_node = node
            
# # 
# # 
# #     

#         # rotated_head = ListNode(444, head)
#         #print(rotated_head)
#         ######rotated_head = ListNode()
#         head_copy = head
#         last_node = ListNode()
#         counter = 0

#         for i in range(k):
            
#             #print(head_copy)
            
#             while head_copy.next is not None:
#                     #print("test")
#               #  print("HEAD COPY BEFORE CHANGE ", head_copy)
#                # last_node = head_copy
#                 previous_node = head_copy
#                 print("\n HEAD_COPY/previous node  ", head_copy)
#                 next_node = head_copy.next
#                 print("\n next_node ", next_node)
                
#                # print("\n ROTATE SO FAR BULIT:   ", rotated_head)
                
#                 if next_node.next is None:
#                     counter += 1
#                     previous_node.next = None # remove the link to the last node
#                     print("\n previous node: ", previous_node)
#                     previous_node = last_node
#                     last_node = next_node #in the while loop I already moved to next node
#                     print("last node:   ",last_node)
#                     #print(head)
#                     if counter == 1:
#                         last_node.next = head # BUG !!!!!!!!!!!!!! HERE setting last node at the beginning of the head.
#                     else: last_node.next = previous_node

#                     print("last node to seeeeeeeeee  ", last_node)
#                     # rotated_head = last_node # for clarity I made a new attribute
#                     # print("#####TEST ROTATED HEAD IN PROGRESS",rotated_head, "\n")
#                     # head_copy = rotated_head
#                     # print("----------- TEST IF HEAD_COPY WHENT WELL ", head_copy, "\n")
#                     # # head_copy = rotated_head

#                 elif head_copy.next is not None:
#                     head_copy = head_copy.next

#             head_copy = last_node
        
#         rotated_head = last_node
            
#                 #print(last_node)
#                 #print("####HEAD COPY FATER UPDATE  ", head_copy)
                
#       #  print(rotated_head)        
#             #print("testing this area")
#             # last_node.next = head
#             #print("#####TESTING PRINTING NEW ROTATED HEAD ", last_node)
#             # rotated_head = last_node
#             # print(rotated_head)
#         #print(rotated_head)
#         return rotated_head







# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
#print(head)

head = ListNode(1, ListNode(2, ListNode(3, None)))
#head = ListNode(1, None)
k = 2000000000
solution = Solution()
solution.rotateRight(head, k)
# print(solution.rotateRight(head, k))



