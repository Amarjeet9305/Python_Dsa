# Write a program for convert roman to integer at a given any roman 
# Approach: We are solve this problem using dict and applying  approach

class Solution(object):
    
     def romanToInt(self , s):
         
         # First creating a dictonary
         
         roman_map = {
             
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
         }
         
        
        # Take a variable calculate total integer and initial state
        
         total = 0
        # Initalize an index variable i to traverse the string s
        
         i = 0 
        
         while i < len(s):
             
             if i + 1 <len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
                 
                 total += roman_map[s[i + 1]] - roman_map[s[i]]
                 
                 i += 2
             else:
                 total += roman_map[s[i]]
         return total            
# Driver code

sol = Solution()

print(sol.romanToInt("III"))                 
         
    
  
    