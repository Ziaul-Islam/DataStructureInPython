class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y) if x / y > 0 else -(-x // y)
        }
        for token in tokens:
            if token not in operators:
                stack.append(int(token))  # Convert token to integer
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(operators[token](val2, val1))
        return stack[-1]
