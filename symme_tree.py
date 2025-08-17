# Write a program to check given tree symmetric or not

# Definition for a binary tree node

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution class
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True

        def isSaw(v1, v2):
            if not v1 and not v2:
                return True
            if not v1 or not v2:
                return False
            # Mirror check: left of one vs right of other, and right of one vs left of other
            return (v1.val == v2.val and
                    isSaw(v1.left, v2.right) and
                    isSaw(v1.right, v2.left))

        return isSaw(root.left, root.right)


# Driver code
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

sol = Solution()
print(sol.isSymmetric(root))  
