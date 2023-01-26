#!/usr/bin/env python3

def print_fibonacci(length):
    result = []
    if length > 0:
        result.append(0)
        if length > 1:
            result.append(1)
            if length > 2:
                i = 2
                while i < length:
                    number = result[-2] + result[-1]
                    result.append(number)
                    i += 1
    print(result)
    