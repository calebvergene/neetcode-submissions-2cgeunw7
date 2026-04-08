class Solution:
    ## every word should start with int then ";"
    ## that way, you know how to long each word should be and also how long the number is
    def encode(self, strs: List[str]) -> str:
        final = ""
        for word in strs:
            final += f'{len(word)};{word}'
        print(final)
        return final
        

    def decode(self, s: str) -> List[str]:
        final = []
        word = ""
        length = 0
        onword = False
        for i in range(len(s)):
            if s[i] == ";" and not onword:
                length = int(length)
                if not length:
                    final.append("")
                    continue
                onword = True
            elif not onword:
                length = str(length) + str(s[i])
            elif onword:
                word += s[i]
                length -= 1
                if length == 0:
                    final.append(word)
                    word = ""
                    onword = False
        return final
                


