class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_stringS = sorted()
        sorted_stringT = sorted()
        
        return sorted_stringS == sorted_stringT