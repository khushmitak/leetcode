"""
METHOD: To find the product except itself, we can divide the array into prefix and postfix
and use the product of prefix and postfix to output an array of products. 
For this problem, the time complexity: O(n)
Space complexity: O(1) (as specified in the question)
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums) #creating an array of length nums with initial value for all positions = 1
        
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            result[i] = prefix #taking the prefix and putting it in position i in result array
            prefix *= nums[i] #prefix is multiplied with nums value and that value is stored in next index
            
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix #multiply the postfix value with the prefix value stored in result
            postfix *= nums[i]
        return result