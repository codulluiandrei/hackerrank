#!/bin/python3
import numpy
n, m = map(int, input().split())
a = numpy.array( [list(map(int, input().split())) for _ in range(n)] )
print(numpy.mean(a, axis=1))
print(numpy.var(a, axis=0))
print(round(numpy.std(a), 11))
