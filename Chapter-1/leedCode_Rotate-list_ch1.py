# Given the head of a linked list, rotate the list to the right by k places.

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:


# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
 

# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109


# Definition for singly-linked list.
class Iterator:
   ''' Iterator class '''
   def __init__(self, head):
       # Team object reference
       self._head = head
       # member variable to keep track of current index
       self._index = 0

#    def __next__(self):
#        ''''Returns the next value from team object's lists '''
#        if self._index < (len(self._team._juniorMembers) + len(self._team._seniorMembers)) :
#            if self._index < len(self._team._juniorMembers): # Check if junior members are fully iterated or not
#                result = (self._team._juniorMembers[self._index] , 'junior')
#            else:
#                result = (self._team._seniorMembers[self._index - len(self._team._juniorMembers)]   , 'senior')
#            self._index +=1
#            return result
#        # End of Iteration
#        raise StopIteration

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# I added this for me to be able to see it printed in SVC the same way as it is in LeetCode
    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"

    def __iter__(self):
       ''' Returns the Iterator object '''
       return Iterator(self)


class Solution(object):
    
    def get_nr_nodes(self, head):
        nr_nodes = 1 # starting with 1 because the while loop goes with head.next which does not includ the first node.
        while head.next is not None:
            nr_nodes +=1
            head = head.next
        return nr_nodes
    
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if (head is None):
            return None

        if k == 0 :
            return head

        nr_nodes = self.get_nr_nodes(head)
        

        if 0 > k >= 2 * 10^9 or nr_nodes >= 500:
            return None
        
        if k >= nr_nodes and nr_nodes > 0: # k => how many times to rotate and nr_nodes => the number of nodes in head
            remining = k % nr_nodes #
            if remining == 0:

                return head
            else:
                provisional_k = k - remining 
               
                provisional_k = remining # 1 => already done one itteration.
                # print("\n PROVISIONAL K after remining added ", provisional_k)
                # print("\n remining ", remining)
                k = provisional_k
                # print("\n k is now: ", k)

        #print("\n HEAD START ", head)

        head_copy = head
        connection_head = head
        last_node = ListNode()
        counter = 0
        nr_nodes = 1
        for i in range(k):

            if head_copy.next is None:
                  #  print("here ", head)
                    return head
            else:         
                while head_copy.next is not None:

                    previous_node = head_copy
                    next_node = head_copy.next
                    # if i == 0:
                    #     nr_nodes +=1
                    #print("\n HEAD 1", head)
                    if next_node.next is None:# or head_copy.next is None:
                       # print("\n next node:   ", next_node.next)
                       #print("\n head_copy.next node:   ", head_copy.next)
                        counter += 1
                        previous_node.next = None # remove the link to the last node
                        previous_node = last_node
                        last_node = next_node 
                        #print("\n last_node: ", last_node, " counter: ", counter, " nr of nodes ", nr_nodes)
                        if counter == 1: # or nr_nodes == 2:
                           # print("HEAD HERE ", head)
                            last_node.next = connection_head 
                           # print("\n last node: ", last_node, " \n WHAT HAPPENED TO HEAD: ", connection_head)
                        else: 
                            last_node.next = previous_node
                            #print("\n \n last_node!!!!1: ", last_node)


                    elif head_copy.next is not None:
                        head_copy = head_copy.next

                head_copy = last_node
            
        rotated_head = last_node

        #print("\n2", rotated_head, "\n")
        return rotated_head



#head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
#print(head)
head = ListNode(0, ListNode(1, ListNode(2, None)))
#head = ListNode(1, ListNode(2, ListNode(3, None)))
#head = ListNode(1, ListNode(2, None))
#head = ListNode(1, None)
#k = 2000000000 # 2,000,000,000 
k = 4
solution = Solution()
#solution.rotateRight(head, k)
print(solution.rotateRight(head, k))

