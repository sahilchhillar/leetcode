def validParenthesis(s):
    brackets = ""

    for i in range(len(s)):
        if s[i] in ['(', '[', '{']:
            brackets += s[i]
        
        elif s[i] == ')' and (len(brackets) == 0 or brackets[len(brackets)-1] != '('):
            return False
        
        elif s[i] == ']' and (len(brackets) == 0 or brackets[len(brackets)-1] != '['):
            return False

        elif s[i] == '}' and (len(brackets) == 0 or brackets[len(brackets)-1] != '{'):
            return False
        
        else:
            brackets = brackets[:len(brackets)-1]
    
    if len(brackets) != 0:
        return False
    
    return True


print(validParenthesis("({}())[])"))