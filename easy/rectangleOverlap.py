def rectangleOverlap(rec1, rec2):
    return rec1[0] < rec2[2] and rec2[0] < rec1[2] and rec1[1] < rec2[3] and rec2[1] < rec1[3]

print(rectangleOverlap(rec1 = [0,0,1,1], rec2 = [2,2,3,3]))