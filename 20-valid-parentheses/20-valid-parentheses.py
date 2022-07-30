class Solution:

    
    def isValid(self, s: str) -> bool:
        OPENING_BRACKETS = {'[', '(', '{'}  # Better to use frozenset.
        CLOSING_BRACKETS_TO_OPENING_BRACKETS = {']': '[', ')': '(', '}': '{'}  # Better to use immutabledict.
        if not s:
            return True
        stack = []
        for ch in s:
            if ch in OPENING_BRACKETS:
                stack.append(ch)
            elif ch in CLOSING_BRACKETS_TO_OPENING_BRACKETS:
                if not stack or stack[-1] != CLOSING_BRACKETS_TO_OPENING_BRACKETS[ch]:
                    return False
                stack.pop()
        return not stack