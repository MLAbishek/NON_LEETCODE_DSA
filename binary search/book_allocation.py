"""
Book Allocation Problem

Difficulty: Hard

You are given an array `nums` of `n` integers, where `nums[i]` represents the number of pages in the i-th book, and an integer `m` representing the number of students.

You must allocate all the books to `m` students such that:
1. Each student gets at least one book.
2. Each book is assigned to exactly one student.
3. The allocation must be contiguous (i.e., books assigned to a student must be in a continuous sequence).

Your goal is to **minimize the maximum number of pages assigned to a student**. If it is not possible to allocate books under the given constraints, return -1.

Example 1:
Input: nums = [12, 34, 67, 90], m = 2
Output: 113
Explanation: Allocation [12, 34, 67] and [90] has the minimum maximum pages = 113.

Example 2:
Input: nums = [10, 20, 30, 40], m = 2
Output: 60
Explanation: Allocation [10, 20, 30] and [40] results in max pages = 60.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= m <= nums.length
"""


class Solution:

    def checker(self, arr, k, thresold):
        totstudent = 1
        totpages = 0
        for i in range(len(arr)):
            if totpages + arr[i] <= thresold:
                totpages += arr[i]
            else:
                totpages = arr[i]
                totstudent += 1

        return totstudent

    def findPages(self, arr, k):

        l = max(arr)
        r = sum(arr)

        if k > len(arr):
            return -1

        if k == 1:
            return sum(arr)

        ans = float("inf")
        while l <= r:
            mid = (l + r) // 2
            if self.checker(arr, k, mid) <= k:
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        return ans
