class Solution:
    OPENING_TO_CLOSING = {'[': ']', '(': ')', '{': '}'}  # Should use immutabledict
    CLOSING_TO_OPENING = {']': '[', ')': '(', '}': '{'}  # Should use immutabledict
    
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        for ch in s:
            if ch in Solution.OPENING_TO_CLOSING:
                stack.append(ch)
            elif ch in Solution.CLOSING_TO_OPENING:
                if not stack or stack[-1] != Solution.CLOSING_TO_OPENING[ch]:
                    return False
                stack.pop()
        return not stack