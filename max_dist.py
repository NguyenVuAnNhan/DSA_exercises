class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        small = arrays[0][0]
        big = arrays[0][-1]
        dist = 0

        for i in arrays[1:]:
            dist = max(dist, max(big - i[0], i[-1] - small))
            small = min(small, i[0])
            big = max(big, i[-1])
        
        return dist