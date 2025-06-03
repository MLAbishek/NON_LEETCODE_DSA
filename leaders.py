from typing import List
class Solution:
    def findLeaders(self, nums):
        ans=[]
        flag=1
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    flag=0
                
            if flag==1:
                ans.append(nums[i])
            else:
                flag=1
        ans.append(nums[-1])
        return ans


        
# Example usage (for local testing):
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    nums1 = [1, 2, 5, 3, 1, 2]
    print("Output:", sol.findLeaders(nums1))  # Expected: [5, 3, 2]

    # Test Case 2
    nums2 = [-3, 4, 5, 1, -4, -5]
    print("Output:", sol.findLeaders(nums2))  # Expected: [5, 1, -4, -5]

    # Test Case 3
    nums3 = [-3, 4, 5, 1, -30, -10]
    print("Output:", sol.findLeaders(nums3))  # Expected: [5, 1, -10]
