class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = []
        for s in strs:
            encoded.append(f'{len(s)}:{s}')
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded = []
        i = 0
        while (colon_idx := s.find(':', i)) != -1:
            str_length = int(s[i:colon_idx])
            decoded.append(s[colon_idx+1:colon_idx+str_length+1])
            i = colon_idx + str_length + 1
        return decoded

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))