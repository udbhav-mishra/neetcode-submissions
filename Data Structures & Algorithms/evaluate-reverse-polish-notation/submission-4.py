class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def operation(num1, num2, operand):
            if operand == '+': stack.append(num1 + num2)
            elif operand == '-': stack.append(num1 - num2)
            elif operand == '*': stack.append(num1 * num2)
            else: stack.append(int(num1 / num2))
            return

        stack = []
        for i in range(len(tokens)):
            if tokens[i] in '+-*/':
                operand = tokens[i]
                num2 = stack.pop()
                num1 = stack.pop()
                operation(num1, num2, operand)

            else: stack.append(int(tokens[i]))
        return stack.pop()