#!/bin/python3
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        temp = input().split(' ')
        name = temp[0]
        student_marks[name] = (float(temp[1]), float(temp[2]), float(temp[3]))
    query_name = input()
    print('%.2f' % (sum(student_marks[query_name]) / 3))