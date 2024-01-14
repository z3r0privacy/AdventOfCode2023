from aoc2023.day import Day

class Day12 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = False
        self.input = self.read_file_lines()
        self.cache = {}

    def place_stones(self, state, groups, req_stones, req_nostones, max_len):
        if len(groups) == 0:
            if len(state) > max_len:
                return 0
            if any((i >= len(state) or state[i] != '#') for i in req_stones):
                return 0
            if any((i < len(state) and state[i] != '.') for i in req_nostones):
                return 0
            return 1
        min_len = sum(groups)+len(groups)-1
        total = 0
        for nz in range(1 if len(state) > 0 else 0, max_len-min_len-len(state)+1):
            c = self.place_stones(state+list(nz*".")+list(groups[0]*"#"), groups[1:], req_stones, req_nostones, max_len)
            total += c
        return total

    def count_num_possibilities(self, row, part2=False):
        conds, _groups = row.split(" ")
        if part2:
            conds = conds+"?"+conds 
            _groups = _groups+","+_groups 
        groups = [int(i) for i in _groups.split(",")]
        req_stones = [i for i in range(len(conds)) if conds[i] == '#']
        req_nostones = [i for i in range(len(conds)) if conds[i] == '.']
        num_stones = self.place_stones([], groups, req_stones, req_nostones, len(conds))
        if part2:
            b = self.cache[row]
            mul = num_stones / b
            return int(b*mul*mul*mul*mul)
        else:
            self.cache[row] = num_stones
        return num_stones


    def solve_1(self):
        return sum(self.count_num_possibilities(r) for r in self.input)

    def solve_2(self):
        return sum(self.count_num_possibilities(r, part2=True) for r in self.input)