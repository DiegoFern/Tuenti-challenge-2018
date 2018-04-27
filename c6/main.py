
def parser_note(line):
    X,L,S,P=list(map(float,line.strip().split()))
    time_period_punt=((X)/S,(X+L)/S,P)
    return time_period_punt

def select(notes):
    
    notes.sort(key=lambda x:(x[0],-x[2]))
    print(notes)
    last=-float('inf')
    for i in notes:
        if last<i[0]:
            yield i[-1]
            last=i[1]

def greedy_main(s):
    L=list(map(parser_note,s.split('\n')
            ))

    return list(select(L))



