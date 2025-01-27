class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution: 
    def reverseLinkList(self, head):
        curr = head
        prev = None 
        while curr: 
            temp = curr.next
            curr.next = prev 
            prev = curr 
            curr = temp 
        return prev 
    

head = ListNode(1, ListNode(2, ListNode(3)))

solution = Solution()
reversed_head = solution.reverseLinkList(head)

current = reversed_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

"""
time = O(N)
space = O(1)
"""