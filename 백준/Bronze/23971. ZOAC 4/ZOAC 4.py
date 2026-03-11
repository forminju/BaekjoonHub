H,W,N,M = map(int, input().split())

import math

row_count = math.ceil(H / (N+1))
col_count = math.ceil(W / (M+1))

print(row_count * col_count)