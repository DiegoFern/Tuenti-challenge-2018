from scipy.optimize import linprog
import sys
from numpy import zeros,ones,array
def number_laser(N,M,pos):
    if len(pos)==0:
        return N+M
    c=[-1]*(N+M)#cost of linear programing
    A=zeros((len(pos),N+M))
    for i,(r,s) in enumerate(pos):
        A[i,r]=1
        A[i,N+s]=1
    b=ones(len(pos))
    res=linprog(array(c),A_ub=A,b_ub=b,bounds=list(zip(zeros(A.shape[1]),ones(A.shape[1])))).fun
    return -res
S=sys.stdin
for c in range(int(next(S))):
    N,M,I=map(int,next(S).split())
    pos=[]
    for i in range(int(I)):
        a,b=map(int,next(S).split())
        pos.append((a,b))
    print('Case #%s: %s'%(c+1,int(number_laser(N,M,pos))))
