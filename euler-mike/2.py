#!/usr/bin/env python3
# MZ
# 4613732 

fib = [1, 2]
sum = 2
i = 2

while True:
    fib[i:] = [fib[i - 1] + fib[i - 2]]
    if fib[i] > 4e6:
        break
    if fib[i] % 2 == 0:
        sum = sum + fib[i]
    i = i + 1

print(sum)
