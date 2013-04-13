#!/usr/bin/env python3
# MZ
# 142913828922 

max = 2000000
map = [True] * (max + 1);
sum = 0

for i in range(2, max + 1):
    if map[i]:
        sum += i
        j = i
        while j <= max:
            map[j] = False
            j = j + i

print(sum)
