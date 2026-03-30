class Solution:
    def check_more_freq(self, res: list[int], num_count: dict, num: int):
        for i, cur in enumerate(res):
            if cur not in num_count:
                if num not in res:
                    res[i] = num
                break
            elif num_count[num] > num_count[cur] and num not in res:
                res[i] = num
                break

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = {}
        res = [0] * k
        for num in nums:
            if num not in nums_count:
                nums_count[num] = 1
                self.check_more_freq(res, nums_count, num)
            else:
                nums_count[num] += 1
                self.check_more_freq(res, nums_count, num)

        return res

        