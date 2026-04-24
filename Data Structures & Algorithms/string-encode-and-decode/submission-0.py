class Solution:

    def encode(self, strs: List[str]) -> str:

        ans = ""
        for i in strs:
            size = len(i)
            ans += str(size) + "#" + i
        
        return ans

    def decode(self, s: str) -> List[str]:
        word = ""
        size = ""
        char = 0
        ans = []
        while char < len(s):
            
            if s[char] != "#":
                size += s[char]
                char += 1
            else:
                char += 1
                intsize = int(size)
                
                for i in range(intsize):
                    word += s[char]
                    char += 1
                
                ans.append(word)
                size = ""
                word = ""
       
        return ans

        


















