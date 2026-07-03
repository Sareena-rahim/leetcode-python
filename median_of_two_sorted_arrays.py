class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = sorted(nums1 + nums2)

        if len(merged) % 2 != 0:
            return merged[len(merged) // 2]
        else:
            midpoint = len(merged) // 2
            return (merged[midpoint] + merged[midpoint - 1]) / 2
sol=Solution()
sol.findMedianSortedArrays([1,3],[2])