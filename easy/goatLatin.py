def isVowel(c):
    # vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
    # if c in vowels:
    #     return True
    # return False
    if c == 'a' or c == 'A' or c == 'e' or c == 'E' or c == 'i' or c == 'I' or c == 'o' or c == 'O' or c == 'u' or c == 'U':
        return True
    return False

def goatLatin(sentence):
    sentence = sentence
    goat = "ma"
    a_count = 1

    new_sentence = ""
    temp = ""
    for i, char in enumerate(sentence):
        if char != " ":
            temp += char
        else:
            if isVowel(temp[0]):
                new_sentence += temp + goat + 'a'*a_count + ' '
            else:
                new_sentence += temp[1:] + temp[0] + goat + 'a'*a_count + ' '
            temp = ""
            a_count += 1

    print(new_sentence[:-1])
    return new_sentence[:-1]
    
print(goatLatin(sentence = "I speak Goat Latin"))