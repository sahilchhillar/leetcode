def mostCommonWord(paragraph, banned):
    words = {}
    temp = ""
    paragraph += '.'
    for i, char in enumerate(paragraph):
        if char.isalpha():
            temp += char
        else:
            temp = temp.lower()
            if temp not in banned and temp != "":
                if words.get(temp) is None:
                    words[temp] = 1
                else:
                    words[temp] += 1
            
            temp = ""
    print(words)

    maxWord, maxVal = "", 0
    for key, val in words.items():
        if val > maxVal:
            maxVal = val
            maxWord = key
    
    return maxWord

print(mostCommonWord(paragraph = "Bob. hIt, baLl", banned = ["bob", "hit"]))