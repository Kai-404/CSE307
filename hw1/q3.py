def q3():
    s1 = input()
    s2 = input()

    if s1 == s2 == "":
        return False
    elif s1 == "":
        if s2[0] == s2[-1] and (s2[0] != "\"" or s2[0] != "\'") :
            return True
        else:
            return False

    elif s2 == "":
        if s1[0] == s1[-1] and (s1[0] != "\"" or s1[0] != "\'") :
            return True
        else:
            return False

    elif s1[0] != '\'' and s1[0] != "\"" :
        return False
    elif s1[-1] != '\\':
        return False
    elif s1[0] != s2[-1]:
        return False
    
    s = s1[0:-1]+s2
    
    i = 0
    while i < len(s):
        if s[i] == "\\":
            if s[i+1] != "\'" and s[i+1] != "\"" and s[i+1] != "\\" :
                return False
            else:
                s = s[0:i]+s[i+2:]
                i=i-1
        else:
            i=i+1
    return True


if __name__ == "__main__":
    print(str(q3()))

