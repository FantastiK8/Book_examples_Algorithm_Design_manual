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
    def get_nr_nodes(head):
        nr_nodes = 0
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

        # When the input rotation start to be repetitive? based on that k can be reduced.
        # e.g. head input of 2 nodes become repepetive: 1,2 => 2,1 (r=1), 1,2 (r=2)
        # e.g. head input of 3 nodes become repepetive: 1,2,3 => 3,1,2 (r=1), 2,3,1 (r=2), 1,2,3 (r=3)
        # e.g. head input of 4 nodes become repepetive: 1,2,3,4 => 4,1,2,3 (r=1)=> 3,4,1,2 (r=2), 2,3,4,1 (r=3), 1,2,3,4 (r=4)
        
        if (head is None):
            return None

        if k == 0 :
            return head

        nr_nodes = get_nr_nodes(head)


        print("\n HEAD START ", head)

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
                    
                    # print("\n head ", head)
                    # print("\n connection head ", connection_head )
                    # print("\n last node ", last_node)


                    previous_node = head_copy
                    next_node = head_copy.next
                    if i == 0:
                        nr_nodes +=1
                    print("\n HEAD 1", head)
                    if next_node.next is None:# or head_copy.next is None:
                        print("\n next node:   ", next_node.next)
                       #print("\n head_copy.next node:   ", head_copy.next)
                        counter += 1
                        previous_node.next = None # remove the link to the last node
                        previous_node = last_node
                        last_node = next_node 
                        print("\n last_node: ", last_node, " counter: ", counter, " nr of nodes ", nr_nodes)
                        if counter == 1: # or nr_nodes == 2:
                            print("HEAD HERE ", head)
                            last_node.next = connection_head 
                            print("\n last node: ", last_node, " \n WHAT HAPPENED TO HEAD: ", connection_head)
                        else: 
                            last_node.next = previous_node
                            print("\n \n last_node!!!!1: ", last_node)


                    elif head_copy.next is not None:
                        head_copy = head_copy.next

                head_copy = last_node

                #print("\n k : ", k, "  and nr_nodes ", nr_nodes)
                if i == 0:
                    if k >= nr_nodes and nr_nodes > 0: # k => how many times to rotate and nr_nodes => the number of nodes in head
                        remining = k % nr_nodes #
                        print("\n REMAINING ", remining)
                        if remining == 0:
                            print("\n HEAD ", head)
                            return head
                        else:
                            provisional_k = k - remining 
                            print("\n PROVISIONAL K after - remining ", provisional_k, "  remining ", remining)
                            #provisional_k = provisional_k/nr_nodes
                            #print("\n PROVISIONAL K ", provisional_k)
                            provisional_k = remining - 1 # 1 => already done one itteration.
                            print("\n PROVISIONAL K after remining added ", provisional_k)
                            print("\n remining ", remining)
                            k = provisional_k
                            print("\n k is now: ", k)
            
        rotated_head = last_node

        print("\n head ", head)
        print("\n connection head ", connection_head )
        print("\n last node ", last_node)
        print("\n rotated_head", rotated_head)

        print("\n2", rotated_head, "\n")
        return rotated_head






# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
#print(head)

#head = ListNode(1, ListNode(2, ListNode(3, None)))
head = ListNode(1, ListNode(2, None))
#head = ListNode(1, None)
#k = 2000000000 # 2,000,000,000 
k = 2
solution = Solution()
solution.rotateRight(head, k)
# print(solution.rotateRight(head, k))


##########
