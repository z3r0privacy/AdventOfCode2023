from aoc2023.day import Day


class Day11 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self.input = self.read_file_lines()

    def solve_1(self):
        pos_list = []
        offset_top = 0
        for y in range(len(self.input)):
            has_g = False
            for x in range(len(self.input[y])):
                if self.input[y][x] == '#':
                    pos_list.append((x, y+offset_top))
                    has_g = True
            if not has_g:
                offset_top += 1
        for x in range(len(self.input[0])-1, -1, -1):
            if all(self.input[y][x] != '#' for y in range(len(self.input))):
                for i in range(len(pos_list)):
                    if pos_list[i][0] > x:
                        pos_list[i] = (pos_list[i][0]+1, pos_list[i][1])
        #print(pos_list)
        sum = 0
        for i in range(len(pos_list)):
            for j in range(i+1, len(pos_list)):
                d = abs(pos_list[i][0]-pos_list[j][0]) + abs(pos_list[i][1]-pos_list[j][1])
                sum += d
                #print(f"{pos_list[i]} - {pos_list[j]} = {d}")
        return sum

    def solve_2(self):
        pos_list = []
        offset_top = 0
        mult = 1000000
        for y in range(len(self.input)):
            has_g = False
            for x in range(len(self.input[y])):
                if self.input[y][x] == '#':
                    pos_list.append((x, y+offset_top))
                    has_g = True
            if not has_g:
                offset_top += mult-1
        for x in range(len(self.input[0])-1, -1, -1):
            if all(self.input[y][x] != '#' for y in range(len(self.input))):
                for i in range(len(pos_list)):
                    if pos_list[i][0] > x:
                        pos_list[i] = (pos_list[i][0]+mult-1, pos_list[i][1])
        #print(pos_list)
        sum = 0
        for i in range(len(pos_list)):
            for j in range(i+1, len(pos_list)):
                d = abs(pos_list[i][0]-pos_list[j][0]) + abs(pos_list[i][1]-pos_list[j][1])
                sum += d
                #print(f"{pos_list[i]} - {pos_list[j]} = {d}")
        return sum