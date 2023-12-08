from aoc2023.day import Day

class Day07 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self.input = self.read_file_lines()

    def _get_hand_type(self, cards):
        card_count={}
        for c in cards:
            if c not in card_count:
                card_count[c] = 0
            card_count[c] += 1
        count_list = list(card_count.values())
        count_list.sort(reverse=True)
        if count_list == [5]:
            # five of a kind
            return 7 
        if count_list == [4,1]:
            # four of a kind
            return 6
        if count_list == [3,2]:
            # full house
            return 5
        if count_list == [3,1,1]:
            # three of a kind
            return 4
        if count_list == [2,2,1]:
            # two pairs
            return 3
        if count_list == [2,1,1,1]:
            # one pair
            return 2
        if count_list == [1,1,1,1,1]:
            return 1
        raise Exception("Invalid Count State")
    
    def _get_hand_type_joker(self, cards):
        card_count={}
        for c in cards:
            if c not in card_count:
                card_count[c] = 0
            card_count[c] += 1
        num_j = card_count[1] if 1 in card_count else 0
        if 1 in card_count:
            del card_count[1]
        count_list = list(card_count.values())
        if len(count_list) == 0:
            # all 5 cards J
            count_list.append(0)
        count_list.sort(reverse=True)
        count_list[0] += num_j
        if count_list == [5]:
            # five of a kind
            return 7 
        if count_list == [4,1]:
            # four of a kind
            return 6
        if count_list == [3,2]:
            # full house
            return 5
        if count_list == [3,1,1]:
            # three of a kind
            return 4
        if count_list == [2,2,1]:
            # two pairs
            return 3
        if count_list == [2,1,1,1]:
            # one pair
            return 2
        if count_list == [1,1,1,1,1]:
            return 1
        raise Exception("Invalid Count State")

    def solve_1(self):
        pts = {str(i):i for i in range(2,10)}
        pts.update({
            # A, K, Q, J, T
            'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
        })
        hands = []
        for line in self.input:
            hand,bid = line.split(" ")
            p_hand = [pts[c] for c in hand]
            hands.append((p_hand, self._get_hand_type(p_hand), int(bid)))
        hands.sort(key=lambda h: (h[1], *h[0]))
        sum = 0
        mult = 1
        for _,_,p in hands:
            sum += p*mult
            mult += 1
        return sum

    def solve_2(self):
        pts = {str(i):i for i in range(2,10)}
        pts.update({
            # A, K, Q, J, T
            'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14
        })
        hands = []
        for line in self.input:
            hand,bid = line.split(" ")
            p_hand = [pts[c] for c in hand]
            hands.append((p_hand, self._get_hand_type_joker(p_hand), int(bid)))
        hands.sort(key=lambda h: (h[1], *h[0]))
        sum = 0
        mult = 1
        for _,_,p in hands:
            sum += p*mult
            mult += 1
        return sum
