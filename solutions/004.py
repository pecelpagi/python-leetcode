# https://leetcode.com/problems/median-of-two-sorted-arrays

from typing import List
import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        retval = 0
        
        merged_array = nums1 + nums2

        merged_array.sort()

        if (len(merged_array) % 2 == 0):
            lastIndex = math.floor(len(merged_array) / 2)
            firstIndex = lastIndex - 1

            retval = (merged_array[lastIndex] + merged_array[firstIndex]) / 2
        else:
            index = math.floor(len(merged_array) / 2)

            retval = merged_array[index]

        return retval
    
solution = Solution()
print(solution.findMedianSortedArrays([1,3], [2]))