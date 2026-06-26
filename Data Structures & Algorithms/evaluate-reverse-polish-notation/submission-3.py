class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            print(stack)
            match c:
                case '+':
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(op1 + op2)
                case '-':
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(op2 - op1)
                case '*':
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(op1 * op2)
                case '/':
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(int(op2 / op1))
                case _:
                    stack.append(int(c))
        return stack.pop()