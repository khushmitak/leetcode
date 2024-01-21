"""
arr1 = [1,2,3,4]; False
arr2 = [1,2,3,2]; True
arr2 = []; False
arr4 = [1]; False

We will take the element in the first index.
Compare it to the rest of the elements in the array using for loops.


Time Comp: o(n^2)
Space Comp: O(1)

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