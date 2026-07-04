class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        slow=0
        fast=1
        while fast<len(nums):
            if nums[slow]==0 and nums[fast]==0:
                fast+=1
            elif nums[slow]==0 and nums[fast]!=0:
                nums[slow],nums[fast]=nums[fast],nums[slow]
            else:
                slow+=1
                fast+=1
        return None

sol = Solution()
sol.moveZeroes([0,1,0,3,4,2])