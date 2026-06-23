class Solution:
    def isValid(self, s: str) -> bool:
        # list acting as stack
        stack = []

        #dictionary to map closing brackets to their opening coparts
        bracket_map = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for char in s:
            #if its a closing bracket
            if char in bracket_map:
                #pop the top element if the top is not empty, otherwise use a dummy '#'
                top_element = stack.pop() if stack else '#'

                #if the popped element doesnot match opening bracket its invalid
                if bracket_map[char] != top_element:
                    return False
            
            #if its an opening bracket
            else:
                stack.append(char)
        #if the stack is empty at the end its valid ("True"), if  not invalid ('False)
        return not stack

