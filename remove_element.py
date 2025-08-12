#An array nums

#A value val

#You need to remove all occurrences of val in-place and return the new length.

#You must do it without using extra array space — meaning modify nums itself.

class Solution:
    def removeElement(self, nums, val):
        write_index = 0
        for num in nums:
            if num != val:
                nums[write_index] = num
                write_index += 1
        return write_index

# Driver code
sol = Solution()
nums = [3, 2, 2, 3]
length = sol.removeElement(nums, 3)
print(length)     # 2
print(nums[:length])  # [2, 2]
