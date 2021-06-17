def solve123(al,sh):
    al=list(al)
    sh=list(sh)
    s=[]
    if sh[0]==al[3] and sh[2]==al[1]: s.append(0)
    elif sh[0]==al[3] and sh[2]==al[2]: s.append(1)
    elif sh[0]==al[4] and sh[2]==al[1]: s.append(4)
    elif sh[0]==al[4] and sh[2]==al[2]: s.append(5)
    if sh[1]==al[3] and sh[5]==al[1]: s.append(0)
    elif sh[1]==al[3] and sh[5]==al[2]: s.append(1)
    elif sh[1]==al[4] and sh[5]==al[1]: s.append(4)
    elif sh[1]==al[4] and sh[5]==al[2]: s.append(5)
    if sh[6]==al[1]:
        s.append(2)
        if sh[7]==al[0]: lt=True
        elif sh[7]==al[-1]: lt=False
    else:
        s.append(3)
        if sh[7]==al[0]: lt=False
        elif sh[7]==al[-1]: lt=True
    if sh[9]==al[2]:
        s.append(3)
        if sh[8]==al[0]: rt=True
        elif sh[8]==al[-1]: rt=False
    else:
        s.append(2)
        if sh[8]==al[0]: rt=False
        elif sh[8]==al[-1]: rt=True
    if sh[-2]==al[3] and sh[10]==al[1]: s.append(0)
    elif sh[-2]==al[3] and sh[10]==al[2]: s.append(1)
    elif sh[-2]==al[4] and sh[10]==al[1]: s.append(4)
    elif sh[-2]==al[4] and sh[10]==al[2]: s.append(5)
    if sh[-1]==al[3] and sh[13]==al[1]: s.append(0)
    elif sh[-1]==al[3] and sh[13]==al[2]: s.append(1)
    elif sh[-1]==al[4] and sh[13]==al[1]: s.append(4)
    elif sh[-1]==al[4] and sh[13]==al[2]: s.append(5)
    sh=s
    ans=[]
    if lt:
        if sh[2]==2: pass
        else:
            i0=sh.index(0)
            i1=sh.index(1)
            i2=sh.index(2)
            i3=sh.index(3)
            i4=sh.index(4)
            i5=sh.index(5)
            sh[i0],sh[i1],sh[i2],sh[i3],sh[i4],sh[i5]=sh[i1],sh[i0],sh[i3],sh[i2],sh[i5],sh[i4]
    elif rt:
        ans.append('M')
        sh[2],sh[3]=sh[3],sh[2]
        lt,rt=rt,lt    
        if sh[2]==2: pass
        else:
            i0=sh.index(0)
            i1=sh.index(1)
            i2=sh.index(2)
            i3=sh.index(3)
            i4=sh.index(4)
            i5=sh.index(5)
            sh[i0],sh[i1],sh[i2],sh[i3],sh[i4],sh[i5]=sh[i1],sh[i0],sh[i3],sh[i2],sh[i5],sh[i4]
    else:
        ans.append('L')
        sh[4],sh[0]=sh[0],sh[4]
        lt=not(lt)
        if sh[2]==2: pass
        else:
            i0=sh.index(0)
            i1=sh.index(1)
            i2=sh.index(2)
            i3=sh.index(3)
            i4=sh.index(4)
            i5=sh.index(5)
            sh[i0],sh[i1],sh[i2],sh[i3],sh[i4],sh[i5]=sh[i1],sh[i0],sh[i3],sh[i2],sh[i5],sh[i4]
    if sh[0]==0 and sh[1]==1:
        if sh[4]==4 and sh[5]==5: pass
        else:
            ans.append('D')
            sh[4],sh[5]=sh[5],sh[4]
    elif sh[0]==1 and sh[1]==0:
        if sh[4]==4 and sh[5]==5:
            ans.append('U')
            sh[1],sh[0]=sh[0],sh[1]
        else:
            ans.append('U')
            sh[1],sh[0]=sh[0],sh[1]
            ans.append('D')
            sh[4],sh[5]=sh[5],sh[4]
    elif sh[0]==0:
        if sh[4]==4 or sh[4]==5:
            ans.append('R')
            sh[1],sh[5]=sh[5],sh[1]
            rt=not(rt)
        else:
            ans.append('D')
            sh[4],sh[5]=sh[5],sh[4]
            ans.append('R')
            sh[1],sh[5]=sh[5],sh[1]
            rt=not(rt)
    elif sh[0]==1:
        if sh[4]==4 or sh[4]==5:
            ans.append('R')
            sh[1],sh[5]=sh[5],sh[1]
            rt=not(rt)
        else:
            ans.append('D')
            sh[4],sh[5]=sh[5],sh[4]
            ans.append('R')
            sh[1],sh[5]=sh[5],sh[1]
            rt=not(rt)
    elif sh[1]==0:
        ans.append('U')
        sh[1],sh[0]=sh[0],sh[1]
        if sh[4]==4 or sh[4]==5:
            ans.append('R')
            sh[1],sh[5]=sh[5],sh[1]
            rt=not(rt)
        else:
            ans.append('D')
            sh[4],sh[5]=sh[5],sh[4]
            ans.append('R')
            sh[1],sh[5]=sh[5],sh[1]
            rt=not(rt)
    elif sh[1]==1:
        ans.append('U')
        sh[1],sh[0]=sh[0],sh[1]
        if sh[4]==4 or sh[4]==5:
            ans.append('R')
            sh[1],sh[5]=sh[5],sh[1]
            rt=not(rt)
        else:
            ans.append('D')
            sh[4],sh[5]=sh[5],sh[4]
            ans.append('R')
            sh[1],sh[5]=sh[5],sh[1]
            rt=not(rt)
    else:
        ans.append('R')
        sh[1],sh[5]=sh[5],sh[1]
        ans.append('U')
        sh[1],sh[0]=sh[0],sh[1]
        ans.append('R')
        sh[1],sh[5]=sh[5],sh[1]
        ans.append('D')
        sh[4],sh[5]=sh[5],sh[4]
        ans.append('R')
        sh[1],sh[5]=sh[5],sh[1]
        rt=not(rt)
    if sh[0]!=0:
        ans.append('U')
        sh[1],sh[0]=sh[0],sh[1]
    if sh[4]!=4:
        ans.append('D')
        sh[4],sh[5]=sh[5],sh[4]
    if rt==False: ans+=['R','U','R','U','R','U']
    results=[]
    for item in ans:
        if results and item==results[-1]: results.pop()
        else: results.append(item)
    ans=results
    if len(ans)>1:
        if (ans[-1]=='U' and ans[-2]=='D') or (ans[-1]=='D' and ans[-2]=='U'):
            del ans[-1]
            ans[-1]='M'
    return ans
