from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        
        # an array of arrays that will be the bucket holder
        # using bucker sort to store the numbers related to counts 
        freq = [[] for i in range(len(nums)+1)]

        # fill in the dictionary with numbers and their counts:
        # [1,1,1,2,2,3] = { 1:3, 2:2, 3:1 }
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        # enumerate - get both items from the dictionary
        for n, c in counts.items():
            freq[c].append(n)
        
        res = []
        # Iterate backwards through the freq array 
        #                  end,    start, step
        for i in range(len(freq)-1,   0,  -1):
            for item in freq[i]:
                res.append(item)
                if len(res) == k:
                    return res
        
if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,1,2,2,3]
    
    print(sol.topKFrequent(nums, 2))