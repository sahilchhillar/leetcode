def numberOfLines(widths, s):
    countLine = 1
    pixelLength = 0
    for c in s:
        if pixelLength + widths[ord(c)-ord('a')] > 100:
            countLine += 1
            pixelLength = widths[ord(c)-ord('a')]
        else:
            pixelLength += widths[ord(c)-ord('a')]
    
    return [countLine, pixelLength]

print(numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz"))