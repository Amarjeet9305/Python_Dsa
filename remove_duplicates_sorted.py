class Solution(object):
    def removeDuplicates(self, nums):
        
    

        # If nums is empty, no elements to process
        if not nums:
            return 0

        # write_index points to the position where the next unique element should go
        write_index = 1  

        # Start reading from the second element (index 1)
        for read_index in range(1, len(nums)):

            # If the current element is NOT equal to the previous one,
            # it means we've found a new unique element
            if nums[read_index] != nums[read_index - 1]:

                # Place this unique element at the write_index position
                nums[write_index] = nums[read_index]

                # Move the write_index forward
                write_index += 1  

        # At the end, write_index will be the count of unique elements
        return write_index

# Driver Code
sol = Solution()
nums = [1,1,3]
#print(sol.removeDuplicates([1, 1, 2, 3, 4, 4, 5]))  # Output: 5
print(sol.removeDuplicates(nums))
