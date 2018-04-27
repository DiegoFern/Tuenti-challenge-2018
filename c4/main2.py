import networkx as nx
import numpy as np
from collections import deque
        
def main(table):
    """
    table is list(string) with the 
    return distance ('IMPOSSIBLE' if there is no solution)
    """
    G=nx.DiGraph()
    size=len(table),len(table[0])#size of the table
    explored=dict()#nodes expanded
    to_explored=list()
    for i,t in enumerate(table):
        for j,pos in enumerate(t):
            if pos in ('D','S','P','.','*'):
                
                if pos=='S':
                    begin=(i,j)
                elif pos=='P':
                    princess=(i,j)
                elif pos=='D':
                    end=(i,j) 
    to_explored.append(begin)
    i,j=begin
    to_explored_set=set(to_explored)
    path1=distance(begin,princess,table,size)
    if path1 is None:
        return 'IMPOSSIBLE'
    path2=distance(princess,end,table,size)
    if path2 is None:
        return 'IMPOSSIBLE'

    return path2+path1 
def distance(begin,end,table,size):
    seen_nodes=set()
    queue=[]
    queue.append(begin)
    i,j=begin
    distance={}
    while queue and (i,j)!=end:
        i,j=queue.pop(0)
        if (i,j) in seen_nodes:
            continue
        for m in list(legal_movs(i,j,table[i][j],size,table)):
            if m in seen_nodes:
                pass
            else:
                distance[m]=min(distance.get((i,j),0)+1,distance.get(m,10**100))
                queue.append(m)
        seen_nodes.add((i,j))
    return None if end not in distance else distance[end]


def legal_movs(i,j,pos,size,table):
    if pos=='*':
        jumps=[(2,4),(4,2),(-2,4),(-4,2),
                (2,-4),(4,-2),(-2,-4),(-4,-2),]
    else:
        jumps=[(1,2),(2,1),(-1,2),(-2,1),
                (1,-2),(2,-1),(-1,-2),(-2,-1),]
    for di,dj in jumps:
        I=di+i
        J=dj+j
        if (I>=0 and size[0]>I and J>=0 and size[1]>J
            and table[I][J]!='#'):
            yield (I,J)
def comp(x):
    comp.n+=1
    return 'Case #%s: %s'%(comp.n,x)
comp.n=0

if __name__=='__main__':
    import sys
    s=sys.stdin
    for problem in range(int(next(s))):
        s1,s2=list(map(int,next(s).split()))
        table=[]
        for i in range(s1):
            table.append(next(s).strip())
        ans=main(np.array(table))

        print(comp((ans)))
