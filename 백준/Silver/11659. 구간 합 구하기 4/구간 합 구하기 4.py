import sys

input = sys.stdin.readline
n,m = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0] * (n+1)
temp = 0

for i in range(n):
    temp += arr[i]
    prefix_sum[i+1] = temp

for _ in range(m):
    a,b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])