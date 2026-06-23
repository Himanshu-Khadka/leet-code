class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []

        for c in s:
            #push the expeced closing bracket for every open bracket
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')

            #if its a closing bracket it much match the poppped element.
            elif not stack or stack.pop() != c:
                return False
        
        #valid if the stack is completely empty
        return not stack