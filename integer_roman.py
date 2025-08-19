# Write a program to covert integer to roman using for loop.

# Define the class and method

class Solution():
    def intRoman(self,num):
        
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    # Check roman is empty then
        roman = ""  
        # Check all each value and symbols
        for i in range(len(value)):
            while num >= value[i]:
                roman += symbol[i]
                num -= value[i]
        return roman
# Driver code
#Testcase1
sol = Solution()

print(sol.intRoman(num=3749))

#Testcase2     
print(sol.intRoman(num=58))      

#Testcase3
print(sol.intRoman(num=1994))    