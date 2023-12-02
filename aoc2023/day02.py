from aoc2023.day import Day

class Day02 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = False
        self.input = self.read_file_lines()

    def _is_possible(self, draws):
        max_red = 12
        max_green = 13
        max_blue = 14
        for draw in draws.split(";"):
            for color in draw.split(","):
                _cnt,col = color.strip().split(" ")
                cnt = int(_cnt)
                if col == "red" and cnt > max_red:
                    return False
                if col == "blue" and cnt > max_blue:
                    return False
                if col == "green" and cnt > max_green:
                    return False
        return True
    
    def _calc_power(self, draws):
        max_red = 0
        max_green = 0
        max_blue = 0
        for draw in draws.split(";"):
            for color in draw.split(","):
                _cnt,col = color.strip().split(" ")
                cnt = int(_cnt)
                if col == "red" and cnt > max_red:
                    max_red = cnt
                if col == "blue" and cnt > max_blue:
                    max_blue = cnt
                if col == "green" and cnt > max_green:
                    max_green = cnt
        return max_red * max_green * max_blue
    
    def solve_1(self):
        sum = 0
        for game in self.input:
            gameid,draws = game.split(":")
            if self._is_possible(draws):
                sum += int(gameid.split(" ")[1].strip())
        return sum

    def solve_2(self):
        return sum(self._calc_power(game.split(":")[1]) for game in self.input)