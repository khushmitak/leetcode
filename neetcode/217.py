"""
arr1 = [1,2,3,4]; False
arr2 = [1,2,3,2]; True
arr2 = []; False
arr4 = [1]; False

METHOD 1: This is a bruteforce method where every element is compared with other elements in the array.
If there are any duplicates found, return true, else return false.

Time Comp: o(n^2)
Space Comp: O(1)

This approach is not efficient because of the time complexity for large arrays.

"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            for k in range(i+1, len(nums)): 
                if nums[i] == nums[k]:
                    return True
        return False
            

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)

        return False
    
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)

        return False