def Iterator2(s):
    k=0

    while 1:
        for d in sorted(s.S):
            yield k*s.m+d
        k+=1
def Iterator(s):
    k=0
    while 1:
        for d in range(s.b,s.c+1):
            yield k*s.m+d
        k+=1
class solutions_ineq:
    '''
    giving the equation x mod m <- [b,c]
       returns the solutions
    '''
    def __init__(self,m,b,c):
        self.b=b
        self.m=m
        self.c=c
    def __contains__(self,x):
        ans=(x-self.b) %self.m
        return ans<=self.c-self.b
    def generator(self):
        return Iterator(self)
    def min(self):
        return next(Iterator(self))
class solutions_mult_ineq:
    '''
    giving the equation x mod m <- set
    returns the solutions
    '''
    def __init__(self,m,S):
        self.S={(m if (s%m==0) else s%m) for s in S}
        self.m=m

    def __contains__(self,x):
        ans=(x) %self.m
        return ans in self.S
    def min(self):
        return (min(self.S)) if self.S else 'IMPOSSIBLE'
    def __repr__(self):
        return 'solutions_mult_ineq(%s,%s)'%(self.m,self.S)
    def generator(self):
        return Iterator2(self)
def Intersection_bounded(A,B,bound):
    a=next(A)
    b=next(B)
    while a<bound and b<bound:
        if a==b:
            yield a
            a=next(A)
        elif a<b:
            a=next(A)
        else:
            b=next(B)
def takebounded(xs,b):
    for x in xs:
        if x<b:
            yield x
def MCD(a,b):
    while b!=0:
        a=a%b
        a,b=b,a
    return a
def MCM(a,b):
    return a*b/MCD(a,b)
def solve_multiples_ineq(INEQS):
    INEQS=iter(INEQS)
    Sol=next(INEQS)
    mcm=Sol.m
    for a in INEQS:
        mcm=MCM(a.m,mcm)
        candidates=set(Intersection_bounded(Sol.generator(),a.generator(),mcm+1))
        Sol=solutions_mult_ineq(mcm,candidates)
        
    return Sol

def parser(line,l):
    a,b=list(map(int,line.split()))
    return solutions_ineq(a,(a-b+l),(a-l),)
def main():
    import sys
    for c in range(int(next(sys.stdin))):
        INEQS=[]
        for l in range(int(next(sys.stdin))):
            INEQS.append((parser(next(sys.stdin),l)))
        print('Case #%s: %s'%(c+1,solve_multiples_ineq(INEQS)))

if __name__=='__main__':
    main()