def solve122(al,sh):
    al=list(al)
    sh=list(sh)
    s=[]
    if sh[-2]==al[3] and sh[4]==al[-1]: s.append(1)
    elif sh[-2]==al[3] and sh[4]==al[0]: s.append(2)
    elif sh[-2]==al[4] and sh[4]==al[0]: s.append(0)
    elif sh[-2]==al[4] and sh[4]==al[-1]: s.append(3)
    if sh[0]==al[3] and sh[2]==al[0]: s.append(1)
    elif sh[0]==al[3] and sh[2]==al[-1]: s.append(2)
    elif sh[0]==al[4] and sh[2]==al[-1]: s.append(0)
    elif sh[0]==al[4] and sh[2]==al[0]: s.append(3)
    if sh[1]==al[3] and sh[3]==al[-1]: s.append(1)
    elif sh[1]==al[3] and sh[3]==al[0]: s.append(2)
    elif sh[1]==al[4] and sh[3]==al[0]: s.append(0)
    elif sh[1]==al[4] and sh[3]==al[-1]: s.append(3)
    if sh[-1]==al[3] and sh[-3]==al[0]: s.append(1)
    elif sh[-1]==al[3] and sh[-3]==al[-1]: s.append(2)
    elif sh[-1]==al[4] and sh[-3]==al[-1]: s.append(0)
    elif sh[-1]==al[4] and sh[-3]==al[0]: s.append(3)
    sh=s
    if sh[0]==0: fans=[0,1,2,3]
    elif sh[0]==1: fans=[1,0,3,2]
    elif sh[0]==2: fans=[2,3,0,1]
    else: fans=[3,2,1,0]
    ans=[]
    if sh!=fans:
        ans.append('R')
        sh[2],sh[3]=sh[3],sh[2]
    if sh!=fans:
        ans.append('U')
        sh[2],sh[1]=sh[1],sh[2]
    if sh!=fans:
        ans.append('R')
        sh[2],sh[3]=sh[3],sh[2]
    if sh!=fans:
        ans.append('U')
        sh[2],sh[1]=sh[1],sh[2]
    if sh!=fans:
        ans.append('R')
        sh[2],sh[3]=sh[3],sh[2]
    if len(ans)==5: ans=['U']
    if len(ans)==4: ans=['U','R']
    return ans
