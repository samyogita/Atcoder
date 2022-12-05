s = input()
t = input()
l = 0
r = 0
while l < len(s) and r < len(t):
    if s[l] != t[r]:
        break
    l += 1
    r += 1
print(l+1)