class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        largest = second = -1
        
        for num in arr:
            if num > largest:
                
                second = largest
                
                largest = num
            elif num > second and num != largest:
                
                second = num
        return second        
          
        
# Function calling expected output 

obj = Solution()

# Test case

arr = [12,35,1,10,34,1]

print(obj.getSecondLargest(arr))