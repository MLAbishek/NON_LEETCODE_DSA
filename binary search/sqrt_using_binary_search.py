import unittest

"""
100. Find Square Root of a Number
Medium

Hint:
Given a positive integer n. Find and return its square root. If n is not a perfect square, then return the floor value of sqrt(n).

Examples:

Input: n = 36
Output: 6
Explanation: 6 is the square root of 36.

Input: n = 28
Output: 5
Explanation: The square root of 28 is approximately 5.292. So, the floor value will be 5.
"""


class Solution:
    def mySqrt(self, n: int) -> int:
        if n < 2:
            return n
        l = 0
        r = n - 1
        while l <= r:
            m = (l + r) // 2
            if m * m == n:
                return m
            elif m * m < n:
                l = m + 1
            else:
                r = m - 1
        return r


s = Solution()

print(s.mySqrt(0))  # Expected: 0
print(s.mySqrt(1))  # Expected: 1
print(s.mySqrt(4))  # Expected: 2
print(s.mySqrt(10))  # Expected: 3
print(s.mySqrt(16))  # Expected: 4
print(s.mySqrt(28))  # Expected: 5
print(s.mySqrt(36))  # Expected: 6
print(s.mySqrt(100))  # Expected: 10
