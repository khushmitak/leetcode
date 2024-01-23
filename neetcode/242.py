"""
METHOD 1: Both strings s and t can be sorted to check if they are anagrams.
Sorting will arrange the strings in ascending order.
Then, if the two sorted strings are the same, they are anagrams, return true.
Otherwise, return false.

Time Complexity : O(n log n)
Space Complexity : O(1)

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_stringS = sorted()
        sorted_stringT = sorted()
        
        return sorted_stringS == sorted_stringT