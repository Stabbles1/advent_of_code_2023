from dataclasses import dataclass, field


@dataclass
class MapRange:
    dest_range_start: int
    src_range_start: int
    range_len: int

    def in_range(self, num: int) -> bool:
        return self.src_range_start <= num <= self.src_range_start + self.range_len

    @property
    def offset(self) -> int:
        return self.dest_range_start - self.src_range_start