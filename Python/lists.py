#!/bin/python3
if __name__ == '__main__':
    N = int(input())
    ans = []
    for _ in range(N):
        temp = list(input().split())
        if temp[0] == 'insert':
            ans.insert(int(temp[1]), int(temp[2]))
        elif temp[0] == 'remove':
            ans.remove(int(temp[1]))
        elif temp[0] == 'append':
            ans.append(int(temp[1]))
        elif temp[0] == 'sort':
            ans.sort()
        elif temp[0] == 'pop':
            ans.pop()
        elif temp[0] == 'reverse':
            ans.reverse()
        elif temp[0] == 'index':
            var = ans.index(int(temp[1]))
            print(var)
        elif temp[0] == 'print':
            print(ans)