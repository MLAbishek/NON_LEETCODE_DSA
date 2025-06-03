"""
Painter's Partition Problem

Problem Statement:
Given an array/list of length N, where the array/list represents the boards and each element of the given array/list represents the length of each board.

There are K painters available to paint these boards. Each painter takes 1 unit of time to paint 1 unit length of the board.

Your task is to determine the **minimum time** required to paint all the boards under the constraint that:
1. Each painter can only paint **continuous sections** of boards.
2. A board cannot be painted by more than one painter.

Return the minimum area (time) needed to paint all the boards.

Examples:

Input: boards = [10, 20, 30, 40], k = 2
Output: 60
Explanation: One optimal way is to paint boards as [10, 20, 30] and [40], so the max painted length is 60.

Input: boards = [5, 10, 30, 20], k = 2
Output: 35
Explanation: Allocate [5,10,30] to one and [20] to another.

Constraints:
- 1 <= N <= 10^5
- 1 <= boards[i] <= 10^9
- 1 <= K <= N
"""


class Solution:
    def helper(self, arr, k, thresold):
        boardtime = 0
        worker = 1
        for i in range(len(arr)):
            if boardtime + arr[i] <= thresold:
                boardtime += arr[i]
            else:
                boardtime = arr[i]
                worker += 1

        return worker

    def minTime(self, boards: list[int], k: int) -> int:
        l = max(boards)
        r = sum(boards)
        ans = float("inf")
        while l <= r:
            mid = (l + r) // 2
            if self.helper(boards, k, mid) <= k:
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1

        return ans


"--------------------------------------------------------------------------------------------------------------"
test_cases = [
    {"boards": [10, 20, 30, 40], "k": 2, "expected": 60},
    {"boards": [5, 10, 30, 20], "k": 2, "expected": 45},
    {"boards": [10, 20, 30, 40, 50], "k": 3, "expected": 60},
    {"boards": [10, 10, 10, 10], "k": 2, "expected": 20},
    {"boards": [1, 1, 1, 1, 1, 1], "k": 3, "expected": 2},
    {"boards": [100], "k": 1, "expected": 100},
    {"boards": [10, 20], "k": 2, "expected": 20},
    {"boards": [1, 2, 3, 4, 5], "k": 2, "expected": 9},
]
s = Solution()
for i, case in enumerate(test_cases):
    result = s.minTime(case["boards"], case["k"])
    print(
        f"Test Case {i+1}: {'Pass' if result == case['expected'] else 'Fail'} | Output: {result}, Expected: {case['expected']}"
    )
