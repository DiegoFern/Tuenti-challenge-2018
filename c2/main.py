def assign_values_max(text):
    """
    Given a string of text give the maximun interpretation value:
    >assign_values_max('abab')
    """
    D_max={}
    v_max=len(set(text))-1
    exp=v_max+1
    for t in text:
        if t not in D_max:
            D_max[t]=v_max
            v_max-=1

    return sum(map(lambda x,y:x*(exp**y),map(D_max.__getitem__,reversed(text)),range(1000000)))

def assign_values_min(text):
    """
    Given a string of text give the maximun interpretation value:
    >assign_values_min('abab')
    """text2=text.replace(text[0],'')
    D_min={}
    exp=len(set(text))
    v_min=0
    D_min[text[0]]=1
    for t in text2:
        if t not in D_min:
            D_min[t]=v_min
            v_min+=1
            if v_min==1:
                v_min=2
    return sum(map(lambda x,y:x*(exp**y),map(D_min.__getitem__,reversed(text)),range(1000000)))

def main(s):
    t=s.strip()
    return assign_values_max(t)-assign_values_min(t)

def comp(x):
    comp.n+=1
    return 'Case #%s: %s'%(comp.n,x)
comp.n=0
if __name__=='__main__':
    import sys
    s=sys.stdin
    next(s)
    for i in s:
        print(comp(main(i)))
