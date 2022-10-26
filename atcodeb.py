h, w = list(map(int, input().split()))
matrix = []
res = [0] * w
for i in range(h):		 
    s = input()
    cur = []
    for i in s:	 
        cur.append(1 if i == '#' else 0)
    matrix.append(cur)

for i in range(w):
    for j in range(h):
        res[i] += matrix[j][i]
for ele in res:
    print(ele, end = ' ')
        
       
