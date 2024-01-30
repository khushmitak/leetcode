class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet =set(nums)
        longestSeq = 0
        
        for i in nums:
            if (i - 1) not in numSet: #check if the sequence starts here
                length = 1
                while (i + length) in numSet:
                    length += 1
                longestSeq = max(length, longestSeq)
        return longestSeq
                