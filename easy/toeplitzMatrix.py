def toeplitz(mat):
    rows = len(mat)
    cols = len(mat[0])

    group = {}

    for i in range(rows):
        for j in range(cols):
            key = i-j
            if group.get(key) is None:
                group[key] = mat[i][j]
            else:
                if group[key] != mat[i][j]:
                    return False
    return True

print(toeplitz(mat = [[11,74,0,93],[40,11,74,7]]))