
def parser_note(line):
    X,L,S,P=list(map(float,line.strip().split()))
    time_period_punt=((X)/S,(X+L)/S,P)
    return time_period_punt

def select(notes):
    
    notes.sort(key=lambda x:(x[0],-x[2]))
    return estimate_after_release(0,0,notes)

def memoize(f):
    def helper(*x):
        if x[:2]not in helper.memo:            
            helper.memo[x[:2]] = f(*x)
        return helper.memo[x[:2]]
    helper.memo={} 
    return helper

@memoize
def estimate_after_release(next_index_note,time_released,notes):
    next_index_note+=1
    while next_index_note<len(notes) and notes[next_index_note][0]<=time_released:
        next_index_note+=1
        
    if next_index_note>=len(notes):
        return 0
    _,time,punt=notes[next_index_note]
    case_pulse_note=punt+estimate_after_release(next_index_note,time,notes)
    case_pulse_not_note=estimate_after_release(next_index_note,time_released,notes)
    return max(case_pulse_not_note,case_pulse_note)

from itertools import groupby
def join_doubles(xs):
    for k,vs in groupby(xs,key=lambda x:x[:2]):
        yield k+(sum(map(lambda x:x[-1],vs)),)

def main():
   import sys
   sys.setrecursionlimit(10000)
   for p in range(int(next(sys.stdin))):
       lines_c=int(next(sys.stdin))
       notes_problem=[parser_note(next(sys.stdin)) for l in range(lines_c)]
       notes_problem.sort(key=lambda x:(x[0],x[1]))
       notes_problem=list(join_doubles(notes_problem))
       
       print('Case #%s: %s'%(p+1,int(estimate_after_release(-1,-1,notes_problem)))
            )
       estimate_after_release.memo={}
if __name__=='__main__':
    main()
