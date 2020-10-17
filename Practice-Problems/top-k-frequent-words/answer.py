class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_dict = {}
        
        for word in words:
            freq_dict[word] = 1 if word not in freq_dict else freq_dict[word] + 1
        
        lst = sorted(freq_dict, key = lambda x: (-freq_dict[x], x))
        
        return lst[:k]
