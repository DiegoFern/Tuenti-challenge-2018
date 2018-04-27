import networkx as nx
import numpy as np
def table2graph(table):
    """
    table is list(string) with the 
       returns G:a Graph with legals jumps
                start:start_node
                end:end_node
    """
    G=nx.DiGraph()
    size=len(table),len(table[0])#size of the table
    explored={}#nodes expanded
    for i,t in enumerate(table):
        for j,pos in enumerate(t):
            if pos in ('D','S','P','.','*'):
                
                if pos=='S':
                    begin=(i,j)
                elif pos=='P':
                    princess=(i,j)
                elif pos=='D':
                    end=(i,j) 
                for mov in legal_movs(i,j,pos,size,table):
                    G.add_edge((i,j),mov)
    return G,begin,princess,end


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
        G,begin,princess,end=table2graph(np.array(table))
        try:
            ans=int(nx.shortest_path_length(G,begin,princess)+nx.shortest_path_length(G,princess,end))

        except nx.NetworkXException:
            ans='IMPOSSIBLE'
        print(comp((ans)))
