def keyboardRow(words):
    rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    keyChars = []
    for row in rows:
        for word in words:
            found = True
            for i in range(len(word)):
                if word[i].lower() not in row:
                    found = False
                    break
            if found:
                keyChars.append(word)

    return keyChars

print(keyboardRow(words = ["Hello","Alaska","Dad","Peace"]))