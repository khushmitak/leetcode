"""
arr = [1,2,7,9]
arr = [4]
arr =[]

METHOD 1: This is the bruteforce method where the sum of every pair of elements is checked for the target.
This is done by using nested loops.

Time complexity: O(n^2)
Space complexity: O(n)
    
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return[]
