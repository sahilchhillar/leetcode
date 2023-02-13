def pascalsTriangle(rows):
    if rows == 1:
        return [[1]]

    triangle = [[1], [1,1]]
    for i in range(1, rows):
        lastRow = triangle[i]
        row = [lastRow[0]]
        for j in range(1, len(lastRow)):
            sum = lastRow[j]+lastRow[j-1]
            row.append(sum)
        row.append(lastRow[len(lastRow)-1])
        triangle.append(row)

    return triangle


print(pascalsTriangle(6))           