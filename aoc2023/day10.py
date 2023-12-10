from aoc2023.day import Day

class Day10 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = False
        self.input = self.read_file_lines()
        self.path = []

    def get_next_pos(self, x, y, px, py):
        c = self.input[y][x]
        if c == '|':
            x1, y1 = x, y+1
            x2, y2 = x, y-1
        if c == '-':
            x1, y1 = x-1, y
            x2, y2 = x+1, y
        if c == 'L':
            x1, y1 = x, y-1
            x2, y2 = x+1, y
        if c == 'J':
            x1, y1 = x, y-1
            x2, y2 = x-1, y
        if c == '7':
            x1, y1 = x-1, y
            x2, y2 = x, y+1
        if c == 'F':
            x1, y1 = x+1, y
            x2, y2 = x, y+1
        if x1 == px and y1 == py:
            return x2, y2
        return x1, y1

    def count_path_tiles(self, x, y, d):
        if y == 6 and x == 2:
            pass
        cnt = 0
        cx, cy = x+d[0], y+d[1]
        while cx >= 0 and cy >= 0 and cy < len(self.input) and cx < len(self.input[cy]):
            if (cx, cy) in self.path:
                cnt += 1
                if d[0] == 0 and self.input[cy][cx] == '|':
                    cnt -= 1
                if d[1] == 0 and self.input[cy][cx] == '-':
                    cnt -= 1
            cx, cy = cx+d[0], cy+d[1]
        return cnt

    def solve_1(self):
        sx, sy = -1, -1
        for y in range(len(self.input)):
            for x in range(len(self.input[y])):
                if self.input[y][x] == 'S':
                    sx, sy = x, y
        path = [(sx, sy)]
        if self.input[sy][sx+1] in ['-', 'J', '7']:
            path.append((sx+1, sy))
        elif self.input[sy][sx-1] in ['-', 'L', 'F']:
            path.append((sx-1, sy))
        elif self.input[sy-1][x] in ['|', 'F', '7']:
            path.append((sx, sy-1))
        elif self.input[sy+1][sx] in ['|', 'J', 'L']:
            path.append((sx, sy+1))
        while True:
            nx, ny = self.get_next_pos(path[-1][0], path[-1][1], path[-2][0], path[-2][1])
            if nx == sx and ny == sy:
                break
            path.append((nx, ny))
        self.path = path
        return int(len(path)/2)

    def solve_2(self):
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        cnt = 0
        for y in range(len(self.input)):
            for x in range(len(self.input)):
                if (x,y) in self.path:
                    continue
                in_path = True
                for d in dirs:
                    c = self.count_path_tiles(x, y, d)
                    if c&1 == 0:
                        in_path = False
                if in_path:
                    cnt += 1
        return cnt