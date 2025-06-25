# Write a program palindrome digit is reversal special case.
# Negative number can be never Palindrome.
# Numbers ending in 0 (e.g., 10) are not palindromes unless the number is 0 itself.

# Approach:Reverse Half of the Number (Optimal, No String Conversion)

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return  False
            
        reversed_half = 0   

        # Reverse half of the number

        while x > reversed_half:
            digit = x % 10
            reversed_half = reversed_half * 10 + digit
            x //= 10

        return x == reversed_half or x == reversed_half // 10 
# Driver code

    