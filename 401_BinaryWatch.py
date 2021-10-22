from typing import List, Tuple
from itertools import combinations

LEDS_POSSIBILITIES = [
    "H1", "H2", "H4", "H8",
    "M1", "M2", "M4", "M8", "M16", "M32"
]

def hour_mins(hs: List[str]) -> Tuple[int, int]:
    hours = mins = 0
    for x in hs:
        if x[0] == "H":
            hours += int(x[1:])
        else:
            mins += int(x[1:])
    return hours, mins

def format_hour_mins(hours: int, mins: int) -> str:
    mins = f"0{mins}" if mins < 10 else str(mins)
    return f"{hours}:{mins}"

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        res = []
        for h in range(12):
            for m in range(60):
                if (bin(h).count('1') + bin(m).count('1')) == turnedOn:
                    res.append(f'{h}:{m:02d}')
        return res


    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        res = []
        for hour in range(0,12):
            for minumte in range(0,60):

                hourOne = bin(hour).count('1')
                minumteOne = bin(minumte).count('1')

                if hourOne <= 4 and minumteOne <= 6:
                    if hourOne + minumteOne == turnedOn:
                        res.append(str(hour)+':'+str(minumte).zfill(2))

        return res

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # combinations(p,r) is all possible results where set of objects p split same length(r).
        xs = combinations(LEDS_POSSIBILITIES, turnedOn)
        ans = []
        print(xs)
        for hs in xs:
            hours, mins = hour_mins(hs)
            if hours < 12 and mins < 60:
                ans.append(format_hour_mins(hours, mins))
        return ans