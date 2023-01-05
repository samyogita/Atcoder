n = int(input())
char = list(input())
found = False
for i in range(n):
    if char[i] == ',' and found == False:
        char[i] = '.'
    elif char[i] == '"':
        found ^= 1
print(*char, sep ='')


