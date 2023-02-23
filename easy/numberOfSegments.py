def numberOfSegments(s):
    temp = ""
    count = 0

    for i, char in enumerate(s):
        if char != " ":
            temp += char
        else:
            if temp != "":
                count += 1
                temp = ""
    
    if temp != "":
        count += 1
    return count

print(numberOfSegments(s = "Hello      "))