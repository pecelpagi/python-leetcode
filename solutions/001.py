# https://leetcode.com/problems/two-sum

from typing import List

class Solution:
    __cache = {}

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.__cache = {}
        results: List[int] = []

        for i, val in enumerate(nums):
            cacheKey = str(val)

            if (cacheKey in self.__cache):
                equal_target = (self.__cache[cacheKey]["value"] + val) == target

                if (equal_target):
                    first_index = self.__cache[cacheKey]["index"]
                    last_index = i
                    results = [first_index, last_index]
                    break
            else:
                self.__cache[str(target - val)] = { "index": i, "value": val }

        return results

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
print(solution.twoSum([3,2,4], 6))
print(solution.twoSum([3,3], 6))
