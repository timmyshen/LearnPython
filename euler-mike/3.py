#!/usr/bin/env python3
# MZ
# 6857 

from math import sqrt

bignum = 600851475143

def factor(num, start):
    for i in range(start, int(sqrt(num)) + 1):
        if num % i == 0:
            return factor(num / i, i);
    return num;

print(str(factor(bignum, 2)));
