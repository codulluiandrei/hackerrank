#!/bin/python3
if __name__ == '__main__':
    x = int(input()) + 1
    y = int(input()) + 1
    z = int(input()) + 1
    n = int(input())
    result = [
        [xt, yt, zt]
        for xt in range(x)
        for yt in range(y) 
        for zt in range(z) 
        if xt + yt + zt != n
    ] 
    print(result)