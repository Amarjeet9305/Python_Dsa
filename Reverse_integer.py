class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        sign = -1 if x < 0 else 1
        s = list(str(abs(x)))  # convert absolute value to list of chars
        
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        rev = sign * int(''.join(s))
        
        if rev < MIN_INT or rev > MAX_INT:
            return 0
        return rev


# Driver code
sol = Solution()

print(sol.reverse(123))
print(sol.reverse(120))