# https://atcoder.jp/contests/abc406 contest link

import numpy as np

def val_check(vals: list[int])-> str:
    
    
    if vals[0]>=24 or vals[2] >=24 or vals[1] >=60 or vals[3]>=60:
        return "No"
    if vals[0] > vals[2]:
        return "Yes"
    if vals[0] == vals[2]:
        if vals[1] >= vals[3]:
            return "Yes"
    return "No"

a = input()
b = a.split(" ")

for idx, ch in enumerate(b):
    b[idx] = int(float(ch))
    
print(val_check(b))
