# Write a program Longest Common Prefix(LCP) to find the longest common prefix string an
# given array or list 
# Solution is using Brute force approach to finding vertical scaling that means compare 
# Index position (character by character)

class solution(object):
    def lcp(self,strs):
        # If list is empty
        if not strs:
            return ""  # Return null
        # Check first all character compare
        for i in range(len(strs[0])):
            char = strs[0][i]
# Compare this character with the same index in all other string
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
            # If loop mismatch all character         
                    return strs[0][:i]
        return strs[0]

#Driver code

sol = solution()

#print(sol.lcp(["flower", "flow", "flight"]))           

print(sol.lcp(["Bat","Cat","Dog"])) 
            
