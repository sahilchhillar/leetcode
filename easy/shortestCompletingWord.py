import sys

def shortestCompletingWord(licensePlate, words):
    licensePlate = licensePlate.lower()
    license = {}
    for char in licensePlate:
        if char.isalpha():
            if license.get(char) is None:
                license[char] = 1
            else:
                license[char] += 1
    
    print(license)
    shortest = sys.maxsize
    shortestWord = words[0]
    for word in words:
        word = word.lower()
        temp = {}
        for char in word:
            if temp.get(char) is None:
                temp[char] = 1
            else:
                temp[char] += 1
        
        print(temp)
        found = True
        for key, val in license.items():
            if key not in temp.keys() or val > temp.get(key):
                found = False
                break
        # print(found)
        if found:
            if len(word) < shortest:
                shortest = len(word)
                shortestWord = word

    return shortestWord

print(shortestCompletingWord(licensePlate = "GrC8950", words = ["measure","other","every","base","according","level","meeting","none","marriage","rest"]))