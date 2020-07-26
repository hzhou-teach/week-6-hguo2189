class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        row = []
        matrix = []
        m = C
        while m > 0:
            row.append(0)
            m -= 1
        m = R
        while m > 0:
            matrix.append(row[:])
            m -= 1
        n = R * C
        direct = "right"
        #r0 is y, c0 is x
        points = [[r0,c0]]
        move_right, move_down, move_left, move_up = 1,1,2,2
        while len(points) < n:
            if direct == "right":
                m = move_right
                while m > 0:
                    c0 += 1
                    m -= 1
                    if 0 <= c0 <= C-1 and 0 <= r0 <= R-1:
                        points.append([r0,c0])
                move_right += 2
                direct = "down"
            elif direct == "down":
                m = move_down
                while m > 0:
                    r0 += 1
                    m -= 1
                    if 0 <= c0 <= C-1 and 0 <= r0 <= R-1:
                        points.append([r0,c0])
                move_down += 2
                direct = "left"
            elif direct == "left":
                m = move_left
                while m > 0:
                    c0 -= 1
                    m -= 1
                    if 0 <= c0 <= C-1 and 0 <= r0 <= R-1:
                        points.append([r0,c0])
                move_left += 2
                direct = "up"
            elif direct == "up":
                m = move_up
                while m > 0:
                    r0 -= 1
                    m -= 1
                    if 0 <= c0 <= C-1 and 0 <= r0 <= R-1:
                        points.append([r0,c0])
                move_up += 2
                direct = "right"
        return points