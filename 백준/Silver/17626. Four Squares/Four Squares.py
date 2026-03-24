import sys

def chk(n, is_sq, sq):

    if is_sq[n]:
        return 1

    m = len(sq)

    for i in range(m):
        if sq[i] > n :
            break
        if is_sq[n-sq[i]]:
            return 2

    for i in range(m):
        if sq[i] > n :
            break
        for j in range(i, m):
            target = n - (sq[i] + sq[j])
            if target <0 :
                break
            if is_sq[target]:
                return 3

    return 4


is_sq = [False] * 50001
sq = []
i = 1
while i*i <= 50000:
    is_sq[i*i] = True
    sq.append(i*i)
    i+=1


n = int(sys.stdin.readline())
print(chk(n, is_sq, sq))