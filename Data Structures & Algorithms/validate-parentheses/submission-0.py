class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if stack:
                if char == ")" and stack[-1] == "(":
                    del stack[-1]
                elif char == "}" and stack[-1] == "{":
                    del stack[-1]
                elif char == "]" and stack[-1] == "[":
                    del stack[-1]
                else: stack.append(char)
            else: stack.append(char)
        return True if not stack else False