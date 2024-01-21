"""
arr1 = [1,2,3,4]; False
arr2 = [1,2,3,2]; True
arr2 = []; False
arr4 = [1]; False

METHOD 1: This is a bruteforce method where every element is compared with other elements in the array.
If there are any duplicates found, return true, else return false.

Time Comp: O(n^2)
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

"""
METHOD 2: The array is first sorted in ascending order.
Then the adjacent elements are compared to check for duplicates.
If any of the two elements are same, then duplicates are found, so return True. Otherwise, return False.

Time Complexity: O(n log n)
Space Complexty: O(1)

""" 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False


"""
METHOD 3: Use a hashset to store elements from the array.
If an element is already in the hashset, the duplicate has been found. Return True.
Otherwise, add an element to the hashset and continue.

Time complexity: O(n)
Space complexity: O(n)

This is the most efficient method to check for duplicates.
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)

        return False