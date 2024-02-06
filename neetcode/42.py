#trapping rain water

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: #if no height at all, no rain water is trapped
            return 0
        
        left  = 0 #left pointerat the starting index
        right = len(height) - 1 #right pointer at the end
        leftMax = height[left]
        rightMax = height[right]
        result = 0
        
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                result += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                result += rightMax - height[right]
                
        return result