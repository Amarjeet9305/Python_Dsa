# Given a array will to move all zeros array to the right side at a given space
# It is two pionter problem will to solved move all zeros array to the right then we ini
# variable i and j


# Function defintion 

class Solution:
    # Function defintion with two argument
    def pushZeroToEnd(self,arr):
        # calcluate the arr lengeth
        n = len(arr)
        # take second pinter to update array updation
        j = 0
        # Move non-zero to elements forward
        for i in range(n):
            if arr[i] != 0:
                arr[j],arr[i] = arr[i],arr[j]
                
                j += 1
# Driver code
arr = [1,2,0,4,3,0,5,0]

obj = Solution()

obj.pushZeroToEnd(arr)

print(arr)                
    
