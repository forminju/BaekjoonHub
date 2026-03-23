n,m = map(int, input().split())
r,c,d = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
# 방향 : (d+3) % 4

def solve(ci,cj, dr):
    cnt = 0
    while True:
        if arr[ci][cj] == 0:
            arr[ci][cj] = 2
            cnt +=1

        flag = 1
        for _ in range(4):
            dr = (dr+3)%4
            ni,nj = ci+dx[dr], cj+dy[dr]
            if 0<=ni<n and 0<=nj<m and arr[ni][nj] == 0:
                ci, cj = ni,nj
                flag = 0
                break

        if flag == 1:
            bi, bj = ci-dx[dr], cj-dy[dr]
            if 0<=bi<n and 0<=bj<m and arr[bi][bj] != 1:
                    ci,cj = bi,bj

            else:
                return cnt

print(solve(r,c,d))
