class Solution:
    def kidsWithCandies(self, A: list[int], e: int) -> list[bool]:
        limit = max(A) - e
        return [(c < limit) == False for c in A]