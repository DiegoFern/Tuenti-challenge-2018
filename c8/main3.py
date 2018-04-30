from functools import reduce
from itertools import groupby
def parser(line,l):
    a,b=list(map(int,line.split()))
    return ((a-b-l )%a),a

def main():
    import sys
    for c in range(int(next(sys.stdin))):
        INEQS=[]
        for l in range(int(next(sys.stdin))):
            
            INEQS.append(list((parser(next(sys.stdin),l))))
    
        if 1 or c in (7,27):#option to debug
            try:
                print('Case #%s: %s'%(c+1,int(chinese_remainder(*list(zip(*rewrite(INEQS)))))))
            except :
                print('Case #%s: NEVER'%(c+1))

def rewrite(Ls):
    d={}
    ans=[]
    for L in Ls:
        a,n=L
        facts=factorize(n)
        for f,exp in facts:
            y=(a,f)
            if y not in d:
                ans.append((a%(f**exp),f,exp))
    ans.sort(key=lambda x:(-x[1],-x[2]))
    for _,v in groupby(ans ,key=lambda x:x[1],):
        v1=next(v)
        a1,f1,exp1=v1#x mod f^exp=a
        for a2,f,exp in v:
            if a1 % (f**exp)!=a2%(f**exp):
                raise Except()
        yield (a1,f1**exp1)


primes=[2]
for i in range(2,10000):
    if not(any(map(lambda x:i%x==0,primes))):
        primes.append(i)


def factorize(a):
    descomp=[]
    for p in primes:
        if a%p==0:
            descomp.append([p,1])
            a=a/p
            while a%p==0:
                descomp[-1][1]+=1
                a=a/p
    if a>1:
        descomp.append([a,1])
    return descomp

class Except(Exception):
    pass

def chinese_remainder(a,n):

    sum = 0
    prod = reduce(lambda a, b: a*b, n)
 
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: 
        return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: 
        x1 += b0
    return x1
 

def teoremaChino(elements, modules):
    m = 1
    M = list()
    I = list()
    sol = 0
    index = 0
    for module in modules: 
        m = m * module
    for module in modules: 
        M.append(int(m/module))
        I.append(inverso(M[index], modules[index]))
        sol = sol + (elements[index] * M[index] * I[index])
        index = index + 1

    # print(M)
    # print(I)
    # print(sol)
    return sol%MCM(modules)

def MCD(a,b):
    while b!=0:
        a=a%b
        a,b=b,a
    return a

def mcm(a,b):
    return a*b/MCD(a,b)

def MCM(modules):
    ans=modules[0]
    for i in (modules):
        ans=mcm(ans,i)
    return ans

if __name__=='__main__':
    main()
