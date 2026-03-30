class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for i, temp in enumerate(temperatures):
            count = 0
            while i != len(temperatures) - 1:
                if temperatures[i + 1] <= temp:
                    count += 1
                    i += 1
                else:
                    count += 1
                    res.append(count)
                    break

                if i == len(temperatures) - 1 and count != 0:
                    res.append(0)
            if count == 0:
                res.append(count)
            print(res)
        # res.append(count)

        return res

        