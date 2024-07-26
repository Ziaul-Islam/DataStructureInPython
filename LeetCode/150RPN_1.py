class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []

        for token in tokens:
            if token == "+":
                stack[-2] = stack[-2] + stack[-1]
                stack.pop(-1)
            elif token == "-":
                stack[-2] = stack[-2] - stack[-1]
                stack.pop(-1)
            elif token == "*":
                stack[-2] = stack[-2] * stack[-1]
                stack.pop(-1)
            elif token == "/":
                stack[-2] = stack[-2] // stack[-1] if stack[-2] * stack[-1] >= 0 else -(-stack[-2] // stack[-1])
                stack.pop(-1)
            else:
                stack.append(int(token))

        return stack[-1]