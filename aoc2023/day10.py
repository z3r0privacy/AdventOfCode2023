from aoc2023.day import Day

class Day10 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
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
        cnt = 0
        cx, cy = x+d[0], y+d[1]
        prev = ''
        while cx >= 0 and cy >= 0 and cy < len(self.input) and cx < len(self.input[cy]):
            if (cx, cy) in self.path:
                if not (d[0] == 0 and self.input[cy][cx] == '|'):
                    if not(d[1] == 0 and self.input[cy][cx] == '-'):
                        pn = [prev, self.input[cy][cx]]
                        if not(d[0] == 1 and pn in [["L", "7"], ["F", "J"]]):
                            if not(d[0] == -1 and pn in [["J", "F"], ["7", "L"]]):
                                if not(d[1] == 1 and pn in [['7', 'L'], ['F', 'J']]):
                                    if not(d[1] == -1 and pn in [['J', 'F'], ['L', '7']]):
                                        cnt += 1
                        prev = self.input[cy][cx]
            elif (cx,cy) in self.p2_cache:
                return self.p2_cache[(cx,cy)][d] + cnt
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
        
        dx = self.path[1][0] - self.path[-1][0]
        dy = self.path[1][1] - self.path[-1][1]
        sval = ''
        if (dx == 0 and dy == 2) or (dx == 0 and dy == -2):
            sval = "|"
        elif (dx == 2 and dy == 0) or (dx == -2 and dy == 0):
            sval = '='
        elif dx == 1 and dy == 1:
            sval = "L"
        elif dx == -1 and dy == 1:
            sval == "J"
        elif dx == -1 and dy == -1:
            sval = "7"
        elif dx == 1 and dy == -1:
            sval = "F"
        if sval == "":
            raise RuntimeError()
        self.input[sy] = self.input[sy][:sx] + sval + self.input[sy][sx+1:]
        return int(len(path)/2)

    def solve_2(self):
        cnt = 0
        self.p2_cache = {}
        for y in range(len(self.input)):
            for x in range(len(self.input[y])):
                if (x,y) in self.path:
                    continue
                cl = self.count_path_tiles(x,y,(-1, 0))
                cu = self.count_path_tiles(x,y,(0, -1))
                self.p2_cache[(x,y)] = {
                    (-1, 0): cl,
                    (0, -1): cu
                }
                if cl&1 == 1 and cu&1 == 1:
                    cnt += 1
        return cnt
