def fab(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b, c, count = 0, 1, 0, 2
    while count <= n:
        c = a+b
        a = b
        b = c
        count += 1
    return c

print(fab(6))