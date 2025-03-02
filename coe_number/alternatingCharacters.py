def alternatingCharacters(s):
    num=0
    for i in range(1,len(s)):
        if s[i-1]==s[i]:
            num+=1
    return num