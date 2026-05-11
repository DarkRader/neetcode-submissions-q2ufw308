class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []

        for op in operations:
            if op == "+":
                result.append(result[-1] + result[-2])
            elif op == "D":
                result.append(result[-1] * 2)
            elif op == "C":
                result.pop()
            else:
                result.append(int(op))

        res = 0
        for num in result:
            res += num

        return res
        