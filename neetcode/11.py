class Solution:
    def maxArea(self, height: List[int]) -> int:
        #brute force
        
        result = 0
        
        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                area = (r - l) * min(height[l], height[r])
                result = max(result, area)
                
        return result
    
class Solution:
    def maxArea(self, height: List[int]) -> int:
        #optimal solution
        l = 0
        r = len(height) - 1
        result = 0
        
        while l < r:
            area = (r - l) * min(height[l], height[r])
            result = max(result, area)
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                r -= 1 
        
        return result