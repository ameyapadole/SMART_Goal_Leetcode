import collections

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left
        self.right = right

class Solution: 
    def invertBinaryTree(root):
        if not root:
            return None 

        q = collections.deque([root])
        while q: 
            curr = q.popleft()
            curr.left, curr.right = curr.right, curr.left 

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return root 
    
"""
Time Complexity = O(N)
Space Complexity = O(1)
"""