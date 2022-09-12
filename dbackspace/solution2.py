comps = int(input())

for i in range(comps):
    s = str(input())
    t = str(input())
    bflag = False
    if len(t) <= len(s):
        indx = s.find(t[0])
        while(indx != -1):
            serchedS = t[1:]
            containerS = s[indx+1:]
            while(True):
                if len(serchedS) == 0 :
                    if (len(containerS)%2 == 0):
                        bflag = True
                        break
                    bflag = False
                    break
                if len(containerS) == 0:
                    bflag = False
                    break
                
                sxindex = containerS.find(serchedS[0])
                if (sxindex == -1):
                    bflag = False
                    break

                containerS = containerS[sxindex+1:]
                if (sxindex % 2) == 0:
                    serchedS = serchedS[1:]


            if bflag :
                break
            s = s[indx+1:]
            indx = s.find(t[0])


    print('YES' if bflag else 'NO')
