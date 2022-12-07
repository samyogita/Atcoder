from collections import Counter
h, w = list(map(int, input().split()))
s = ['' for _ in range(w)]
t = ['' for _ in range(w)]
for i in range(h):
    a =input()
    for j in range(w):
        
        s[j] += a[j]
for i in range(h):
    b =input()
    for j in range(w):
        
        t[j] += b[j]
print(s)
print(t)
if Counter(s) == Counter(t):
    print('Yes')
else:
    print('No')

