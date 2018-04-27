
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
    next_index_note_bis=next_index_note
    while next_index_note<len(notes) and notes[next_index_note][0]<time_released:
        next_index_note+=1
        
    if next_index_note>=len(notes):
        return 0
    time,period,punt=notes[next_index_note]
    return max(punt+estimate_after_release(next_index_note+1,time+1,notes),
            estimate_after_release(next_index_note_bis+1,time_released,notes))

def main():
   import sys
   for p in range(int(next(sys.stdin))):
       lines_c=int(next(sys.stdin))
       print('-'*100)
       notes_problem=[parser_note(next(sys.stdin)) for l in range(lines_c)]
       notes_problem.sort(key=lambda x:(x[0],-x[2]))
       print(notes_problem)
       print(estimate_after_release(0,-1,notes_problem)
            )
       print(estimate_after_release.memo)
       estimate_after_release.memo={}
if __name__=='__main__':
    main()
