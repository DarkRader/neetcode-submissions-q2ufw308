class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []

        for bracket in s:
            if bracket == '[' or bracket == '{' or  bracket == '(':
               stack.append(bracket)
               continue

            if not bool(stack):
                return False

            if bracket == ']':
                pop_element = stack.pop()
                if pop_element != '[':
                    return False

            if bracket == '}':
                pop_element = stack.pop()
                if pop_element != '{':
                    return False

            if bracket == ')':
                pop_element = stack.pop()
                if pop_element != '(':
                    return False

        if bool(stack):
            return False
        return True
        