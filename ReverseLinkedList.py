# ID: 206
# URL: https://leetcode.com/problems/reverse-linked-list/
# Difficulty: Easy


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class RecursiveSolution:
    """
    Recursive solution to reversing a linked list in place.

    """
    def reverseList(self, head: ListNode) -> ListNode:
        """
        :param head: head node of the linked list to be reversed
        :returns: head node of the reversed linked list
        """
        # head doesn't exist
        if head is None:
            return
        # call helper function
        head=self.reverseHelper(head, None)
        return head
        
        
    def reverseHelper(self, curr, prev):
        """
        Recursive helper function to reverse a linked list in place.
        :param curr: current node of the linked list (begin at the head)
        :param prev: previous node of the linked list
        :returns: head (first node) of the reversed linked list

        """
        # base case reached the end, next node is None
        if curr.next is None:
            curr.next=prev
            
            return curr
        # base case the head is None
        if curr is None:
            return curr
        # reverse the way the current node points to be the previous node
        next=curr.next
        curr.next=prev
        return self.reverseHelper(next, curr)
        