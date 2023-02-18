def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    s_dict = {}
    t_dict = {}

    for i in range(len(s)):
        if s_dict.get(s[i]) is None and t_dict.get(t[i]) is None:
            s_dict[s[i]] = t[i]
            t_dict[t[i]] = s[i]
        
        elif s_dict.get(s[i]) != t[i] or t_dict.get(t[i]) != s[i]:
            return False
    return True

print(isIsomorphic("badc", "baba"))