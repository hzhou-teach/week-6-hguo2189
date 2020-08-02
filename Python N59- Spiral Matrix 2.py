class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        row = []
        m = n
        while m > 0:
            row.append(0)
            m -= 1
        matrix = []
        m = n
        while m > 0:
            matrix.append(row[:])
            m -= 1
        top_max, right_max, bottom_max, left_max = 1, n - 1, n - 1, 0
        n = n ** 2
        x, y = 0, 0
        m = 1
        direct = "right"
        while m <= n:
            if direct == "right":
                matrix[y][x] = m
                m += 1
                x += 1
            elif direct == "down":
                matrix[y][x] = m
                m += 1
                y += 1
            elif direct == "left":
                matrix[y][x] = m
                m += 1
                x -= 1
            elif direct == "up":
                matrix[y][x] = m
                m += 1
                y -= 1
            
            if x == right_max and direct == "right":
                direct = "down"
                right_max -= 1
            elif y == bottom_max and direct == "down":
                direct = "left"
                bottom_max -= 1
            elif x == left_max and direct == "left":
                direct = "up"
                left_max += 1
            elif y == top_max and direct == "up":
                direct = "right"
                top_max += 1