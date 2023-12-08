from aoc2023.day import Day

class Day04 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self.input = self.read_file_lines()

    def solve_1(self):
        sum = 0
        for line in self.input:
            line = line.split(":")[1]
            s_winning, s_having = line.split("|")
            winning = [int(n.strip()) for n in s_winning.strip().split(" ") if n]
            having = [int(n.strip()) for n in s_having.strip().split(" ") if n]
            cnt = len([i for i in having if i in winning])
            if cnt > 0:
                sum += 1 << (cnt-1)
        return sum

    def solve_2(self):
        cards_count = {}
        # setup, all original cards
        for line in self.input:
            gamenum = line.split(":")[0].split(" ")[-1]
            cards_count[int(gamenum)] = 1
        #iterate over cards
        for line in self.input:
            gamenum = int(line.split(":")[0].split(" ")[-1])
            s_winning, s_having = line.split(":")[1].split("|")
            winning = [int(n.strip()) for n in s_winning.strip().split(" ") if n]
            having = [int(n.strip()) for n in s_having.strip().split(" ") if n]
            cnt = len([i for i in having if i in winning])
            for i in range(cnt):
                if gamenum+i+1 in cards_count.keys():
                    cards_count[gamenum+i+1] += cards_count[gamenum]
        return sum(cards_count.values())
