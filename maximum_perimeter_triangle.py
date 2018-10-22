f=int(input())

for i in range(f):
    n=int(input())
    l=[]
    t=[]
    r=[]
    
    for i in range(n):
        st=input()
        s=list(st)
        k=0
        if len(s)==1:
            if st not in l:
                l.append(st)
                k=0.2
                t.append(k)
            else:

                k=t[l.index(st)]/2
                t.append(k)
                l.append(st)
        else:
            if st not in l:
                    l.append(st)
                    for i in range(len(s)-1):
                        if (s[i]=='d' or s[i]=='f') and (s[i+1]=='j' or s[i+1]=='k'):
                            k+=0.2
                        elif (s[i]=='d' or s[i]=='f') and (s[i+1]=='d' or s[i+1]=='f'):
                            k+=0.4
                        elif (s[i]=='j' or s[i]=='k') and (s[i+1]=='d' or s[i+1]=='f'):
                            k+=0.2
                        elif (s[i]=='j' or s[i]=='k') and (s[i+1]=='j' or s[i+1]=='k'):
                            k+=0.4
                    k=k+.2
                    t.append(k)
                
            else:
                
                l.append(st)
                k=t[l.index(st)]/2
                t.append(k)
    
    print(sum(t)*10)
 