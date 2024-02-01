class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = "" # to store new string with only alphanumeric characters
        
        for c in s:
            if c.isalnum():
                newString += c.lower()
        
        return newString == newString[::-1]