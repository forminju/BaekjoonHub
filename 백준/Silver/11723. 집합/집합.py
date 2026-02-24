import sys
input = sys.stdin.readline

m = int(input())
S = set()

for i in range(m):
    cmd = input().split()

    if cmd[0] == 'add' :
        x= int(cmd[1])
        S.add(x)

    elif cmd[0] == 'remove' :
        x = int(cmd[1])
        S.discard(x)

    elif cmd[0] == 'check':
        x = int(cmd[1])
        if x in S:
            print(1)
        else:
            print(0)

    elif cmd[0] == 'toggle':
        x = int(cmd[1])
        if x in S:
            S.remove(x)
        else:
            S.add(x)

    elif cmd[0] == 'all':
        S = set(range(1,21))

    elif cmd[0] == 'empty' :
        S.clear()


