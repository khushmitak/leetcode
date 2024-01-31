class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #count the occurences of each number
        array = [[] for i in range(len(nums) + 1)] # array to store list of numbers based on count
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            array[c].append(n)
        
        result = []
        for i in range(len(array) - 1, 0, -1):
            for n in array[i]:
                result.append(n)
                if (len(result)) == k:
                    return result