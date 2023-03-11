def flipImage(image):
    rows, cols = len(image), len(image[0])
    for i in range(rows):
        low, high = 0, cols-1
        while low <= high:
            image[i][low], image[i][high] = int(not image[i][high]), int(not image[i][low])
            low += 1
            high -= 1
    
    print(image)

flipImage(image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]])