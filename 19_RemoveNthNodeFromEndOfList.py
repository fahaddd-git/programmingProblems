# ID: 19
# URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Difficulty: Medium
# Description: Given the head of a linked list, remove the nth node from the end of the list and return its head.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        algorithm:
        - if the next node is None return ListNode("")
        - create a counter
        - create a pointer to the head of the linked list
        - iterate through the linked list adding 1 to the counter each time next is not None
        - subtract n from the counter 
        - create pointer to head node
        - iterate through the linked list to counter-1 position
            - set next ListNode counter-1 to equal ListNode counter+1
        - return head
        """
        # only 1 node in linked list
        if head.next is None:
            head.val=""
            return head
        
        counter=1
        
        head_node=head
        
        while head.next is not None:
            head=head.next
            counter+=1
            
        # location of element to be removed
        counter=counter-n

        # edge case, head to be removed
        if counter==0:
            return head_node.next
        
        prev=head_node
        
        # iterate to the node to be removed -1
        for node in range(counter-1):
            prev=prev.next

        # set the previous node to node to be removed +1
        if prev.next is not None:
            prev.next=prev.next.next
        else:
            prev.next=None
        
        # return beginning of linked list
        return head_node
            
            
            