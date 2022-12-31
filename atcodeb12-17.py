from collections import defaultdict
n, m = list(map(int, input().split()))
cnt = 0
g = defaultdict(set)
for i in range(n):
    val = input()
    for j in range(m):
        if val[j] == 'o':
            g[i].add(j)
    
for x in range(n):
    for y in range(x+1, n):
        D = set()
        D = g[x].union(g[y])
        if len(D) == m:
            cnt += 1
print(cnt)

