def morseCode(words):
    codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    
    morse = set()
    
    for word in words:
        code = ""
        for w in word:
            pos = ord(w)-ord('a')
            code += codes[pos]
        
        morse.add(code)
    
    return len(morse)

print(morseCode(words = ["gin","zen","gig","msg"]))