class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        result=[]
        for num in set2:
            if num in set1:
                result.append(num)
        return result
sol=Solution()
print(sol.intersection([4,9,5],[9,4,9,8,4]))
        