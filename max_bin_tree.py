# You are given an integer array nums with no duplicates. A maximum binary tree 
# can be built recursively from nums using the
# following algorithm

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left
# Create a class and instance
class Solution(object):
    def isMaximum(self,nums):
        # If nums is empty
        if not nums:
            return None
        # Find max element and index
        max_val = max(nums)
        max_index = nums.index(max_val)
        
        # Create a root node
        root = TreeNode(max_val)
        
        # Recursively build left subtree (element before max_index)
        root.left = self.isMaximum(nums[:max_index])
        
        # Recursively build right subtree (element after max_index)
        
        root.right = self.isMaximum(nums[max_index+1:])
        
        return root

# Helper function to print tree in preorder traversal
def preorder(node):
    if not node:
        
        return []
    return [node.val] + preorder(node.left) + preorder(node.right)
    
# Driver code
nums = [3, 2, 1, 6, 0, 5]
sol = Solution()            
root = sol.isMaximum(nums)

print("Preorder Traversal of Maximum Binary Tree:", preorder(root))