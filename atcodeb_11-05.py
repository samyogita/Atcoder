from collections import defaultdict
n, m = list(map(int, input().split()))
n , m = int(n), int(m)
g = defaultdict(list)
for i in range(m):
    e = list(map(int, input().split()))
    g[e[0]].append(e[1])
    g[e[1]].append(e[0])
for j in range(1, n+1):
    g[j].sort()
    print(len(g[j]), *g[j])