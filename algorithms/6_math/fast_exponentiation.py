"""
Imagine you are the co-pilot in the forest rescue helicopter. Our forests are burning fast and only way to save them is for you to 
beat the fire in the exponent-modulo game, ie. you need to answer faster than the fire.

Implement fast_exp function with three integer parameters base, pow and mod returning (base ^ pow) % mod.

They play the exponent game to decide 
"""

from time import time as now


def fast_exp(base, pow, mod):
    if pow == 1:
        return base % mod
    elif pow == 0:
        return 1
    square = fast_exp(base, int(pow/2), mod)
    if pow % 2 == 0:
        return (square ** 2) % mod
    else:
        return (base * square ** 2) % mod


def fire_exp(base, pow, mod):
    return (base ** pow) % mod


def benchmark(tests):
    for test in tests:
        base, pow, forest, mod = test
        user_start = now()
        user_res = fast_exp(base, pow, mod)
        user_end = now()
        fire_res = fire_exp(base, pow, mod)
        fire_end = now()
        print(f"User: {user_end-user_start} ms, Fire: {fire_end-user_end} ms.")
        if user_end - user_start < fire_end - user_end:
            print(f"You saved {forest} forest!")
        else:
            print(f"We couldn't save the {forest} forest :(...")


test_cases = [(1, 100000, "Manavgat", 5343), (2, 50001653, "Kaz Dağları", 39041),
              (6, 107933, "Bodrum", 1293), (9, 43, "Rushmore", 384)]
benchmark(test_cases)
