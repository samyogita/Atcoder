s = list(input())
s.reverse()
pos = -1
for i in range(len(s)):
    if s[i] == 'a':
        pos = len(s) - i 
        break
print(pos)
