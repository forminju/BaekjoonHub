import sys
input = sys.stdin.readline

n,m = map(int, input().split())

hear = set()
for _ in range(n):
  hear.add(input().strip())

both = []
for _ in range(m):
  name = input().strip()
  if name in hear:
    both.append(name)

both.sort()

print(len(both))
print("\n".join(both))
