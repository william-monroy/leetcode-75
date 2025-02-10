class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final_str = ''
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            final_str += word1[i]
            final_str += word2[i]
        return final_str + word1[min_len:] + word2[min_len:] 
        