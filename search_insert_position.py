# Write a program search insert position to find targe value index position.
# Approach: Binary Search

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # First Initalize two pointer for binary search
        low, high = 0, len(nums) - 1
        
        # Binary Search loop until low > high

        while low <= high:
            # Find the middle index

            mid = (low + high) // 2
        # Target found at mid index
            if nums[mid] == target:
                return mid  # Return Index value where target element
            elif nums[mid] < target:
                low = mid + 1
            # If Target is smaller so search the left half    
            else:
                high = mid - 1    
        # Position to insert target to maintain sorted order        
        return low                

# Driver Code
#Case:1
sol = Solution()
nums = [1,3,5,6]
print(sol.searchInsert(nums,target=5))     

# Case:2
print(sol.searchInsert(nums,target = 2))

# Case:3
print(sol.searchInsert(nums,target=7))  