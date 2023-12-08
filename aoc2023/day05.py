from aoc2023.day import Day

class Day05 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self.input = self.read_file_lines()

    def _transition(self, seed, map):
        for start_inc, end_exc, dist in map:
            if start_inc <= seed < end_exc:
                return seed + dist
        return seed

    def solve_1(self):
        mappings = []
        curr_map = []
        curr_line = 3
        while curr_line < len(self.input):
            if not self.input[curr_line]:
                curr_line += 2
                mappings.append(curr_map)
                curr_map = []
                continue
            nums = self.input[curr_line].split(" ")
            dest_start, source_start, range_len = [int(i) for i in nums]
            curr_map.append((source_start, source_start+range_len, dest_start-source_start))
            curr_line += 1
        mappings.append(curr_map)

        min_dist = None
        for seed in [int(i) for i in self.input[0].split(": ")[1].split(" ")]:
            for map in mappings:
                seed = self._transition(seed, map)
            if min_dist is None or seed < min_dist:
                min_dist = seed
        return min_dist

    def _get_range(self, seed, map):
        next_bigger = None
        for start_inc, end_exc, dist in map:
            if start_inc <= seed < end_exc:
                return seed+dist, end_exc-seed
            elif start_inc > seed and (next_bigger is None or start_inc < next_bigger):
                next_bigger = start_inc
        if next_bigger is not None:
            return seed, next_bigger-seed
        return seed, -1

    def _calc_range_seeds(self, seeds, mappings, map_idx):
        results = []
        _map = mappings[map_idx]
        for s_start, s_len in seeds:
            c_start, c_len = s_start, s_len
            new_seeds = []
            while c_len:
                new_start, max_len = self._get_range(c_start, _map)
                if max_len == -1:
                    max_len = c_len
                eff_len = min(max_len, c_len)
                new_seeds.append((new_start, eff_len))
                c_start += eff_len
                c_len -= eff_len
            if map_idx == len(mappings)-1:
                results.append(min(s[0] for s in new_seeds))
            else:
                results.append(self._calc_range_seeds(new_seeds, mappings, map_idx+1))
        return min(results)


    def solve_2(self):
        mappings = []
        curr_map = []
        curr_line = 3
        while curr_line < len(self.input):
            if not self.input[curr_line]:
                curr_line += 2
                mappings.append(curr_map)
                curr_map = []
                continue
            nums = self.input[curr_line].split(" ")
            dest_start, source_start, range_len = [int(i) for i in nums]
            curr_map.append((source_start, source_start+range_len, dest_start-source_start))
            curr_line += 1
        mappings.append(curr_map)

        seed_nums = [int(i) for i in self.input[0].split(": ")[1].split(" ")]
        seeds = []
        for i in range(0, len(seed_nums), 2):
            seeds.append((seed_nums[i], seed_nums[i+1]))
        return self._calc_range_seeds(seeds,mappings, 0)
