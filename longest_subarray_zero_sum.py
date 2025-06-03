from typing import List

class Solution:
    def maxLen(self, nums: List[int]) -> int:
        hashmap = {}
        cursum = 0
        maxdiff = 0  # Initialize to 0 instead of negative infinity
        
        for i in range(len(nums)):
            cursum += nums[i]
            
            if cursum == 0:
                maxdiff = max(maxdiff, i + 1)
            
            if cursum in hashmap:
                diff = i - hashmap[cursum]
                maxdiff = max(maxdiff, diff)
            else:
                hashmap[cursum] = i
        
        return maxdiff  # No need for the conditional return

# ----------------- 
# Test cases 
# -----------------

def test():
    sol = Solution()
    test_cases = [
        ([15, -2, 2, -8, 1, 7, 10, 23], 5),
        ([1, 2, 3], 0),
        ([0, 0, 0, 0], 4),
        ([6, -1, -3, 4, -2, 2, 4, 6, -12, -7], 9),
        ([], 0),
        ([1, -1], 2),
        ([1, 2, -3, 3], 3)
    ]
        
    for i, (nums, expected) in enumerate(test_cases):
        result = sol.maxLen(nums)
        print(f"Test case {i+1}: ", "Pass ✅" if result == expected else f"Fail ❌ (Expected {expected}, Got {result})")

if __name__ == "__main__":
    test()