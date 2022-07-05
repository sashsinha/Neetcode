class Solution:
    DIGITS_TO_LETTERS = {
        '2': ('a', 'b', 'c'),
        '3': ('d', 'e', 'f'),
        '4': ('g', 'h', 'i'),
        '5': ('j', 'k', 'l'),
        '6': ('m', 'n', 'o'),
        '7': ('p', 'q', 'r', 's'),
        '8': ('t', 'u', 'v'),
        '9': ('w', 'x', 'y', 'z')
    }

    def letterCombinations(self, digits: str) -> List[str]:
        def helper(i: int, path: list[str]) -> None:
            if i == len(digits):
                if path:
                    result.append(''.join(path))
                return
            for letter in Solution.DIGITS_TO_LETTERS[digits[i]]:
                path.append(letter)
                helper(i + 1, path)
                path.pop()
        result = []
        helper(0, [])
        return result
