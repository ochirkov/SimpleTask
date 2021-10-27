#!/usr/bin/env python
from random import randrange


a = []

while len(a) != 10:
    r = randrange(10)
    if r not in a:
        a.append(r)

print(a)