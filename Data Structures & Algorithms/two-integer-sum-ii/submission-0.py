class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, t, z = 0, 1, len(numbers) - 1

        while True:
            while t <= z:
                if numbers[i] + numbers[t] == target:
                    return[i + 1, t + 1]
                t += 1
            i = i + 1
            t = i + 1

        return []
        