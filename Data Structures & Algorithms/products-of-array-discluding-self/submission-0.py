class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        for i, num in enumerate(nums):
            for j, n in enumerate(nums):
                if j != i:
                    res[i] = res[i] * n


        return res
        