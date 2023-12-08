from aoc2023.day import Day
import functools, math

class Day06 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self.input = self.read_file_lines()

    def solve_1(self):
        # dist =  (d-x)*x
        # dx - dx² 
        ## derivate to find local max
        # d - 2x == 0
        # 2x = d
        # x = d/2
        # equal points
        # (d-x)*x == r
        # dx - x² = r
        # quadratic formula: ax² + bx + c = 0
        # a: -1, b: d, c:-r  (-dx² + dx -r == 0)
        # x = (-d +/- sqrt(d²-4r))/-2d

        times = [int(i.strip()) for i in self.input[0].split(":")[1].strip().split(" ") if i]
        records = [int(i.strip()) for i in self.input[1].split(":")[1].strip().split(" ") if i]

        counts = []
        for i in range(len(times)):
            a = -1
            b = times[i]
            c = -records[i]
            solutions = [(-b+math.sqrt(b*b-4*a*c))/(2*a), (-b-math.sqrt(b*b-4*a*c))/(2*a)]
            start = math.ceil(min(solutions))
            end = math.floor(max(solutions))+1
            counts.append(end-start)
        return functools.reduce(lambda a,b: a*b, counts) 



    def solve_2(self):
        time = int(self.input[0].split(":")[1].strip().replace(" ", ""))
        record = int(self.input[1].split(":")[1].strip().replace(" ", ""))

        # solve quadratic formula to get record-pushtimes
        a = -1
        b = time
        c = -record
        solutions = [(-b+math.sqrt(b*b-4*a*c))/(2*a), (-b-math.sqrt(b*b-4*a*c))/(2*a)]
        start = math.ceil(min(solutions))
        end = math.floor(max(solutions))+1
        return end-start
