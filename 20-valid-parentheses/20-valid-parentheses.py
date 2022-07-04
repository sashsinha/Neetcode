class Solution:
    def isValid(self, s: str) -> bool:
        closing_to_opening = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        stack = []
        for ch in s:
            if ch not in closing_to_opening:
                stack.append(ch)
            else:
                if not stack or closing_to_opening[ch] != stack.pop():
                    return False
        return not stack
