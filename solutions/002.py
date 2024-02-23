# https://leetcode.com/problems/add-two-numbers

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    head = None

    def insertAtEnd(self, val):
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node

    def get_leading_number(self, latest_sum):
        leading_number = 0

        if (len(str(latest_sum)) > 1):
            leading_number = str(latest_sum)[0]

        return int(leading_number)


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        latest_sum = 0

        current_l1_node = l1
        current_l2_node = l2

        while (current_l1_node != None or current_l2_node != None):
            leading_number = self.get_leading_number(latest_sum)
            l1_node_val = current_l1_node.val if current_l1_node != None else 0
            l2_node_val = current_l2_node.val if current_l2_node != None else 0
            latest_sum = l1_node_val + l2_node_val + leading_number

            new_value = str(latest_sum)[len(str(latest_sum)) - 1]
            
            self.insertAtEnd(new_value)

            if (current_l1_node != None):
                current_l1_node = current_l1_node.next
            
            if (current_l2_node != None):
                current_l2_node = current_l2_node.next
            
            if (int(len(str(latest_sum)) > 1) and current_l1_node == None and current_l2_node == None):
                leading_number = self.get_leading_number(latest_sum)
                self.insertAtEnd(leading_number)
        
        return self.head
            

solution = Solution()
l1_node = ListNode(5)
l2_node = ListNode(5)

new_node = solution.addTwoNumbers(l1_node, l2_node)

while (new_node.next != None):
    print(new_node.val)
    new_node = new_node.next

print(new_node.val)