def isBalanced(s):
    brackets = {'(':')', '{':'}', '[':']'}
    stack = []

    for char in s:
        if char in brackets:
            stack.append(char)
        elif len(stack) == 0:
            return 'NO'
        elif brackets[stack[-1]] == char:
            stack.pop() 
        else: 
            return 'NO'
    
    if len(stack) == 0:
        return 'YES'
    else: 
        return 'NO'



print(isBalanced("{[(])}")) # NO
print(isBalanced("([{[()]}])")) # YES
print(isBalanced("{()}")) # YES
print(isBalanced("")) # YES
print(isBalanced("{(([])[])[]]}")) # NO