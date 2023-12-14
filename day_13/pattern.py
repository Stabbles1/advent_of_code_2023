
from dataclasses import dataclass


@dataclass
class Pattern:
    grid: list[str]

    @staticmethod
    def get_candidate_reflections(l: str) -> list[int]:
        # Can be optimised by passing in the remaining candidates
        #print(l)
        candidates = []
        line_length = len(l)
        for mirror_index in range(1,line_length):
            left = l[:mirror_index]
            right = l[mirror_index:]
            smallest_list = min(len(left), len(right))
            is_candidate = True
            #print(f"{left=} {right=}")
            for window in range(1, smallest_list+1):
                if left[-window] == right[window-1]:
                    continue
                else:
                    is_candidate = False
            if is_candidate:
                #print(f"Reflection candidate at {mirror_index}")
                candidates.append(mirror_index)
        return candidates


    def find_vertical_reflection(self) -> int:
        remaining_candidates = None
        for line in self.grid:
            if remaining_candidates == None:
                remaining_candidates = self.get_candidate_reflections(line)
            else:
                new_candidates = self.get_candidate_reflections(line)
                remaining_candidates = list(set(remaining_candidates).intersection(new_candidates))
            if remaining_candidates == []:
                raise IndexError

        if len(remaining_candidates) > 1:
            raise Exception("This should never happen")
        return remaining_candidates[0]
    
    def find_horizontal_reflection(self) -> int:
        remaining_candidates = None
        constructed_lines = []
        for x in range(0, len(self.grid[0])):
            constructed_lines.append("")
            for y in range(0, len(self.grid)):
                constructed_lines[x] += self.grid[y][x]
        
        for line in constructed_lines:
            if remaining_candidates == None:
                remaining_candidates = self.get_candidate_reflections(line)
            else:
                new_candidates = self.get_candidate_reflections(line)
                remaining_candidates = list(set(remaining_candidates).intersection(new_candidates))
            if remaining_candidates == []:
                raise IndexError

        if len(remaining_candidates) > 1:
            raise Exception("This should never happen")
        return remaining_candidates[0]
        


    def value(self) -> int:
        try:
            return self.find_vertical_reflection()
        except IndexError:
            return 100 * self.find_horizontal_reflection()