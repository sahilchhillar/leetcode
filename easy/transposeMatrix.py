def tranpose(mat):
    rows, cols = len(mat), len(mat[0])
    ans = [[None for i in range(rows)] for j in range(cols)]
    print(ans)

    for i in range(rows):
        for j in range(cols):
            ans[j][i] = mat[i][j]
    
    return ans


print(tranpose(mat = [[1,2,3],[4,5,6],[7,8,9]]))