# Write a program to check each parentheses are open and close or not
# We are using Stack data structure principle of LIFO

# Create a class

class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            # If char is a closing bracket
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)  # If opening bracket, push to stack
        
        # Stack must be empty for valid parentheses
        return not stack

# Driver code
sol = Solution()
print(sol.isValid("()[]{}"))  # True
print(sol.isValid("(]"))      # False
print(sol.isValid("{[]}"))    # True
