# Write a program to given an array arr=[1,2,3,4,5,6] then reverse the array 


class Solution:
    def reverseArray(self, arr):
        """
        Reverses the given list in place.

        :param arr: List of elements to be reversed
        :type arr: list
        """
        arr.reverse()

# Example usage:
solution = Solution()
arr = [1, 4, 3, 2, 6, 5]
solution.reverseArray(arr)
print(arr)  # Output: [5, 6, 2, 3, 4, 1]
