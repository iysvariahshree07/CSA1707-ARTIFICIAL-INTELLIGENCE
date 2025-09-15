def water_jug(x, y, target):
    seen = set()
    def dfs(a,b):
        if (a,b) in seen: return
        print(a,b)
        if a==target or b==target: return True
        seen.add((a,b))
        return (dfs(x,b) or dfs(0,b) or dfs(a,y) or dfs(a,0) or
                dfs(min(a+b,x), max(0,a+b-x)) or dfs(max(0,a+b-y), min(a+b,y)))
    dfs(0,0)

water_jug(4,3,2)
