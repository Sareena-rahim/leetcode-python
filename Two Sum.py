class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                 if nums[i]+nums[j]==target:
                     return [i,j]
        return None
sol = Solution()
result =sol.twoSum([2,7,11,15],18)
print(result)