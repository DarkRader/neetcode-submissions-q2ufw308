class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, t = 0, len(numbers) - 1

        while True:
            curSum = numbers[i] + numbers[t]

            if curSum > target:
                t -= 1
            elif curSum < target:
                i += 1
            else:
                return[i + 1, t + 1]
        # while True:
        #     while t <= z:
        #         if numbers[i] + numbers[t] == target:
        #             return[i + 1, t + 1]
        #         t += 1
        #     i = i + 1
        #     t = i + 1

        return []
        