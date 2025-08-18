# Write a program to check tree balanced or not.

# Definition for a binary tree node

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isEqual(self, root):
        def dfs(node):
            if not node:
                return 0  # height = 0
            
            left = dfs(node.left)
            if left == -1:  # left subtree unbalanced
                return -1
            
            right = dfs(node.right)
            if right == -1:  # right subtree unbalanced
                return -1
            
            if abs(left - right) > 1:
                return -1  # unbalanced
            
            return 1 + max(left, right)  # return height
        
        return dfs(root) != -1


# Example tree
# Testcase 1
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(3)
# root.left.left.left = TreeNode(4)
# root.left.left.right = TreeNode(4)

#Testcases 2
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(15)
root.left.right = TreeNode(7)



sol = Solution()
print(sol.isEqual(root))  # Output: False
