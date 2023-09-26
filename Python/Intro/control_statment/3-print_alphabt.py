#!/usr/bin/python3
"""A program that prints the ASCII alphabet in lowercase
and not followed by a new line"""

for alpha in range(ord('a'), ord('z') + 1):
    alpha = chr(alpha)
    if alpha not in 'qe':
        print(alpha, end='')