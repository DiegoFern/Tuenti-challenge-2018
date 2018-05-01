from bisect import *
def login(f):
    def ans(*arg):
        print('%s(%s)'%(f.__name__,','.join(map(str,arg))))
        a=f(*arg)
        print('%s(%s)'%(
            f.__name__,','.join(map(str,arg))),'>',a)
        return a
    return ans
def pp(i):
    print(i)
    return 1
@login
def f(a,b,S,n=None):
    u=a
    s=0
    if a>b:
        return 0
    if a-b%2==0:
        return 0
    if a+1==b:
        return 1
    for v in range(a+1,b+1):
        print((u,v),(v+2,b,S,n))
        #with u,v vertex fixed
        #s+=f(u,v+1,S,n)*f(v+2,b,S,n)
    return s
def memoize(f):
    def helper(*x):
        if x not in helper.memo:            
            helper.memo[x] = f(*x)
        return helper.memo[x]
    helper.memo={} 
    return helper
import sys
sys.setrecursionlimit(10000) 
class restriction(frozenset):
    def __init__(self,*args,**kargs):
        super()
        self.min=sorted(set(l for i in self for l in i))

    def not_restriction(self,a,b):
        index_1=bisect_left(self.min,(a),)
        index_2=bisect_left(self.min,(b),)
        return (index_1==index_2)
mod=10**9+7
@memoize
def f2(a,b,S):
    if a>0 and S.not_restriction(a-1,b):
        return f2(0,b-a,S)
    if a==2+b:return 1
    if a==b:return 1
    s=0
    for i in range(a+1,b):
        if (a,i) not in S:
            s+=f2(a+1,i,S)*f2(i+1,b,S)
    return s%(mod)
def main():
    import sys
    S=sys.stdin
    for c in range(int(next(S))):
        P,NR=tuple(map(int,next(S).split()))
        s=set()
        for n in range(NR):
            line=tuple(map(int,(next(S).split())))
            if 0 :#c in (6,17,):
                print(line,P)
            if line[0]>line[1]:
                line=(line[1],line[0])
            s.add(line)
        s=restriction(s)
        f2.memo.clear()
        print('Case #%s: %s'%(c+1,f2(0,P,s)))
if __name__=='__main__':
    main()
