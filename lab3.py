'''
Created on Sep 12, 2022

@author: user
'''

def expandWinningSet(domain: int(), W: int()):
    
    if not W:
        for a in domain:
            # Final position criterion
            if a >= 100:
                W.append(a)
        if W:
            W.sort()
        
    else:
        # Next move criteria
        try:
            validRange = list(a for a in domain if a >= W[0]-20 and a < W[0])
            print(f"current valid range: {validRange}")
            for a in validRange:
                # print(f"{a} evaluated")
                if (a + 1 not in W and (a + 2 in W and a + 11 in W)) or (a + 10 not in W and (a + 11 in W and  a + 20 in W)):
                    W.append(a)
                    # print(f"{a} appended")
        except IndexError as e:
            print(e)
        W.sort()
    return W

domain = range(1, 110)
W = []
print(f"Iteration 0")
print(f"Current winning set: {W}")
for i in range(8):
    print(f"Iteration {i + 1}")
    W = expandWinningSet(domain, W)
    print(f"Current winning set: {W}")
    
    
    
    