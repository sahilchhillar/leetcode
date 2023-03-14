def fairCandySwap(alice, bob):
    suma, sumb = sum(alice), sum(bob)
    setb = set(bob)

    for a in alice:
        if a + (sumb - suma)/2 in setb:
            return [a, a + (sumb - suma)/2]

print(fairCandySwap(alice = [1,1], bob = [2,2]))