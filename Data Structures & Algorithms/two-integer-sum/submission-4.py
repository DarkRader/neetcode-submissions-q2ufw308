class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        A = []
        for i, num in enumerate(nums):
            A.append([num, i])

        A.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            sum = A[i][0] + A[j][0]
            if sum == target:
                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]

            if sum < target:
                i += 1
                continue
            j -= 1

        return []