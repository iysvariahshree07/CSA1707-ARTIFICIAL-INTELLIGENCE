import itertools

def solve():
    letters = "SENDMORY"
    for perm in itertools.permutations("0123456789", len(letters)):
        s = dict(zip(letters, perm))
        if s['S']=='0' or s['M']=='0': continue
        SEND = int(s['S']+s['E']+s['N']+s['D'])
        MORE = int(s['M']+s['O']+s['R']+s['E'])
        MONEY= int(s['M']+s['O']+s['N']+s['E']+s['Y'])
        if SEND+MORE==MONEY:
            print("SEND =",SEND,"MORE =",MORE,"MONEY =",MONEY)
            return
solve()
