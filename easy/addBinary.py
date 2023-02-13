def addBinary(a, b):
    i, j = len(a)-1, len(b)-1

    c = ''
    carry = '0'

    while i >= 0 and j >= 0:
        if a[i] == b[j] == '0':
            if carry == '1':
                c = '1' + c
            else:
                c = '0' + c
            carry = '0'
        
        elif a[i] != b[j]:
            if carry == '0':
                c = '1' + c
            else:
                c = '0' + c
                carry = '1'
        
        elif a[i] == b[j] == '1':
            if carry == '0':
                c = '0' + c
            else:
                c = '1' + c
            carry = '1'

        i -= 1
        j -= 1

    while i >= 0:
        if a[i] == '0':
            if carry == '1':
                c = '1' + c
                carry = '0'
            else:
                c = a[i] + c
        
        else:
            if carry == '1':
                c = '0' + c
                carry = '1'
            else:
                c = a[i] + c
            # carry = '1'
        
        i -= 1
    
    while j >= 0:
        if b[j] == '0':
            if carry == '1':
                c = '1' + c
                carry = '0'
            else:
                c = b[j] + c
        
        else:
            if carry == '1':
                c = '0' + c
            else:
                c = b[j] + c
            # carry = '1'

        j -= 1

    if carry == '1':
        c = '1' + c
    
    return c


print(addBinary("11", '1'))
