def reshapeMatrix(mat, r, c):
    if (r == len(mat) and c == len(mat[0])) or (len(mat)*len(mat[0]) != r*c):
        return mat
    
    rows, cols = len(mat), len(mat[0])
    arr = [[0 for j in range(c)] for i in range(r)]
    rIndex, cIndex = 0, 0
    for i in range(rows):
        for j in range(cols):
            if cIndex == c:
                rIndex += 1
                cIndex = 0

            arr[rIndex][cIndex] = mat[i][j]
            cIndex += 1
    return arr

reshapeMatrix(mat = [[1,2],[3,4]], r = 4, c = 1)