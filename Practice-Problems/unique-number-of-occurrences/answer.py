class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur_dict = {}
        for num in arr:
            occur_dict[num] = occur_dict.get(num, 0) + 1
        occurences = occur_dict.values()
        return len(occurences) == len(set(occurences))
