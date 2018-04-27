'''
there is a homormofism between notes and integers mod
12
'''
n2note=dict(enumerate('A A# B C C# D D# E F F# G G#'.split()))
note2n=dict(map(lambda x:(x[1],x[0]),enumerate('A A# B C C# D D# E F F# G G#'.split())))
for i in 'ABCDEFG':
    note2n[i+'b']=(note2n[i]-1)%12
for i in 'ABCDEFG':
    note2n[i+'#']=(note2n[i]+1)%12

major='WWHWWWH'
minor='WHWWHWW'
def execute_scale(root,scale):
    rootN=note2n[root]
    for i in scale:
        if i=='W':
            rootN=(rootN+2)%12
        if i=='H':
            rootN=(rootN+1)%12
        yield n2note[rootN]

all_scales=list()
for i in range(12):
    all_scales.append(('M'+n2note[i],set(execute_scale(n2note[i],major))))
for i in range(12):
    all_scales.append(('m'+n2note[i],set(execute_scale(n2note[i],minor))))


def get_set(inp):
    if inp=='0':
        inp=set()
    else:
        inp=set(map(n2note.__getitem__,map(note2n.__getitem__,inp.split())
        ))
    a=[]
    for name,scale in all_scales:
        if set.issubset(inp,scale):
            a.append(name)
    return ' '.join(a) if a else 'None'
def comp(x):
    comp.n+=1
    return 'Case #%s: %s'%(comp.n,x)
comp.n=0
def avoid(s):
    while 1:
        ans=next(s)
        if ans=='0\n':
            yield ans
        else:
            yield next(s)
if __name__=='__main__':
    import sys
    S=sys.stdin
    next(S)
    for i in avoid(S):
        print(comp(get_set(i.strip())))

