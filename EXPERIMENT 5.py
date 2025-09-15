from collections import deque

def missionaries_cannibals():
    start = (3,3,1)  # 3 missionaries, 3 cannibals, boat left
    goal = (0,0,0)
    q = deque([(start, [])])
    seen = {start}
    while q:
        (M,C,B), path = q.popleft()
        if (M,C,B)==goal:
            for step in path+[(M,C,B)]:
                print(step)
            return
        moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
        for m,c in moves:
            if B==1: new = (M-m,C-c,0)
            else:    new = (M+m,C+c,1)
            M2,C2,B2 = new
            if 0<=M2<=3 and 0<=C2<=3:
                if (M2==0 or M2>=C2) and (3-M2==0 or 3-M2>=3-C2):
                    if new not in seen:
                        seen.add(new)
                        q.append((new,path+[(M,C,B)]))

missionaries_cannibals()
