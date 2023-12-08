from aoc2023.day import Day
import re, math

class Day08 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self.input = self.read_file_lines()

    def solve_1(self):
        directions = self.input[0]
        m = {}
        for line in self.input[2:]:
            r = re.match(r"(\w{3}) = \((\w{3}), (\w{3})\)", line)
            m[r.group(1)] = (r.group(2), r.group(3))
        curr = "AAA"
        count = 0
        while curr != "ZZZ":
            d = directions[count%len(directions)]
            if d == "L":
                curr = m[curr][0]
            else:
                curr = m[curr][1]
            count += 1
        return count

    def solve_2(self):
        directions = self.input[0]
        m = {}
        for line in self.input[2:]:
            r = re.match(r"(\w{3}) = \((\w{3}), (\w{3})\)", line)
            m[r.group(1)] = (r.group(2), r.group(3))
        currents = [p for p in m.keys() if p[2]=='A']
        lens = set()
        count = 0
        while any(c[2]!='Z' for c in currents):
            d = 0 if directions[count%len(directions)] == "L" else 1
            for i in range(len(currents)):
                if currents[i][2] != 'Z':
                    currents[i] = m[currents[i]][d]
                    if currents[i][2] == 'Z':
                        lens.add(count + 1)
            count += 1
        return math.lcm(*lens)
        