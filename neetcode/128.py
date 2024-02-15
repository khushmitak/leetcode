"""
METHOD 1: Using sorting method: The array will be sorted. If an empty array, return 0
If we have more than 1 elements, then compare the elements to see if elements are consecutive or not.
There may be more than 1 consecutive sequences in the array, so update and return the max of current and longest sequence.
Time complexity: O(n log n)
Space complexity: O(1)
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: #if the array is empty, return 0
            return 0
        
        nums.sort()
        currentSeq = 1
        longestSeq = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]: #check if the current element is different from the previous 
                if nums[i-1] == nums[i] - 1: #check if they are consecutive
                    currentSeq += 1
                else: #if not consecutive, update the longestSeq and reset the current sequence
                    longestSeq = max(currentSeq, longestSeq)
                    currentSeq = 1
        return max(currentSeq, longestSeq)

"""
METHOD 2: Use a set to store all the nums and check if the current element is start of sequence or not.
If start of sequence, check for consecutive elements and get the longest Seq.
If not, then continue to next element. 
Return the max of longest sequence and length of array.
"""

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
                