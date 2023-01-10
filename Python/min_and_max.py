#!/bin/python3
import numpy
n, m = map(int,input().split())
mat = numpy.array([[int(x) for x in input().split()] for _ in range(n)])
print(numpy.max(numpy.min(mat, axis = 1)))
