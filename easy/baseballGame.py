def baseballGame(ops):
    points = []
    for opr in ops:
        if opr == 'C':
            points.pop()
            print(points)
        elif opr == 'D':
            val = 2*points[len(points)-1]
            points.append(val)
            print(points)
        elif opr == '+':
            val = points[len(points)-1] + points[len(points)-2]
            points.append(val)
            print(points)
        else:
            points.append(int(opr))
            print(points)

    return sum(points)

print(baseballGame(ops = ["1","C"]))