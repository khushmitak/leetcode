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

"""
METHOD 2: Create hashmaps for both strings. The keys will be the characters and values will be the occurence of each character.
The characters and counts are stored in hashmaps for both strings.
The items in first string are compared to the second string items.
If they are the same, we have anagrams, return true.
Otherwise, return false.

Time Complexity : O(n)
Space Complexity : O(n)

""" 
        