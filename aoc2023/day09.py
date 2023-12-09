from aoc2023.day import Day

class Day09 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self.input = self.read_file_lines()

    def get_next_number(self, row):
        rows = []
        rows.append(row)
        while not all(n == 0 for n in rows[-1]):
            prev = rows[-1]
            curr = []
            for i in range(1, len(prev)):
                curr.append(prev[i]-prev[i-1])
            rows.append(curr)
        cumm = 0
        for r in rows[::-1]:
            cumm += r[-1]
        return cumm
    
    def get_prev_number(self, row):
        rows = []
        rows.append(row)
        while not all(n == 0 for n in rows[-1]):
            prev = rows[-1]
            curr = []
            for i in range(1, len(prev)):
                curr.append(prev[i]-prev[i-1])
            rows.append(curr)
        cumm = 0
        for r in rows[::-1]:
            cumm = r[0]-cumm
        return cumm

    def solve_1(self):
        rows = [[int(i) for i in r.split(" ")] for r in self.input]
        return sum(self.get_next_number(r) for r in rows)

    def solve_2(self):
        rows = [[int(i) for i in r.split(" ")] for r in self.input]
        return sum(self.get_prev_number(r) for r in rows)