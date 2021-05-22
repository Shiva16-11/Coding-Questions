# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode:
    def __init__(self, val=0, next =None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode()
        head = l3
        c = 0

        while l1 or l2:
            temp = 0
            if l1 is None:
                temp = l2.val + c

                l2 = l2.next
            elif l2 is None:
                temp = l1.val + c
                l1 = l1.next
            else:
                temp = l1.val + l2.val + c
                l1 = l1.next
                l2 = l2.next

            c = temp // 10
            temp = temp % 10
            l3.next = ListNode(temp)

            l3 = l3.next
        if c != 0:
            l3.next = ListNode(c)
        return head.next