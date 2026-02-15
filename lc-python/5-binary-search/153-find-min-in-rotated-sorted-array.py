from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        l, r = 0, len(nums)-1

        """ 
        [4,5,6,7,0,1,2]
         l       m   r   <- is m greater than r? No, so we know the minimum is in the left half (including m), we move r to m.

        After the first iteration, we have:
        [4,5,6,7,0]
         l   m   r   <- is m greater than r? Yes, so we know the minimum is in the right half, we move l to m+1.
        
        After the second iteration, we have:
        [7, 0]
         l m r   <- l is at index 0 (value 7), r is at index 1 (value 0), so m = 0. Since nums[m] > nums[r], the minimum is in the right half, so we move l to m+1.
        
        After the third iteration, we have:
        [0]
       l/m/r   <- l and r are the same, we can return the value at l or r.

    
        """
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        
        return nums[l]
    
    

        """ 
        [4,5,6,7,0,1,2]
         l     m     r   <- is m greater than r? Yes, so we know the minimum is in the right half, we move l to m+1.
         l       m   r   <- is m greater than r? No, so we know the minimum is in the left half (including m), we move r to m.
        
        After the first iteration, we have:
        [0,1,2]
        l  m  r   <- is m greater than r? No, so we know the minimum is in the left half (including m), we move r to m.
        
        After the second iteration, we have:
        [0,1]
    
        """