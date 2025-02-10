class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        len1, len2 = len(word1), len(word2)
        
        for i in range(max(len1, len2)):
            if i < len1:
                res.append(word1[i])
            if i < len2:
                res.append(word2[i])
        
        return ''.join(res)
        