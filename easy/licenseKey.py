def licenseKey(s, k):
    temp = ""
    key = ""
    s = s.upper()
    for i in range(len(s)-1, -1, -1):
        if s[i] != '-':
            temp = s[i] + temp
            if len(temp) == k:
                key = '-' + temp + key
                temp = ""

    if temp != '':
        key = temp + key
    
    if key == '':
        return key

    return key if key[0] != '-' else key[1:]
    
print(licenseKey(s = "2-5g-3-J", k = 2))