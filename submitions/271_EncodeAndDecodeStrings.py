class Solution:

    def encode(self, strs: list[str]) -> str:
        return ''.join(str(len(word)) + '#' + word for word in strs)
    def decode(self, s: str) -> list[str]:
        output = []
        i = 0
        while i < len(s):
            j = i
            count = ''
            while s[j] != '#':
                count += s[j]
                j += 1
            count = int(count)
            i = j+1
            word = ''
            for k in range(i, i+count):
                word += s[k]
            output.append(word)
            i = i+count
        return output