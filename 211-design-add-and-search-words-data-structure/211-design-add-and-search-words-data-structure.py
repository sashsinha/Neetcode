class WordDictionary:

    def __init__(self):
        self.trie = {}
        self.end_word_delimiter = '#'

    def addWord(self, word: str) -> None:
        curr = self.trie
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        curr[self.end_word_delimiter] = ''

    def search(self, word: str) -> bool:
        def helper(i: int, curr: dict[dict[str]]) -> bool:
            if i == len(word):
                return self.end_word_delimiter in curr
            ch = word[i]
            if ch == '.':
                return any(helper(i + 1, curr[x]) for x in curr if x != self.end_word_delimiter)
            else:
                if ch not in curr:
                    return False
                return helper(i + 1, curr[ch])
        return helper(0, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)