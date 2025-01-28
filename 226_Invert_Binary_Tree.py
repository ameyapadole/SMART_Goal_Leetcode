class TreeNode: 
    def __init__(self, left = None, right = None, val = 0):
        self.val = val 
        self.left = left
        self.right = right
class Solution:
    def invertBinaryTree(self, root):
        if not root:
            return None 
        temp = root.left 
        root.left = root.right
        root.right = temp 

        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)

        return root 
    

"""
Time = O(N)
Space = O(N), call stack for recursive will take N space. 

"""
