from typing import List


class Solution:
    def findRotationCount(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1
        ans = float("inf")
        index = 0

        while l <= r:
            m = (l + r) // 2
            if nums[l] < nums[m]:
                if nums[l] < ans:
                    ans = nums[l]
                    index = l
                    l = m + 1
            else:
                if nums[m] < nums[r]:
                    if nums[m] < ans:
                        ans = nums[m]
                        index = m
                    r = m - 1
                else:
                    if nums[r] < ans:
                        ans = nums[r]
                        index = r
                    l = m + 1
        return index


#

sol = Solution()
print(sol.findRotationCount([4, 5, 6, 7, 0, 1, 2, 3]) == 4)  # Expected: 4
print(sol.findRotationCount([3, 4, 5, 1, 2]) == 3)  # Expected: 3
print(sol.findRotationCount([1, 2, 3, 4, 5]) == 0)  # Expected: 0
