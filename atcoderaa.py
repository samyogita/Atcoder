n, k = list(map(int, input().split()))
ele = list(map(int, input().split()))
for i in range(0, k):
    ele.remove(ele[0])
    ele.append(0)
for j in ele:
    print(j , end = ' ')