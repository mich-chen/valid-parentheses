from typing import List

def isValid(s: str) -> bool:

    stack = []
    types = {')': '(', '}': '{', ']': '['}

    for char in s:
        # if stack is not empty and character is a closing type
        # and the top of stack is its matching opening type
        if stack and (stack[-1] == types.get(char, None)):
            stack.pop()
        else:
            stack.append(char)

    return len(stack) == 0

# additional/alternative solution:
    # if char in types:
    #     top_element = stack.pop() if stack else None
    #     if types[char] != top_element:
    #         return False
    # else:
    #     stack.append(char)


if __name__ == '__main__':

    s1 = "()[]{}"
    s2 = "([)]"
    s3 = "{[]}"
    print(isValid(s1))  # True
    print(isValid(s2))  # False
    print(isValid(s3))  # True
