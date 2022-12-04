n = int(input())
s = list(map(int, input().split()))
res = [0] * n
res[0] = s[0]
for i in range(1, n):
    res[i] = s[i] - s[i-1]
print(' '.join(map(str, res)))