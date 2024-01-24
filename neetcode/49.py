"""
METHOD: Use a hashmap to store character count as key and the list of anagrams as values.
Iterate over the original list of strings to check for characters in each string.
Append the anagrams together and return the list.

Time Complexity : O(k * n) k = number of given strings, n = average length of each string
Space Complexity : O(n)
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        for i in strs:
            count = [0] * 26
            
            for c in i:
                count[ord(c) - ord("a")] += 1
                
            result[tuple(count)].append(i)
        
        return result.values()