"""
## Collect Rewards
Karel starts at the left end of the first row. 
Along her way, there are prizes, at each corner there may be multiple, disguised as beepers. 
Your job is to move Karel untill the end of the row and pick the prizes along her way.
"""
from karel.stanfordkarel import *

def collect_prizes_in_corner():
    while beepers_present():
        pick_beeper()

while front_is_clear():
    collect_prizes_in_corner()
    move()
collect_prizes_in_corner()

