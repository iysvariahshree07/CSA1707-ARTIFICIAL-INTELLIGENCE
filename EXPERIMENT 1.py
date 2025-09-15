from collections import deque

def is_solvable(state):
    flat = [x for x in state if x != 0]
    inv = sum(flat[i] > flat[j] for i in range(len(flat)) for j in range(i+1, len(flat)))
    return inv % 2 == 0

def bfs(start, goal):
    q = deque([(start, [])])
    seen = {tuple(start)}
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    while q:
        state, path = q.popleft()
        if state == goal:
            return path+[state]
        z = state.index(0)
        x, y = divmod(z, 3)
        for dx,dy in moves:
            nx, ny = x+dx, y+dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                nz = nx*3+ny
                new = state[:]
                new[z], new[nz] = new[nz], new[z]
                if tuple(new) not in seen:
                    seen.add(tuple(new))
                    q.append((new, path+[state]))
    return None

start = [1,2,3,4,0,5,6,7,8]
goal = [1,2,3,4,5,6,7,8,0]

if is_solvable(start):
    path = bfs(start, goal)
    for step in path:
        print(step)
else:
    print("Unsolvable")
