import sys
s=sys.stdin
next(s)

def main(s):
    a,b=map(int,(s.split()))
    return max(0,a-1)*max(0,b-1)
def comp(x):
    comp.n+=1
    return 'Case #%s: %s'%(comp.n,x)
comp.n=0
if __name__=='__main__':
    for i in s:
        print(comp(main(i)))
