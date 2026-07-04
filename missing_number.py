class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        num_dict={}
        for num in nums:
            num_dict[num]=num

        for i in range(len(nums)+1):
            if i not in num_dict:
                return i


sol=Solution()
print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))