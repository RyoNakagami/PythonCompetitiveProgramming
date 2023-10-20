#%%
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Problem

        You are given two non-empty linked lists representing two non-negative integers. 
        The digits are stored in reverse order, and each of their nodes contains a single digit. 
        Add the two numbers and return the sum as a linked list.

        You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    """
    def compute_number(self, listnode):
        state = listnode
        total = 0
        exp = 0
        while state is not None:
            total = total + 10**(exp) * state.val
            state = state.next
            exp += 1
        return total

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = self.compute_number(l1) + self.compute_number(l2)
        return ListNode(','.join(list(str(total)[::-1])))
