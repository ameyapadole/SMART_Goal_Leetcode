def validParenthesis(s):
    stack = []
    mapping = {')':'(', ']':'[', '}':'{'}

    for char in s:
        if char in mapping: 
            topelement = stack.pop() if stack else '#'

            if mapping[char] != topelement:
                return False 
        else:
            stack.append(char)
    return not stack

print(validParenthesis("()[]{}"))


"""
Time Complexity = O(N) because we iterate through the string on char at a time and the push pop operations takes O(1) time.
Space Complexity = O(N) because we push all opening brackets onto the stack, the worst case would be {{{{{{{
"""