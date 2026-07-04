class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        set1=set(nums)
        if len(set1)==1:
            return max(set1)
        maximum1=max(set1)
        set1.remove(maximum1)
        maximum2=max(set1)
        set1.remove(maximum2)
        if len(set1)==0:
            return maximum1
        else:

            return max(set1)
sol=Solution()
print(sol.thirdMax([3,2,1]))

