def peek(stack):
    return stack[-1] if stack else None

def evaluate_top(operator_stack, operand_stack):
    operator = operator_stack.pop()
    a = operand_stack.pop()
    b = operand_stack.pop()
    if operator == '*': operand_stack.append(b * a)
    elif operator == '/': operand_stack.append(b / a)
    elif operator == '+': operand_stack.append(b + a)
    elif operator == '-': operand_stack.append(b - a)

def evaluate(expression):
    tokens = expression.split(' ')
    precedence = {
        '/': 2,
        '*': 2,
        '+': 1,
        '-': 1
    }
    operator_stack = []
    operand_stack = []
    for token in tokens:
        print(operand_stack, operator_stack)
        if token.isnumeric():
            operand_stack.append(float(token))
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            top_of_operator_stack = peek(operator_stack)
            while top_of_operator_stack is not None and top_of_operator_stack != '(':
                print(operand_stack, operator_stack)
                evaluate_top(operator_stack, operand_stack)
                top_of_operator_stack = peek(operator_stack)
            operator_stack.pop()
        else:
            top_of_operator_stack = peek(operator_stack)
            while top_of_operator_stack is not None and top_of_operator_stack not in '()' and precedence[top_of_operator_stack] > precedence[token]:
                print(operand_stack, operator_stack)
                evaluate_top(operator_stack, operand_stack)
                top_of_operator_stack = peek(operator_stack)
            operator_stack.append(token)
    
    while operator_stack:
        print(operand_stack, operator_stack)
        evaluate_top(operator_stack, operand_stack)
    
    return operand_stack[0]

if __name__ == '__main__':
    # x = evaluate("2 * 3 + 5")
    # print(x)
    x = evaluate("5 / 2 + 6 * ( 3 + 5 / 5 )")
    print(x)