# Problem is add two number with given target variable to return output is index number
# Defining two sum function
# Approach is a brute force will finding iteration each of line code
# Time complexity is a o(n^2)

# Defining function
def two_sum(num,target):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i]+num[j] == target:
                return [i,j]
# Driver code
num=[2,3,5,6,7]
target=8

# Function calling

print(two_sum(num,target))
             