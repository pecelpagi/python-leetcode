# https://leetcode.com/problems/palindrome-number

import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        currentNumber = x
        reversedNumber = 0

        while (currentNumber > 0):
            reversedNumber = (reversedNumber * 10) + (currentNumber % 10)
            currentNumber = math.floor(currentNumber / 10)

        return x == reversedNumber
    
solution = Solution()
print(solution.isPalindrome(121))