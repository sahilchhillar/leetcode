def judgeCircles(moves):
    origin = [0,0]
    for move in moves:
        if move == 'R':
            origin[0] += 1
        elif move == 'L':
            origin[0] -= 1
        elif move == 'U': 
            origin[1] += 1
        elif move == 'D':
            origin[1] -= 1
    
    if origin == [0,0]:
        return True
    return False

print(judgeCircles(moves = "LL"))