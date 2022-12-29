n = int(input())

A = list(map(int, input().split()))

q = int(input())
for i in range(q):
    query = list(map(int, input().split())) 
    if query[0] == 2:
        k = query[1] - 1
        print(A[k])
    else:
        pass
        k, x = query[1], query[2]
        A[k-1] = x


