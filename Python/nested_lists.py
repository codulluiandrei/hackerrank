#!/bin/python3
if __name__ == '__main__':
    name = []
    score = []
    for _ in range(int(input())):
        name.append(input())
        score.append(float(input()))
    minim = min(score)
    result = []
    for i in range(len(score)):
        if score[i] == minim:
            score[i] = 1000000000
    minim = min(score)
    for i in range(len(score)):
        if score[i] == minim:
            result.append(name[i])
    result.sort()
    for i in result:
        print(i)