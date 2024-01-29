class Solution:
    def encode(self, strs):
        result = ""
        
        for s in strs:
            result += str(len(s)) + "#" + s
        return result
