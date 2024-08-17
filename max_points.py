class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        cur = points[0]
        ROWS, COLS = len(points), len(points[0])

        for i in range(1, ROWS):
            next_row = points[i].copy()
            left, right = [0]*COLS, [0]*COLS

            left[0] = cur[0]

            for j in range(1, COLS):
                left[j] = max(cur[j], left[j-1]-1)

            right[-1] = cur[-1]
            for j in range(COLS - 2, -1, -1):
                right[j] = max(cur[j], right[j+1]-1)

            for j in range(0, COLS):
                next_row[j] += max(left[j], right[j])
            
            cur = next_row

        return max(cur)