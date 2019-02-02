from sys import stdin
T = int(stdin.readline())

def get(lp, rp, turn):
    if lp == rp:
        if turn == 0:
            return cards[lp]
        else:
            return 0
        
    if mem[lp][rp][turn] != 0:
        return mem[lp][rp][turn]
        
    result = 0
    # 나라면
    next_turn = 1 if turn == 0 else 0
    
    if turn == 0:
        result = max(cards[lp] + get(lp+1, rp, next_turn), cards[rp] +  get(lp, rp-1, next_turn))
    else:
        result = min(get(lp+1, rp, next_turn), get(lp, rp-1, next_turn))
    
    mem[lp][rp][turn] = result
    
    return result

for t in range(T):
    N = int(stdin.readline())
    cards = [int(x) for x in stdin.readline().split()]
    
    mem = [ [ [0, 0] for _ in range(N)] for _ in range(N)]
    
    print(get(0, N-1, 0))
    