def parser_note(line):
    X,L,S,P=list(map(float,line.strip().split()))
    time_period_punt=((X-L)/S,(X)/S,P)
    return time_period_punt

