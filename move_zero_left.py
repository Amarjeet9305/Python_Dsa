# Write a program given array=[1,2,3,0,7,0,9,0] move all non zeros right to left on array 
# given an array space
# Approach is two pointer proble will to start last index to traverse the array

# Function defintion

class Solution:
    def moveZeroLeft(self,arr):
        
        #calcluate the arr lenghth
        
        n = len(arr)
        
        j = 0
        # Travers arry right to left with range function
        for i in range(n-1,-1,-1):
            
            # if non-zeros,swap it with arr[j]
            if arr[i] != 0:
                arr[i],arr[j] =arr[j],arr[i]
                
                j -=1
        return arr        
# Driver code

arr = [1, 2, 0, 4, 3, 0, 5, 0]

obj = Solution()

obj.moveZeroLeft(arr)  

print(arr)              
            