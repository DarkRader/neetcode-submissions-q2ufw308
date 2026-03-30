import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        op = {
            "+": operator.add, 
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }

        for token in tokens:
            if token not in op:
                stack.append(token)
            else:
                second_num = stack.pop()
                first_num = stack.pop()
                res = op[token](int(first_num), int(second_num))
                stack.append(res)

        return int(stack[0])
                
        