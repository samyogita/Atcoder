def solve(h, m):
    time = []
    if h < 10:
        H = '0' + str(h)
    else:
        H = str(h)
    if m < 10:
        M = '0' + str(m)
    else:
        M = str(m)

    for i in H:
        time.append(i)
    for j in M:
        time.append(j)
    a = time[0]
    b = time[1]
    c = time[2]
    d = time[3]
    b, c = c, b
    if (a == '2' and b > '3') or c > '5':
        return False
    return True

found = False
h, m= list(map(int, input().split()))
startingmin = m
for hour in range(h, 24):
    for min in range(startingmin, 60):
        if solve(hour, min):
            found = True
            print(hour, min)
            break
    startingmin = 0
    if found:
        break
if found == False:
    print('00 00')









    


        

