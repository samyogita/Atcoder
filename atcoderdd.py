n = int(input())
mp={0:1}
def solve(n):
    if n == 0:
        return 1
    else:
        if n in mp:
            return mp[n]
        else:
            ans = solve(n//2)+ solve(n//3)
            mp[n] = ans
    return ans
print(solve(n))