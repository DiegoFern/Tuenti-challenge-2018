def MCD(a,b):
    while b!=0:
        a=a%b
        a,b=b,a
    return a

def MCM(a,b):
    return a*b/MCD(a,b)

def parser(line,l):
    a,b=list(map(int,line.split()))
    return ineq(a,b,l)#inequation wich a*(k)-b<x+l<a*k

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

class ineq:
    def __init__(self,a,b,l):
        self.b=b
        self.a=a
        self.l=l
        def generator(a,b,l):
            A,B=self.a-self.b,self.a
            k=0
            while A<B:
                for d in range(A,B+1):
                    yield k*B+d-l
                k+=1
        self.gen=generator
    def __contains__(self,x):
        return self.a-self.b<((x+self.l)%self.a)
    def __iter__(self):
        return self.gen(self.a,self.b,self.l)

def main():
    import sys
    for c in range(int(next(sys.stdin))):
        INEQS=[]
        for l in range(int(next(sys.stdin))):
            INEQS.append((parser(next(sys.stdin),l)))
        print('Case #%s: %s'%(c+1,solve_multiples_ineq(INEQS)))

if __name__=='__main__':
    main()
