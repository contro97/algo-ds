def validateParentheses(s):

    # stack for left character symbols
    stack = []

    # loop for each character of the string
    for i in s:
        # if left symbol is encountered
        if i in ['[', '{', '(']:
            stack.append(i) # add left symbol to the stack
        elif i == ']' and len(stack) != 0 and stack[-1] == '[':
            stack.pop()
        elif i == ')' and len(stack) != 0 and stack[-1] == '(':
            stack.pop()
        elif i == '}' and len(stack) != 0 and stack[-1] == '{':
            stack.pop()
        else:
            return False
    return stack == []



if __name__ == '__main__':
    s = "(("

    print(validateParentheses(s))
