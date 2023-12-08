from aoc2023.day import Day
import re

class Day03 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self.input = self.read_file_lines()

    def _is_symbol(self, line, col):
        if line < 0 or line >= len(self.input):
            return False
        if col < 0 or col >= len(self.input[line]):
            return False
        val = self.input[line][col]
        if '0' <= val <= '9':
            return False
        return val != '.'

    def _has_symbol_around(self, line, match):
        for i in range(match.start()-1, match.end()+1):
            if self._is_symbol(line-1, i) or self._is_symbol(line+1, i):
                return True
        return self._is_symbol(line, match.start()-1) or self._is_symbol(line, match.end())

    def solve_1(self):
        sum = 0
        for i, line in enumerate(self.input):
            for m in re.finditer(r"\d+", line):
                if self._has_symbol_around(i, m):
                    sum += int(m.group())
        return sum

    def _get_surrounding_nums(self, x,y,num_locations):
        def match_pos_num(_y, _x, num):
            return _y == num[0] and num[1] <= _x < num[2]
        nums = []
        num_locs = set()
        for dy in [-1,0,1]:
            for dx in [-1,0,1]:
                if dy == 0 and dx == 0:
                    continue
                for n in num_locations:
                    if (n[0],n[1]) in num_locs:
                        continue
                    if match_pos_num(dy+y, dx+x, n):
                        nums.append(int(n[3]))
                        num_locs.add((n[0], n[1]))
        return nums

    def solve_2(self):
        num_locations = []
        gear_locs = []
        for i, line in enumerate(self.input):
            for m in re.finditer(r"\d+", line):
                num_locations.append((i, m.start(), m.end(), m.group()))
            for j,c in enumerate(line):
                if c == '*':
                    gear_locs.append((i,j))
        sum = 0
        for y,x in gear_locs:
            nums = self._get_surrounding_nums(x, y, num_locations)
            if len(nums) == 2:
                sum += nums[0]*nums[1]
        return sum
