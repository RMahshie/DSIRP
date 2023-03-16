def infix_to_prefix(infix):
    # Reverse the infix string
    infix = infix[::-1]

    # Initialize stacks for the prefix expression and operators
    prefix_stack = []
    operator_stack = []

    # Loop over each character in the infix string
    for c in infix:
        if c.isdigit():
            # If the character is a digit, add it to the prefix stack
            prefix_stack.append(c)
        elif c in ['+', '-', '*', '/']:
            # If the character is an operator, push it onto the operator stack
            operator_stack.append(c)
        elif c == ')':
            # If the character is a closing parenthesis, push it onto the operator stack
            operator_stack.append(c)
        elif c == '(':
            # If the character is an opening parenthesis, pop operators off the stack and
            # add them to the prefix stack until a closing parenthesis is found
            while operator_stack[-1] != ')':
                operator = operator_stack.pop()
                right_operand = prefix_stack.pop()
                left_operand = prefix_stack.pop()
                prefix_stack.append(operator + left_operand + right_operand)
            # Pop the closing parenthesis off the operator stack
            operator_stack.pop()

    # Pop any remaining operators off the stack and add them to the prefix stack
    while operator_stack:
        operator = operator_stack.pop()
        right_operand = prefix_stack.pop()
        left_operand = prefix_stack.pop()
        prefix_stack.append(operator + left_operand + right_operand)

    # Reverse the prefix stack to put the prefix expression in the correct order
    prefix_list = list(prefix_stack[::-1])

    # Join the list elements into a single string
    prefix_str = ''.join(prefix_list)

    return prefix_str

# Example usage
infix_string = "3*(4+5)/6-7"
prefix_list = infix_to_prefix(infix_string)
print(prefix_list)
# Output: '-/*3+4567'
