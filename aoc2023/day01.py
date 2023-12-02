from aoc2023.day import Day

class Day01 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self.input = self.read_file_lines()

    def _get_value_at_pos(self, line, use_spelled=False):
        spelled_digits = {
            "zero": 0,
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9
        }
        if '0' <= line[0] <= '9':
            return int(line[0])
        if use_spelled:
            for w,v in spelled_digits.items():
                if line.startswith(w):
                    return v
        return None

    def solve_1(self):
        sum = 0
        for l in self.input:
            for i in range(len(l)):
                v = self._get_value_at_pos(l[i:])
                if v is not None:
                    sum += 10*v
                    break
            for i in range(1,len(l)+1):
                v = self._get_value_at_pos(l[-i:])
                if v is not None:
                    sum += v
                    break
        return sum

    def solve_2(self):
        sum = 0
        for l in self.input:
            for i in range(len(l)):
                v = self._get_value_at_pos(l[i:], use_spelled=True)
                if v is not None:
                    sum += 10*v
                    break
            for i in range(1,len(l)+1):
                v = self._get_value_at_pos(l[-i:], use_spelled=True)
                if v is not None:
                    sum += v
                    break
        return sum
        