def jewelStone(jewels, stones):
    st = {}
    for s in stones:
        if st.get(s) is None:
            st[s] = 1
        else:
            st[s] += 1
    
    count = 0
    for j in jewels:
        if st.get(j) is not None:
            count += st.get(j)
    
    return count

print(jewelStone(jewels = "aA", stones = "aAAbbbb"))