def solve222(inp):
    ts=[[inp[0],inp[5],inp[15]],[inp[1],inp[8],inp[14]],[inp[2],inp[11],inp[17]],[inp[3],inp[6],inp[16]]]
    bs=[[inp[-3],inp[4],inp[12]],[inp[-4],inp[9],inp[13]],[inp[-1],inp[10],inp[18]],[inp[-2],inp[7],inp[19]]]
    t=[{'W','R','G'},{'W','O','G'},{'W','O','B'},{'W','R','B'},{'Y','R','G'},{'Y','O','G'},{'Y','O','B'},{'Y','R','B'}]
    for i in range(4):
        ts[i]=[t.index(set(ts[i]))+1,ts[i]]
        bs[i]=[t.index(set(bs[i]))+1,bs[i]]
    turns=[]
    for v in range(1,5):
        if ts[3][0]==v:
            turns.extend("D' B' D".split())
            bs.insert(0,ts.pop())
            ts.append(bs.pop())
            bs[2],bs[3]=bs[3],bs[2]
            ts[3][1].reverse()
            bs[0][1].append(bs[0][1].pop(0))
            bs[1][1].append(bs[1][1].pop(1))
            bs[3][1].insert(0,bs[3][1].pop())
        elif ts[1][0]==v:
            turns.extend("R B R'".split())
            store=ts[1]
            ts[1]=bs.pop(1)
            bs.append(store)
            bs.reverse()
            ts[1][1][0],ts[1][1][1]=ts[1][1][1],ts[1][1][0]
            bs[0][1].insert(0,bs[0][1].pop())
            bs[1][1].append(bs[1][1].pop(0))
            bs[3][1][1],bs[3][1][2]=bs[3][1][2],bs[3][1][1]
        elif ts[2][0]==v:
            turns.extend("R' B2 R".split())
            store=ts[2]
            ts[2]=bs.pop(0)
            bs.insert(0,store)
            bs.append(bs.pop(2))
            ts[2][1].reverse()
            bs[0][1].reverse()
            bs[2][1].reverse()
            bs[3][1].reverse()
        elif bs[3][0]==v:
            turns.append("B'")
            bs.insert(0,bs.pop())
            for i in range(4):
                bs[i][1][1],bs[i][1][2]=bs[i][1][2],bs[i][1][1]
        elif bs[1][0]==v:
            turns.append("B")
            bs.append(bs.pop(0))
            for i in range(4):
                bs[i][1][1],bs[i][1][2]=bs[i][1][2],bs[i][1][1]
        elif bs[2][0]==v:
            turns.append("B2")
            bs[0],bs[2]=bs[2],bs[0]
            bs[1],bs[3]=bs[3],bs[1]
        elif ts[0][0]==v and ts[0][1][0]!='W':
            turns.extend("U B U' B'".split())
            store=ts[0]
            ts[0]=bs.pop(0)
            ts[0][1].reverse()
            bs.insert(0,store)
            bs[1],bs[2]=bs[2],bs[1]
            bs[0][1][0],bs[0][1][1]=bs[0][1][1],bs[0][1][0]
            bs[1][1].reverse()
            bs[2][1][1],bs[2][1][2]=bs[2][1][2],bs[2][1][1]
        if bs[0][1][2]=='W' and bs[0][0]==v:
            turns.extend("U B U'".split())
            store=ts[0]
            if v==1: ts[0]=[1,['W','R','G']]
            elif v==2: ts[0]=[2,['W','G','O']]
            elif v==3: ts[0]=[3,['W','O','B']]
            else: ts[0]=[4,['W','B','R']]
            bs[0]=bs.pop(2)
            bs.append(store)
            bs[0][1].insert(0,bs[0][1].pop())
            bs[2][1][1],bs[2][1][2]=bs[2][1][2],bs[2][1][1]
            bs[3][1].append(bs[3][1].pop(0))
        elif bs[0][1][1]=='W' and bs[0][0]==v:
            turns.extend("L' B' L".split())
            store=ts[0]
            if v==1: ts[0]=[1,['W','R','G']]
            elif v==2: ts[0]=[2,['W','G','O']]
            elif v==3: ts[0]=[3,['W','O','B']]
            else: ts[0]=[4,['W','B','R']]
            bs[0]=store
            bs.insert(0,bs.pop(2))
            bs[0][1].append(bs[0][1].pop(0))
            bs[1][1].insert(0,bs[1][1].pop())
            bs[2][1][1],bs[2][1][2]=bs[2][1][2],bs[2][1][1]
        elif bs[0][1][0]=='W' and bs[0][0]==v:
            turns.extend("U B2 U' B' U B U'".split())
            store=ts[0]
            if v==1: ts[0]=[1,['W','R','G']]
            elif v==2: ts[0]=[2,['W','G','O']]
            elif v==3: ts[0]=[3,['W','O','B']]
            else: ts[0]=[4,['W','B','R']]
            bs.pop(0)
            bs.append(store)
            bs.append(bs.pop(1))
            bs[0][1][0],bs[0][1][1]=bs[0][1][1],bs[0][1][0]
            bs[1][1].append(bs[1][1].pop(0))
            bs[2][1][0],bs[2][1][1]=bs[2][1][1],bs[2][1][0]
            bs[3][1][1],bs[3][1][2]=bs[3][1][2],bs[3][1][1]
        turns.append("F'")
        ts.append(ts.pop(0))
        for i in range(4):
            ts[i][1][1],ts[i][1][2]=ts[i][1][2],ts[i][1][1]
    turns.append("y2")
    yel=0
    for i in bs:
        if i[1][0]=='Y': yel+=1
    if yel==0:
        if bs[0][1][2]==bs[1][1][2]==bs[2][1][2]==bs[3][1][2]=='Y':
            turns.extend("R2 F2 R F2 R2".split())
            bs.insert(0,bs.pop())
            bs[0][1].reverse()
            bs[1][1].reverse()
            bs[2][1].reverse()
            bs[3][1].reverse()
        elif bs[0][1][1]==bs[1][1][1]==bs[2][1][1]==bs[3][1][1]=='Y':
            turns.extend("F R2 F2 R F2 R2".split())
            bs[0][1].append(bs[0][1].pop(0))
            bs[1][1].append(bs[1][1].pop(0))
            bs[2][1].append(bs[2][1].pop(0))
            bs[3][1].append(bs[3][1].pop(0))
        else:
            while not(bs[1][1][1]==bs[2][1][1]=='Y'):
                turns.append("F")
                bs.append(bs.pop(0))
                for i in range(4):
                    bs[i][1][1],bs[i][1][2]=bs[i][1][2],bs[i][1][1]
            turns.extend("R F2 R2 F' R2 F' R2 F2 R".split())
            bs=bs[2:]+bs[:2]
            bs[0][1].append(bs[0][1].pop(0))
            bs[1][1].insert(0,bs[1][1].pop())
            bs[2][1].insert(0,bs[2][1].pop())
            bs[3][1].append(bs[3][1].pop(0))
    if yel==1:
        while bs[3][1][0]!='Y':
            turns.append("F")
            bs.append(bs.pop(0))
            for i in range(4):
                bs[i][1][1],bs[i][1][2]=bs[i][1][2],bs[i][1][1]
        if bs[2][1][2]=='Y':
            turns.extend("L' F R F' L F R'".split())
            bs.insert(0,bs.pop(2))
            bs.append(bs.pop(2))
            bs[0][1].insert(0,bs[0][1].pop())
            bs[1][1].reverse()
            bs[2][1].append(bs[2][1].pop(1))
            bs[3][1].append(bs[3][1].pop(0))
        else:
            turns.extend("U F U' F U F2 U'".split())
            bs=bs[2:]+bs[:2]
            bs[0][1].append(bs[0][1].pop(0))
            bs[2][1].append(bs[2][1].pop(0))
            bs[3][1].insert(0,bs[3][1].pop())
    elif yel==2:
        if bs[0][1][0]==bs[2][1][0]=='Y' or bs[1][1][0]==bs[3][1][0]=='Y':
            while not(bs[0][1][1]=='Y'):
                turns.append("F")
                bs.append(bs.pop(0))
                for i in range(4):
                    bs[i][1][1],bs[i][1][2]=bs[i][1][2],bs[i][1][1]
            turns.extend("D R' D' R F R F' R'".split())
            bs.insert(2,bs.pop(0))
            bs[0][1][1],bs[0][1][2]=bs[0][1][2],bs[0][1][1]
            bs[1][1].reverse()
            bs[2][1].append(bs[2][1].pop(0))
        else:
            while not(bs[0][1][0]==bs[3][1][0]=='Y'):
                turns.append("F")
                bs.append(bs.pop(0))
                for i in range(4):
                    bs[i][1][1],bs[i][1][2]=bs[i][1][2],bs[i][1][1]
            if bs[1][1][1]=='Y':
                turns.extend("D R F R' F' D'".split())
                bs[0],bs[1]=bs[1],bs[0]
                bs[2],bs[3]=bs[3],bs[2]
                bs[0][1][0],bs[0][1][1]=bs[0][1][1],bs[0][1][0]
                bs[1][1][1],bs[1][1][2]=bs[1][1][2],bs[1][1][1]
                bs[2][1][1],bs[2][1][2]=bs[2][1][2],bs[2][1][1]
                bs[3][1][0],bs[3][1][1]=bs[3][1][1],bs[3][1][0]
            else:
                turns.extend("R F R' F' R' D R D'".split())
                bs.insert(0,bs.pop(2))
                bs[0][1].insert(0,bs[0][1].pop())
                bs[2][1].reverse()
                bs[1][1][1],bs[1][1][2]=bs[1][1][2],bs[1][1][1]
    same=0
    if not(bs[0][1][2]==bs[1][1][2] and bs[2][1][2]==bs[3][1][2]):
        for i in range(4):
            if bs[0][1][2]==bs[1][1][2]:
                same=1
                break
            turns.append("F")
            bs.append(bs.pop(0))
            for i in range(4):
                bs[i][1][1],bs[i][1][2]=bs[i][1][2],bs[i][1][1]
        if same==1:
            turns.extend("R' D R' U2 R D' R' U2 R2".split())
            bs.append(bs.pop(0))
            bs[1],bs[2]=bs[2],bs[1]
            bs[0][1][1],bs[0][1][2]=bs[0][1][2],bs[0][1][1]
            bs[3][1][1],bs[3][1][2]=bs[3][1][2],bs[3][1][1]
        else:
            turns.extend("D R F' R' F' R F R' D' R F R' F' R' D R D'".split())
            bs[1],bs[3]=bs[3],bs[1]
    while bs!=sorted(bs):
        turns.append("F")
        bs.append(bs.pop(0))
        for i in range(4):
            bs[i][1][1],bs[i][1][2]=bs[i][1][2],bs[i][1][1]
    ans=[]
    for i in turns:
        if ans and i[0]==ans[-1][0]:
            if len(i)==1:
                if len(ans[-1])==1: ans[-1]=i+'2'
                elif ans[-1][1]=='2': ans[-1]=i+"'"
                else: ans.pop()
            elif i[1]=='2':
                if len(ans[-1])==1: ans[-1]=ans[-1][0]+"'"
                elif ans[-1][1]=='2': ans.pop()
                else: ans[-1]=ans[-1][0]
            else:
                if len(ans[-1])==1: ans.pop()
                elif ans[-1][1]=='2': ans[-1]=ans[-1][0]
                else: ans[-1]=ans[-1][0]+'2'
        else: ans.append(i)
    if ans[-1]=='y2': ans.pop()
    return ans
