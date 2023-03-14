def uncommonWords(s1, s2):
    words = []
    count = {}

    for word in s1.split():
        if count.get(word) is None:
            count[word] = 1
        else:
            count[word] += 1
    
    for word in s2.split():
        if count.get(word) is None:
            count[word] = 1
        else:
            count[word] += 1
    
    for key, val in count.items():
        if val == 1:
            words.append(key)
    
    return words

print(uncommonWords(s1 = "apple apple", s2 = "banana"))