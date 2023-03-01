def checkRecord(s):
    absent = 0
    
    for i, char in enumerate(s):
        if char == 'A':
            absent += 1
            if absent > 2:
                return False
        elif char == 'L':
            if i+1 < len(s) and i+2 < len(s):
                if s[i+1] == 'L' and s[i+2] == 'L':
                    return False
    
    return True
            
print(checkRecord(s = "PPALLAPA"))                