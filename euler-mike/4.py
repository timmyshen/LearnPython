#!/usr/bin/env python3
# MZ
# 906609
# Brutal Force

def check(num):
    def _check(numlst):
        if len(numlst) <= 1: return True
        return numlst[0] == numlst[-1] and check(numlst[1:len(numlst) -1])
    return _check(str(num))

max = -1
for i in range(100, 1000):
    for j in range(100, 1000):
        if check(i * j) and i * j > max:
            max = i * j;

print(max);
