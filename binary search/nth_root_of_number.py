"""
Find the Nth Root of M
Medium

Given two numbers N and M, find the Nth root of M. The Nth root of a number M is defined as a number X such that when X is raised to the power of N, it equals M.
If the Nth root is not an integer, return -1.

Examples:

Input: N = 3, M = 27
Output: 3
Explanation: The cube root of 27 is equal to 3.

Input: N = 4, M = 69
Output: -1
Explanation: The 4th root of 69 does not exist as an integer. So, return -1.
"""


class Solution:
    def NthRoot(self, n: int, m: int) -> int:
        l = 0
        r = m - 1
        while l <= r:
            mid = (l + r) // 2
            exp = mid**n
            if exp == m:
                return mid
            elif exp < m:
                l = mid + 1
            else:
                r = mid - 1
        return -1


s = Solution()

print(s.NthRoot(3, 27))  # Expected: 3
print(s.NthRoot(4, 69))  # Expected: -1
print(s.NthRoot(2, 16))  # Expected: 4
print(s.NthRoot(5, 243))  # Expected: 3
print(s.NthRoot(6, 64))  # Expected: 2
