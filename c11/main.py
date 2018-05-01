from scipy.optimize import linprog
import sys
from numpy import zeros,ones,array
import numpy as np
def number_laser3(N,M,pos):
    if len(pos)==0:
        return N+M
    #cost of linear programing
    A=zeros((len(pos),N+M))
    for i,(r,s) in enumerate(pos):
        A[i,r]=-1
        A[i,N+s]=-1
    #A=A[:,A.sum(axis=0)<1]

    b=ones(len(pos))*-1
    #d=N+M-A.shape[1]
    res=linprog(
            ones(A.shape[1]),A_ub=A,b_ub=b,bounds=list(
                zip(zeros(A.shape[1]),ones(A.shape[1])))).fun
    return N+M-abs(-res)
def number_laser(N,M,pos):
    if len(pos)==0:
        return N+M
    #cost of linear programing
    A=zeros((len(pos),N+M))
    for i,(r,s) in enumerate(pos):
        A[i,r]=1
        A[i,N+s]=1
    #A=A[:,A.sum(axis=0)<1]

    b=ones(len(pos))
    #d=N+M-A.shape[1]
    res=linprog(
            -ones(A.shape[1]),A_ub=-A,b_ub=b,bounds=list(
                zip(zeros(A.shape[1]),ones(A.shape[1])))).fun
    return abs(-res)
def number_laser2(N,M,pos):
    Pos=zeros((N,M))
    luces=N+M
    for a,b in pos:
        Pos[a,b]=1
    N=ones(N);M=ones(M)
    Y=Pos.sum(axis=0)
    X=Pos.sum(axis=1)
    while np.any(X>1) or np.any(Y>1):
        luces-=1
        if X.max()>Y.max():
            Pos[np.argmax(X),:]=0

        else:
            Pos[:,np.argmax(Y)]=0
        X=Pos.sum(axis=1)
        Y=Pos.sum(axis=0)
    return luces


    



S=sys.stdin
for c in range(int(next(S))):
    N,M,I=map(int,next(S).split())
    pos=[]
    for i in range(int(I)):
        a,b=map(int,next(S).split())
        pos.append((a,b))
    print('Case #%s: %s'%(c+1,int(number_laser3(N,M,pos))))
