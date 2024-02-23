class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = "" # to store new string with only alphanumeric characters
        
        for c in s:
            if c.isalnum():
                newString += c.lower()
        
        return newString == newString[::-1]

#Method 2:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            while left < right and not self.alphaNum(s[left]):
                left += 1
            while right > left and not self.alphaNum(s[right]):
                right -= 1
                
            if s[left].lower() != s[right].lower():
                return False
            left = left + 1
            right = right - 1
        
        return True
        
        
        def alphaNum(self, c):
            return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') 
                    or ord('0') <= ord(c) <= ord('9'))