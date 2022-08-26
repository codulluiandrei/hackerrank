#!/bin/python2
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().strip().split(" "))
    print(hash(tuple(integer_list)))
