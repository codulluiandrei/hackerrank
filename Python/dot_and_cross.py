#!/bin/python3
import numpy
n = int(input())
a = [list(map(int,input().split())) for i in range(n)]
b = [list(map(int,input().split())) for i in range(n)]
print(numpy.dot(a, b))
