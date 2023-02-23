"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring consisting of non-space characters only.
"""

def lengthOfLastWord(s):
    #Solution 1 -> More space complexity
    # s_list = s.split()
    # return len(s_list[len(s_list)-1])
        
    #Solution 2 -> More time complexity
    i, length = len(s)-1, 0

    while s[i] == " ":
        i -= 1
        
    while i >= 0 and s[i] != " ":
        length += 1
        i -= 1
        
    return length