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

"""
METHOD 2: Using a hashmap is more efficient solution. 
Iterate through the array once and see is the difference between target and current element already exists in hashmap.
If it already exists, return the indices of the two elements.
Otherwise, add the current element to the hashmap.

Time complexity: O(n)
Space complexity: O(n)

"""
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap ={}
        
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashMap:
                return [hashMap[difference], i]
            hashMap[nums[i]] = i
            
        return[]
            