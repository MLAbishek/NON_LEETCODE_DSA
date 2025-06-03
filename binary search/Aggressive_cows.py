"""
Aggressive Cows

Difficulty: Medium

You are given an array with unique elements of stalls[], which denote the position of a stall. You are also given an integer k which denotes the number of aggressive cows. Your task is to assign stalls to k cows such that the minimum distance between any two of them is the maximum possible.

Examples:

Input: stalls = [1, 2, 4, 8, 9], k = 3
Output: 3
Explanation:
- First cow at stall[0] (1)
- Second cow at stall[2] (4)
- Third cow at stall[3] (8)
Minimum distance between any two cows = 3

Input: stalls = [10, 1, 2, 7, 5], k = 3
Output: 4
Explanation:
- First cow at stall[1] (1)
- Second cow at stall[4] (5)
- Third cow at stall[0] (10)
Minimum distance = 4

Input: stalls = [2, 12, 11, 3, 26, 7], k = 5
Output: 1
Explanation:
- Number of stalls = number of cows.
- Cows can be placed anywhere, minimum distance is 1.

Constraints:
2 <= stalls.length <= 10^6
0 <= stalls[i] <= 10^8
2 <= k <= stalls.length
"""


class Solution:
    def canplace(self, stalls, d, k):
        last = stalls[0]
        count = 1
        for i in range(1, len(stalls)):
            if stalls[i] - last >= d:
                count += 1
                last = stalls[i]
            if count == k:
                return True
        return False

    def aggressiveCows(self, stalls: list[int], k: int) -> int:
        stalls.sort()
        l = 0
        r = stalls[-1] - stalls[0]
        ans = float("-inf")
        while l <= r:
            mid = (l + r) // 2
            if self.canplace(stalls, mid, k):
                ans = max(ans, mid)
                l = mid + 1
            else:
                r = mid - 1
        return ans


s = Solution()

print(s.aggressiveCows([1, 2, 4, 8, 9], 3))  # Expected: 3
print(s.aggressiveCows([10, 1, 2, 7, 5], 3))  # Expected: 4
print(s.aggressiveCows([2, 12, 11, 3, 26, 7], 5))  # Expected: 1
