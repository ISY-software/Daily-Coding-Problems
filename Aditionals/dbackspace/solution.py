comps = int(input())


def srsh(searched, container):
    if len(searched) == 0 :
        if (len(container)%2 == 0):
            return True
        return False
    if len(container) == 0:
        return False
    if searched[0] == container[0]:
        return srsh(searched[1:], container[1:])
    if len(container) <= 2:
        return False
    return srsh(searched, container[2:])


for i in range(comps):
    s = str(input())
    t = str(input())
    bflag = False
    if len(t) <= len(s):
        indx = s.find(t[0])
        while(indx != -1):
            bflag = srsh(t[1:], s[indx+1:])
            if bflag :
                break
            s = s[indx+1:]
            indx = s.find(t[0])


    print('YES' if bflag else 'NO')
