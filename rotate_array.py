# Write a program to given array to rotate on anti clockwise direction without any extra space
# Approach is optimal approach will to used: reverse the first d element and reverse n-d element
# and reverse remaining element

class Solution():
    def rotate_arr(self,arr,d):
        # Calcluate the arr size
        
        n = len(arr)
        
        d = d % n
        # Reverse the first d element
        self.reverse(arr, 0, d-1)
        # Reverse the remaining d-n element
        self.reverse(arr, d, n-1)
        # Revese the remaining element
        self.reverse(arr, 0, n-1)
        
    def reverse(self,arr,start,end):
        
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            
            start += 1
            end -= 1
# Driver code 
# Function calling
arr = [1,2,3,4,5]

obj = Solution()

obj.rotate_arr(arr, 3)

print(arr)                