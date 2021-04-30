class Solution:
    def sumZero(self, n: int) -> List[int]:
        results = [x for i in range(1, n//2 +1) for x in {-i, i}]
        if n%2:
            results.append(0)
        return results
