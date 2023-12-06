from dataclasses import dataclass, field


@dataclass
class MapRange:
    dest_range_start: int
    src_range_start: int
    range_len: int

    def in_range(self, num: int) -> bool:
        return self.src_range_start <= num <= self.src_range_start + self.range_len
    
    def closest_encounter(self, num: int) -> int:
        # Distance to the start of the range:
        if num < self.src_range_start:
            return self.src_range_start - num
        # If the number is in the range:
        if self.in_range(num):
            return (self.src_range_start + self.range_len) - num
        else:
            return 9999999999

    @property
    def offset(self) -> int:
        return self.dest_range_start - self.src_range_start