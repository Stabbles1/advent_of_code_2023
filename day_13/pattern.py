
from dataclasses import dataclass


@dataclass
class Pattern:
    grid: list[str]
    smudge_value = -1
    smudge_vertical = -1
    smudge_horizontal = -1

    @staticmethod
    def get_candidate_reflections(l: str, remaining_candidates: list[int]) -> list[int]:
        # Can be optimised by passing in the remaining candidates
        #print(l)
        candidates = []
        for mirror_index in remaining_candidates:
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


    def find_vertical_reflection(self, with_smudge) -> int:
        remaining_candidates = list(range(1, len(self.grid[0])))
        for line in self.grid:
            new_candidates = self.get_candidate_reflections(line, remaining_candidates)
            remaining_candidates = list(set(remaining_candidates).intersection(new_candidates))
            if remaining_candidates == []:
                raise IndexError

        if with_smudge == False and self.smudge_vertical in remaining_candidates:
            remaining_candidates.remove(self.smudge_vertical)
        if len(remaining_candidates) > 1:
            raise Exception(f"This should never happen vertical {remaining_candidates} {self}")
        if with_smudge:
            self.smudge_vertical = remaining_candidates[0]
        return remaining_candidates[0]
    
    def find_horizontal_reflection(self, with_smudge) -> int:
        constructed_lines = []
        for x in range(0, len(self.grid[0])):
            constructed_lines.append("")
            for y in range(0, len(self.grid)):
                constructed_lines[x] += self.grid[y][x]

        remaining_candidates = list(range(1, len(constructed_lines[0])))
        
        for line in constructed_lines:
            new_candidates = self.get_candidate_reflections(line, remaining_candidates)
            remaining_candidates = list(set(remaining_candidates).intersection(new_candidates))
            if remaining_candidates == []:
                raise IndexError
        if with_smudge == False and self.smudge_horizontal in remaining_candidates:
            remaining_candidates.remove(self.smudge_horizontal)
        if len(remaining_candidates) > 1:
            raise Exception(f"This should never happen horizontal {remaining_candidates} {self}")
        if with_smudge:
            self.smudge_horizontal = remaining_candidates[0]
        return remaining_candidates[0]
        


    def value(self, with_smudge=True) -> int:
        try:
            return 100 * self.find_horizontal_reflection(with_smudge)
        except IndexError:
            pass
        try:
            return self.find_vertical_reflection(with_smudge)
        except IndexError:
            return
        
    def swap_value(self, y, x):
        #print(f"Trying smudge @ {y=} {x=}")
        if self.grid[y][x] == ".":
            self.grid[y] = self.grid[y][:x] + "#" + self.grid[y][x+1:]
        else:
            self.grid[y] = self.grid[y][:x] + "." + self.grid[y][x+1:]


    def smudgeless_value(self) -> int:
        self.smudge_value = self.value()
        for smudge_y in range(0, len(self.grid)):
            for smudge_x in range(0, len(self.grid[0])):
                self.swap_value(smudge_y, smudge_x)
                result = self.value(with_smudge=False)
                if result != None and result != self.smudge_value:
                    return result
                else:
                    #Put the smudge back to try another
                    self.swap_value(smudge_y, smudge_x)
        