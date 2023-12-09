from dataclasses import dataclass


@dataclass
class History:
    tiers: list[list[int]]

    def populate(self) -> None:
        while not self.population_complete:
            self._add_layer()
        return
    
    def _add_layer(self):
        prev = self.tiers[-1][0] # Get the first number of the bottom tier
        # Add a new empty layer
        self.tiers.append([])
        for n in self.tiers[-2][1:]:
            self.tiers[-1].append(n-prev)
            prev = n

    @property
    def population_complete(self):
        for n in self.tiers[-1]:
            if n != 0:
                return False
        return True


    
    def extrapolate(self) -> int:
        # Add a zero to the bottom tier
        current_tier_numer = -1
        for tier in self.tiers[::-1]:
            if current_tier_numer == -1:
                tier.append(0)
                current_tier_numer -= 1
                continue
            tier.append(tier[-1] + self.tiers[current_tier_numer+1][-1])
            current_tier_numer -= 1
        return self.tiers[0][-1]
    
    def extrapolate_back(self) -> int:
        # Add a zero to the bottom tier
        current_tier_numer = -1
        for tier in self.tiers[::-1]:
            if current_tier_numer == -1:
                tier.append(0)
                current_tier_numer -= 1
                continue
            tier.insert(0, tier[0] - self.tiers[current_tier_numer+1][0])
            current_tier_numer -= 1
        print(self.tiers)
        return self.tiers[0][0]